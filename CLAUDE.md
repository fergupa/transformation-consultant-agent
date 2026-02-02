# CLAUDE.md - AI Assistant Guide

This document provides essential information for AI assistants working with the Transformation Consultant Agent codebase.

## Project Overview

**Purpose**: An AI-powered business process transformation consultant that analyzes financial process transcripts, generates BPMN diagrams, and provides automation recommendations.

**Tech Stack**: Python 3.9+, Anthropic Claude API, BPMN 2.0 XML

**Current Phase**: Phase 1 (Core Pipeline) is complete. Phases 2 (Teams Integration) and 3 (Voice Integration) are planned.

## Project Structure

```
transformation-consultant-agent/
├── src/                           # Production Python code
│   ├── main.py                    # Main orchestrator with pipeline factory functions
│   ├── pipeline.py                # Pipeline manager and execution engine
│   ├── interfaces/
│   │   └── component.py           # BaseComponent interface & ComponentResult dataclass
│   ├── components/
│   │   ├── input/
│   │   │   └── transcript_processor.py  # Transcript analysis component
│   │   ├── generation/
│   │   │   └── bpmn_generator.py        # BPMN XML generation component
│   │   └── optimization/
│   │       └── recommendation_engine.py # Process recommendations (uses Opus)
│   └── skills/
│       └── skill_manager.py       # SKILL.md file loader with caching
├── skills/                        # Claude skill prompts (SKILL.md files)
│   ├── transcript-analysis/       # Extract process info from transcripts
│   ├── bpmn-generation/           # Generate BPMN 2.0 XML diagrams
│   └── process-optimization/      # Generate optimization recommendations
├── tests/
│   ├── test_pipeline_integration.py  # Main integration tests
│   └── legacy/                       # Legacy test scripts (reference only)
├── data/sample-transcripts/       # Sample input data
├── notebooks/                     # Jupyter notebooks for prototyping
├── config/                        # Configuration (.env files)
├── outputs/                       # Generated artifacts
├── ARCHITECTURE.md                # Detailed architecture documentation
├── SETUP.md                       # Development setup guide
└── requirements.txt               # Python dependencies
```

## Key Files Reference

| File | Purpose |
|------|---------|
| `src/main.py` | Entry point with `run_full_transformation()` and pipeline factories |
| `src/pipeline.py` | `Pipeline` class orchestrating component execution |
| `src/interfaces/component.py` | `BaseComponent` ABC and `ComponentResult` dataclass |
| `skills/*/SKILL.md` | System prompts for Claude (separated from code) |
| `config/.env` | API keys (ANTHROPIC_API_KEY required) |

## Architecture Patterns

### Component-Based Design

All processing components inherit from `BaseComponent` and must implement:

```python
class MyComponent(BaseComponent):
    @property
    def component_name(self) -> str:
        return "Component Name"

    @property
    def skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent.parent / "skills" / "skill-name" / "SKILL.md"

    def validate_input(self, input_data: Any) -> bool:
        # Raise ValueError if invalid
        pass

    def process(self, input_data: Any, **kwargs) -> ComponentResult:
        # Return ComponentResult with success/data/metadata/error
        pass
```

### Pipeline Flow

```
Transcript Text → TranscriptProcessor → Analysis Markdown
                                              ↓
                  BPMNGenerator ← ─ ─ ─ ─ ─ ─ ┤
                       ↓                      ↓
                  BPMN XML         RecommendationEngine
                                              ↓
                                  Recommendations Markdown
```

### Key Design Decisions

1. **SKILL.md files separate from code** - Prompts are "configuration", editable without touching Python
2. **Sequential pipeline** - Output of component N feeds into component N+1
3. **Opus for optimization** - `RecommendationEngine` uses Claude Opus 4.5 for complex reasoning
4. **Lazy client initialization** - Anthropic client created only when needed
5. **Stop on error by default** - Pipeline halts on first component failure

