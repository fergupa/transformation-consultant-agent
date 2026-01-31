"""
Transcript processor component.

This component analyzes process transcripts and extracts structured information
using the transcript-analysis skill.
"""

from pathlib import Path
from typing import Any
from ...interfaces.component import BaseComponent, ComponentResult


class TranscriptProcessor(BaseComponent):
    """
    Component for analyzing process transcripts and extracting structured information.

    Implements the transcript-analysis skill.
    """

    @property
    def component_name(self) -> str:
        """Return human-readable component name."""
        return "Transcript Analysis"

    @property
    def skill_path(self) -> Path:
        """Return path to SKILL.md file for this component."""
        return Path(__file__).parent.parent.parent.parent / "skills" / "transcript-analysis" / "SKILL.md"

    def validate_input(self, input_data: Any) -> bool:
        """
        Validate that input is a non-empty string (transcript text).

        Args:
            input_data: Expected to be transcript text

        Returns:
            True if valid

        Raises:
            ValueError: If input is invalid
        """
        if not isinstance(input_data, str):
            raise ValueError(f"Input must be string, got {type(input_data)}")
        if not input_data.strip():
            raise ValueError("Transcript text cannot be empty")
        if len(input_data) < 100:
            raise ValueError("Transcript text seems too short (< 100 chars)")
        return True

    def process(self, input_data: str, **kwargs) -> ComponentResult:
        """
        Analyze transcript and extract structured process information.

        Args:
            input_data: Transcript text to analyze
            **kwargs: Optional parameters:
                - domain_knowledge: List of domain knowledge filenames to include

        Returns:
            ComponentResult with analysis markdown in data field
        """
        try:
            # Validate input
            self.validate_input(input_data)

            # Load skill prompt
            skill_prompt = self._load_skill_prompt()

            # Prepare system messages
            system_messages = [{"type": "text", "text": skill_prompt}]

            # Optionally load domain knowledge examples
            domain_knowledge = kwargs.get('domain_knowledge', [])
            if domain_knowledge:
                from ...skills.skill_manager import SkillManager
                manager = SkillManager()
                for dk_file in domain_knowledge:
                    dk_content = manager.load_domain_knowledge('transcript-analysis', dk_file)
                    system_messages.append({
                        "type": "text",
                        "text": f"# Domain Knowledge Example\n\n{dk_content}",
                        "cache_control": {"type": "ephemeral"}
                    })

            # Prepare user message
            user_message = f"Please analyze the following process transcript:\n\n{input_data}"

            # Call Claude
            analysis_text, api_metadata = self._call_claude(
                user_message=user_message,
                system_messages=system_messages,
                max_tokens=16000,
                temperature=0
            )

            # Return result
            return ComponentResult(
                success=True,
                data=analysis_text,
                metadata={
                    **api_metadata,
                    "component": self.component_name,
                    "transcript_length": len(input_data)
                }
            )

        except ValueError as e:
            return ComponentResult(
                success=False,
                data=None,
                metadata={"component": self.component_name},
                error=f"Validation error: {str(e)}"
            )
        except Exception as e:
            return ComponentResult(
                success=False,
                data=None,
                metadata={"component": self.component_name},
                error=f"Processing error: {str(e)}"
            )
