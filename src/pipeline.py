"""
Pipeline orchestration for transformation consultant agent.

This module provides classes for building and executing pipelines that
chain together multiple components in sequence.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import json

from .interfaces.component import BaseComponent, ComponentResult


@dataclass
class PipelineResult:
    """Result of pipeline execution."""

    success: bool
    outputs: Dict[str, Any]
    metadata: Dict[str, Any]
    errors: List[str] = field(default_factory=list)
    timestamp: Optional[datetime] = None

    def __post_init__(self):
        """Set timestamp if not provided."""
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def save_outputs(self, output_dir: Path):
        """
        Save pipeline outputs to files.

        Args:
            output_dir: Directory to save outputs to
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        for component_name, output_data in self.outputs.items():
            # Skip None outputs (from failed components)
            if output_data is None:
                continue

            # Determine file extension
            if "BPMN" in component_name:
                ext = ".bpmn"
            elif "Analysis" in component_name:
                ext = "-analysis.md"
            elif "Optimization" in component_name:
                ext = "-recommendations.md"
            else:
                ext = ".txt"

            # Save output
            filename = f"{component_name.lower().replace(' ', '-')}{ext}"
            output_path = output_dir / filename
            output_path.write_text(output_data, encoding='utf-8')

        # Save metadata
        metadata_path = output_dir / "pipeline-metadata.json"
        metadata_path.write_text(
            json.dumps(self.metadata, indent=2, default=str),
            encoding='utf-8'
        )


class Pipeline:
    """
    Orchestrates execution of components in sequence.

    A pipeline is a directed sequence of components where
    the output of one component becomes the input to the next.
    """

    def __init__(self, name: str):
        """
        Initialize pipeline.

        Args:
            name: Human-readable pipeline name
        """
        self.name = name
        self.components: List[BaseComponent] = []
        self.component_configs: List[Dict[str, Any]] = []

    def add_component(self,
                     component: BaseComponent,
                     config: Optional[Dict[str, Any]] = None):
        """
        Add a component to the pipeline.

        Args:
            component: Component instance to add
            config: Component-specific configuration for execution
        """
        self.components.append(component)
        self.component_configs.append(config or {})

    def execute(self,
                initial_input: Any,
                stop_on_error: bool = True) -> PipelineResult:
        """
        Execute pipeline from start to finish.

        Args:
            initial_input: Input to first component
            stop_on_error: If True, stop pipeline on first error

        Returns:
            PipelineResult with all outputs and metadata
        """
        outputs = {}
        errors = []
        metadata = {
            "pipeline_name": self.name,
            "components": [c.component_name for c in self.components],
            "start_time": datetime.now().isoformat()
        }

        # Track current input (output of previous component)
        current_input = initial_input

        # Store intermediate outputs for non-sequential access
        intermediate_outputs = {}

        # Execute each component in sequence
        for i, (component, config) in enumerate(zip(self.components, self.component_configs)):
            component_name = component.component_name
            print(f"[Pipeline] Executing: {component_name} ({i+1}/{len(self.components)})")

            try:
                # Check if config specifies a specific input to use
                if 'input_from' in config:
                    input_component = config['input_from']
                    if input_component in intermediate_outputs:
                        current_input = intermediate_outputs[input_component]
                        print(f"[Pipeline] Using output from '{input_component}' as input")
                    else:
                        raise ValueError(f"Component '{input_component}' output not found")

                # Execute component
                result = component.process(current_input, **config)

                # Store result
                outputs[component_name] = result.data
                intermediate_outputs[component_name] = result.data

                # Track metadata
                if component_name not in metadata:
                    metadata[component_name] = {}
                metadata[component_name] = result.metadata

                # Check for errors
                if not result.success:
                    error_msg = f"{component_name} failed: {result.error}"
                    errors.append(error_msg)
                    print(f"[Pipeline] ERROR: {error_msg}")

                    if stop_on_error:
                        print(f"[Pipeline] Stopping pipeline due to error")
                        break
                    else:
                        # Continue with None input
                        current_input = None
                else:
                    # Success - pass output to next component
                    current_input = result.data
                    print(f"[Pipeline] SUCCESS: {component_name} completed")

            except Exception as e:
                error_msg = f"{component_name} raised exception: {str(e)}"
                errors.append(error_msg)
                print(f"[Pipeline] EXCEPTION: {error_msg}")

                if stop_on_error:
                    break
                else:
                    current_input = None

        # Pipeline completion
        metadata["end_time"] = datetime.now().isoformat()
        metadata["total_components"] = len(self.components)
        metadata["completed_components"] = len(outputs)

        success = len(errors) == 0

        return PipelineResult(
            success=success,
            outputs=outputs,
            metadata=metadata,
            errors=errors
        )
