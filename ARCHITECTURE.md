# Transformation Consultant Agent - Architecture

This document describes the architectural design and key decisions for the transformation consultant agent's modular component-based architecture.

## Overview

The transformation consultant agent is built using a **component-based pipeline architecture** that enables modular, reusable, and testable code. The system transforms business process transcripts into structured analyses, BPMN diagrams, and optimization recommendations.

## Design Philosophy

### Component-Based Architecture

Each skill (transcript analysis, BPMN generation, process optimization) is implemented as a Python component that:
- Implements a common `BaseComponent` interface
- Loads its system prompt from a SKILL.md file
- Validates input and output
- Returns standardized `ComponentResult` objects

Benefits:
- **Modularity**: Components can be developed, tested, and deployed independently
- **Reusability**: Components can be used in different pipelines or contexts
- **Testability**: Unit tests for individual components, integration tests for pipelines
- **Maintainability**: Clear separation of concerns and standardized patterns

### Pipeline Orchestration

The `Pipeline` class orchestrates sequential execution of components, where the output of one component becomes the input to the next. This enables:
- **Automatic data flow**: No manual wiring required
- **Error handling**: Graceful failure handling with detailed error messages
- **State tracking**: Monitor execution state and intermediate results
- **Observability**: Logging and metrics throughout execution

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      Main Orchestrator                      │
│                       (src/main.py)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ create_full_pipeline()                               │  │
│  │ create_analysis_pipeline()                           │  │
│  │ create_bpmn_pipeline()                               │  │
│  │ run_full_transformation()                            │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Pipeline Manager                         │
│                    (src/pipeline.py)                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Pipeline.execute(input) → PipelineResult             │  │
│  │   - Sequential execution                             │  │
│  │   - Pass output to next component                    │  │
│  │   - Track metadata (tokens, timing)                  │  │
│  │   - Handle errors gracefully                         │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌───────────────┐ ┌───────────┐ ┌─────────────────┐
│ Transcript    │ │   BPMN    │ │ Recommendation  │
│ Processor     │ │ Generator │ │     Engine      │
│ (Component 1) │ │(Component │ │  (Component 3)  │
└───────┬───────┘ └─────┬─────┘ └────────┬────────┘
        │               │                 │
        └───────────────┴─────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │    BaseComponent Interface    │
        │  (src/interfaces/component.py)│
        │  ┌─────────────────────────┐  │
        │  │ validate_input()        │  │
        │  │ process() →             │  │
        │  │   ComponentResult       │  │
        │  │ _call_claude()          │  │
        │  └─────────────────────────┘  │
        └───────────────┬───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │      Skill Manager            │
        │  (src/skills/skill_manager.py)│
        │  ┌─────────────────────────┐  │
        │  │ load_skill_prompt()     │  │
        │  │ load_domain_knowledge() │  │
        │  └─────────────────────────┘  │
        └───────────────┬───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │     SKILL.md Files            │
        │  (skills/*/SKILL.md)          │
        │  - System prompts             │
        │  - Domain knowledge           │
        └───────────────────────────────┘
```

## Directory Structure

```
src/
├── __init__.py
├── main.py                           # Main orchestrator
├── pipeline.py                       # Pipeline manager
├── interfaces/
│   ├── __init__.py
│   └── component.py                  # BaseComponent, ComponentResult
├── components/
│   ├── __init__.py
│   ├── input/
│   │   ├── __init__.py
│   │   └── transcript_processor.py   # TranscriptProcessor component
│   ├── analysis/
│   │   └── __init__.py               # Placeholder for future
│   ├── generation/
│   │   ├── __init__.py
│   │   └── bpmn_generator.py         # BPMNGenerator component
│   └── optimization/
│       ├── __init__.py
│       └── recommendation_engine.py   # RecommendationEngine component
└── skills/
    ├── __init__.py
    └── skill_manager.py              # Skill loader
```

## Core Interfaces

### ComponentResult

Standardized result format from component execution:

```python
@dataclass
class ComponentResult:
    success: bool                     # True if processing succeeded
    data: Any                         # Output data (markdown, XML, etc.)
    metadata: Dict[str, Any]          # Execution metadata (tokens, timing)
    error: Optional[str] = None       # Error message if failed
    timestamp: Optional[datetime] = None
```

### BaseComponent

Abstract base class that all components must implement:

```python
class BaseComponent(ABC):
    @property
    @abstractmethod
    def component_name(self) -> str:
        """Human-readable component name."""
        pass

    @property
    @abstractmethod
    def skill_path(self) -> Path:
        """Path to SKILL.md file."""
        pass

    @abstractmethod
    def validate_input(self, input_data: Any) -> bool:
        """Validate input before processing."""
        pass

    @abstractmethod
    def process(self, input_data: Any, **kwargs) -> ComponentResult:
        """Execute main processing logic."""
        pass
```

## Component Implementations

### TranscriptProcessor

- **Location**: [src/components/input/transcript_processor.py](src/components/input/transcript_processor.py)
- **Skill**: `skills/transcript-analysis/SKILL.md`
- **Input**: Transcript text (string)
- **Output**: Process analysis markdown
- **Validation**: Non-empty string, minimum 100 characters

### BPMNGenerator

- **Location**: [src/components/generation/bpmn_generator.py](src/components/generation/bpmn_generator.py)
- **Skill**: `skills/bpmn-generation/SKILL.md`
- **Input**: Process analysis markdown
- **Output**: BPMN 2.0 XML
- **Validation**:
  - Input has required sections (Process Steps, Actors, Decision Points)
  - Output is valid BPMN XML with start/end events
- **Special**: Loads APQC activities reference as cached context

### RecommendationEngine

- **Location**: [src/components/optimization/recommendation_engine.py](src/components/optimization/recommendation_engine.py)
- **Skill**: `skills/process-optimization/SKILL.md`
- **Input**: Process analysis markdown
- **Output**: Optimization recommendations markdown
- **Validation**: Input has Process Steps and Pain Points sections
- **Special**: Uses Claude Opus 4.5 by default for better reasoning

## Key Design Decisions

### 1. Keep SKILL.md Files Separate from Code

**Decision**: Skills remain as markdown files in `skills/` directory, loaded by components.

**Rationale**:
- Prompts are "configuration" not "code"
- Non-developers can update prompts without touching Python
- Git history shows prompt changes clearly
- Same SKILL.md can be used across different interfaces (CLI, API, Teams bot)

### 2. Use Abstract Base Classes

**Decision**: Use ABC with `@abstractmethod` decorators for component interface.

**Rationale**:
- Enforces all components implement required methods
- Enables IDE autocomplete and type checking
- Serves as documentation of the interface
- Makes it easy to add new components following the same pattern

### 3. Sequential Pipeline (Not DAG)

**Decision**: Simple sequential pipeline where output of step N feeds into step N+1.

**Rationale**:
- Current use case is linear: transcript → analysis → BPMN → recommendations
- Simpler to understand and debug
- Covers 95% of use cases
- Can add DAG support later if needed (YAGNI principle)

### 4. Separate Result from Metadata

**Decision**: `ComponentResult` contains both `data` (output) and `metadata` (execution info).

**Rationale**:
- Observability: Track tokens, timing, errors separately from output
- Debugging: Inspect execution metadata without parsing output
- Metrics: Aggregate metadata across pipeline executions
- Error handling: Success/failure status separate from output data

### 5. Use Opus for Optimization

**Decision**: Default to Claude Opus 4.5 for `RecommendationEngine`.

**Rationale**:
- Optimization requires deep analysis, ROI calculations, technology recommendations
- Opus provides better reasoning for complex business recommendations
- Worth the cost for final output quality
- Configurable - can override to use Sonnet if needed

### 6. Lazy Client Initialization

**Decision**: Anthropic client is created only when needed.

**Rationale**:
- Reduces memory overhead
- Allows components to be instantiated without API keys (useful for testing)
- Enables mocking in tests

### 7. Stop on Error by Default

**Decision**: Pipeline stops on first component failure (configurable).

**Rationale**:
- Safer for production - don't waste tokens on bad data
- Easier debugging - clear failure point
- Can enable continue-on-error mode for testing if needed

## Data Flow

### Full Pipeline Flow

```
1. Input: Transcript Text
   ↓
2. TranscriptProcessor.process(transcript)
   → ComponentResult(success=True, data=analysis_markdown)
   ↓
3. BPMNGenerator.process(analysis_markdown)
   → ComponentResult(success=True, data=bpmn_xml)
   ↓
4. RecommendationEngine.process(analysis_markdown)
   → ComponentResult(success=True, data=recommendations_markdown)
   ↓
5. Output: PipelineResult(
       outputs={
           "Transcript Analysis": analysis_markdown,
           "BPMN Generation": bpmn_xml,
           "Process Optimization": recommendations_markdown
       }
   )
```

## Error Handling

### Component-Level Error Handling

Components catch and handle errors gracefully:

```python
try:
    # Validate input
    self.validate_input(input_data)

    # Process
    result = self._call_claude(...)

    # Return success
    return ComponentResult(success=True, data=result)

except ValueError as e:
    return ComponentResult(success=False, error=f"Validation error: {e}")
except Exception as e:
    return ComponentResult(success=False, error=f"Processing error: {e}")
```

### Pipeline-Level Error Handling

Pipeline tracks all errors and decides whether to continue:

```python
if not result.success:
    errors.append(f"{component_name} failed: {result.error}")
    if stop_on_error:
        break  # Stop pipeline
    else:
        current_input = None  # Continue with None
```

## Testing Strategy

### Test Pyramid

- **Unit Tests** (60%): Test components in isolation with mocked API calls
- **Integration Tests** (30%): Test pipelines with real API calls
- **End-to-End Tests** (10%): Test full workflows with sample data

### Test Files

- [tests/test_pipeline_integration.py](tests/test_pipeline_integration.py) - Integration tests
- `tests/legacy/test_bpmn_generation.py` - Legacy test (for reference)
- `tests/legacy/test_process_optimization.py` - Legacy test (for reference)

## Future Enhancements

### Short-term
- Async execution using `asyncio` for parallel component execution
- Retry logic with exponential backoff for API failures
- Caching component outputs
- Streaming component outputs
- Prometheus metrics for observability

### Medium-term
- FastAPI wrapper for REST API access
- Microsoft Teams bot integration
- Voice walkthrough (ElevenLabs integration)
- Process library database for benchmarking
- Plugin system for user-defined components

### Long-term
- Multi-modal input (video/audio transcripts, images)
- Interactive refinement (chat-based)
- Process simulation ("what-if" scenarios)
- Continuous improvement tracking
- Integration marketplace (SAP, Workday, ServiceNow)

## Migration from Legacy Code

The codebase was refactored from a prototype to production architecture:

### Before (Prototype)
- SKILL.md files + test scripts
- Direct Anthropic API calls in test files
- No abstraction layer
- Manual file loading and saving

### After (Production)
- Component-based architecture
- Pipeline orchestration
- Standardized interfaces
- Modular, reusable code
- Comprehensive error handling

### Migration Path

1. Legacy tests moved to `tests/legacy/`
2. New integration tests in `tests/`
3. README updated with new usage examples
4. ARCHITECTURE.md documents design decisions

## Usage Examples

### Using Individual Components

```python
from src.components.input.transcript_processor import TranscriptProcessor

# Create component
processor = TranscriptProcessor(api_key="your-key")

# Process transcript
result = processor.process(transcript_text)

if result.success:
    print(result.data)  # Analysis markdown
    print(result.metadata)  # Token usage, etc.
```

### Using Pipelines

```python
from src.main import create_full_pipeline

# Create pipeline
pipeline = create_full_pipeline(api_key="your-key")

# Execute
result = pipeline.execute(transcript_text)

# Save outputs
result.save_outputs("outputs/my-analysis")
```

### Command-line Usage

```bash
python -m src.main data/sample-transcripts/ap-process.txt outputs/test
```

## References

- [README.md](README.md) - Project overview and getting started
- [Implementation Plan](C:\Users\pferg\.claude\plans\ethereal-munching-cook.md) - Detailed refactoring plan