## Development Commands

```bash
# Setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp config/.env.example config/.env  # Add ANTHROPIC_API_KEY

# Run full transformation
python -m src.main data/sample-transcripts/ap-process.txt outputs/test

# Run tests
pytest tests/test_pipeline_integration.py -v  # Integration tests
pytest tests/ -v                              # All tests

# Verify setup
python test_setup.py

# Jupyter prototyping
jupyter notebook
```

## Coding Conventions

### Naming

- **Classes**: PascalCase (`TranscriptProcessor`, `BPMNGenerator`)
- **Methods/Functions**: snake_case (`validate_input`, `_call_claude`)
- **Skill directories**: kebab-case (`transcript-analysis`, `bpmn-generation`)
- **Output files**: kebab-case with extensions (`.bpmn`, `-analysis.md`, `-recommendations.md`)

### Code Style

- Use `black` for formatting
- Use `flake8` for linting
- Type hints are encouraged
- Dataclasses for structured data (`ComponentResult`, `PipelineResult`)
- Abstract base classes with `@abstractmethod` for interfaces

### Error Handling

Components should catch errors and return `ComponentResult` with `success=False`:

```python
try:
    self.validate_input(input_data)
    result = self._call_claude(...)
    return ComponentResult(success=True, data=result, metadata={...})
except ValueError as e:
    return ComponentResult(success=False, error=f"Validation error: {e}")
except Exception as e:
    return ComponentResult(success=False, error=f"Processing error: {e}")
```

## API Models Used

| Component | Default Model | Rationale |
|-----------|---------------|-----------|
| TranscriptProcessor | claude-sonnet-4-5-20250929 | Balance of speed and quality |
| BPMNGenerator | claude-sonnet-4-5-20250929 | Structured output generation |
| RecommendationEngine | claude-opus-4-5-20251101 | Complex business reasoning |

Models are configurable via constructor parameter.

## Testing Guidelines

- Integration tests in `tests/test_pipeline_integration.py`
- Use fixtures for `api_key`, `sample_transcript`, `sample_analysis`
- Tests require valid `ANTHROPIC_API_KEY` in environment
- Legacy tests in `tests/legacy/` are for reference only

## Common Tasks

### Adding a New Component

1. Create class in `src/components/<category>/` inheriting from `BaseComponent`
2. Create corresponding skill in `skills/<skill-name>/SKILL.md`
3. Implement required properties and methods
4. Add to pipeline factory in `src/main.py`
5. Add integration tests

### Modifying a Skill Prompt

1. Edit the `SKILL.md` file directly in `skills/<skill-name>/`
2. Test with existing integration tests
3. No code changes needed (prompts are loaded at runtime)

### Running a Custom Pipeline

```python
from src.main import create_analysis_pipeline, create_bpmn_pipeline, create_full_pipeline

# Analysis only
pipeline = create_analysis_pipeline(api_key="...")
result = pipeline.execute(transcript_text)

# Full transformation
pipeline = create_full_pipeline(api_key="...")
result = pipeline.execute(transcript_text)
result.save_outputs("outputs/")
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude API key |
| `ELEVENLABS_API_KEY` | No | For voice integration (Phase 3) |

Set in `config/.env` or export directly.

## Important Caveats

1. **BPMN output validation**: Generator validates XML has proper start/end events and BPMN namespace
2. **Input validation**: Components validate input before processing (min 100 chars for transcripts)
3. **Caching**: `SkillManager` caches loaded prompts; restart to pick up SKILL.md changes in long-running processes
4. **Token usage**: Metadata includes token counts; monitor for cost management
5. **Output directory**: `run_full_transformation()` creates directory if it doesn't exist

## Documentation Reference

- **README.md** - Project overview and quick start
- **ARCHITECTURE.md** - Detailed design decisions and diagrams
- **SETUP.md** - Step-by-step environment setup
- **skills/*/README.md** - Individual skill documentation
