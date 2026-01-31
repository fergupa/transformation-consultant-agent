# Transformation Consultant Agent

An AI-powered business process transformation consultant that analyzes financial process transcripts, generates BPMN diagrams, and provides automation recommendations.

## Features

- **Transcript Analysis**: Extracts key process information from call transcripts
- **BPMN Diagram Generation**: Creates visual process flows using BPMN standard
- **Process Optimization**: Identifies automation opportunities and best practices
- **Voice Walkthroughs**: Generates audio explanations via ElevenLabs (future)
- **Teams Integration**: Deploy as Microsoft Teams bot (future)

## Project Structure

```
transformation-consultant-agent/
├── src/                            # Production Python code (REFACTORED)
│   ├── main.py                     # Main orchestrator with pipeline functions
│   ├── pipeline.py                 # Pipeline manager
│   ├── interfaces/
│   │   └── component.py            # BaseComponent interface
│   ├── components/
│   │   ├── input/
│   │   │   └── transcript_processor.py
│   │   ├── generation/
│   │   │   └── bpmn_generator.py
│   │   └── optimization/
│   │       └── recommendation_engine.py
│   └── skills/
│       └── skill_manager.py        # SKILL.md file loader
├── skills/                          # Claude skills (SKILL.md prompts)
│   ├── transcript-analysis/         # Extract process info from transcripts
│   ├── process-optimization/        # Identify improvements & automation
│   ├── bpmn-generation/            # Generate BPMN diagrams
│   └── voice-walkthrough/          # Create audio explanations
├── tests/                          # Unit and integration tests
│   ├── test_pipeline_integration.py # Component & pipeline tests
│   └── legacy/                     # Legacy test scripts
├── notebooks/                       # Jupyter notebooks for prototyping
├── config/                         # Configuration files
├── outputs/                        # Generated artifacts
├── data/                           # Sample transcripts and test data
├── ARCHITECTURE.md                 # Architecture documentation
└── requirements.txt                # Python dependencies
```

## Getting Started

### 1. Set up environment

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API keys

```bash
# Copy the example env file
cp config/.env.example config/.env

# Edit config/.env and add your API keys
# - ANTHROPIC_API_KEY
# - ELEVENLABS_API_KEY (for voice, later)
```

### 3. Start prototyping

```bash
# Launch Jupyter
jupyter notebook

# Open notebooks/01-transcript-analysis-prototype.ipynb
```

## Development Phases

### Phase 1: Core Pipeline (COMPLETE)
- [x] Create transcript analysis skill
- [x] Integrate BPMN generation skill
- [x] Create process optimization skill
- [x] Refactor to modular component architecture
- [x] Create pipeline orchestration system
- [x] Add integration tests

### Phase 2: Teams Integration
- [ ] Build Teams bot using Bot Framework
- [ ] Handle file uploads (transcripts)
- [ ] Display BPMN diagrams via Adaptive Cards
- [ ] Deploy to Azure Bot Service

### Phase 3: Voice Integration
- [ ] Create voice walkthrough skill
- [ ] Integrate ElevenLabs API
- [ ] Generate audio explanations
- [ ] Deliver via Teams

## Usage Examples

### Option 1: Using the Full Pipeline (Recommended)

```python
from src.main import run_full_transformation

# Run full transformation from transcript to recommendations
result = run_full_transformation(
    transcript_path="data/sample-transcripts/ap-process.txt",
    output_dir="outputs/my-analysis"
)

if result.success:
    print("Analysis complete!")
    print(f"Analysis: {result.outputs['Transcript Analysis'][:100]}...")
    print(f"BPMN saved to outputs/my-analysis/bpmn-generation.bpmn")
    print(f"Recommendations saved to outputs/my-analysis/process-optimization-recommendations.md")
```

### Option 2: Using Individual Components

```python
from src.components.input.transcript_processor import TranscriptProcessor
from src.components.generation.bpmn_generator import BPMNGenerator
from src.components.optimization.recommendation_engine import RecommendationEngine

# Create components
processor = TranscriptProcessor(api_key="your-key")
bpmn_gen = BPMNGenerator(api_key="your-key")
recommender = RecommendationEngine(api_key="your-key")

# Process transcript
transcript = open("data/sample-transcripts/ap-process.txt").read()
analysis_result = processor.process(transcript)

# Generate BPMN
bpmn_result = bpmn_gen.process(analysis_result.data)

# Get recommendations
recs_result = recommender.process(analysis_result.data)

print(bpmn_result.data)  # BPMN XML
```

### Option 3: Using Custom Pipelines

```python
from src.main import create_analysis_pipeline, create_full_pipeline, create_bpmn_pipeline

# Analysis only
pipeline = create_analysis_pipeline(api_key="your-key")
result = pipeline.execute(transcript_text)

# BPMN generation from existing analysis
pipeline = create_bpmn_pipeline(api_key="your-key")
result = pipeline.execute(analysis_markdown)

# Full pipeline with custom business context
pipeline = create_full_pipeline(api_key="your-key")
pipeline.component_configs[2]['business_context'] = "Industry: Healthcare, Budget: $500K"
result = pipeline.execute(transcript_text)
result.save_outputs("outputs/results")
```

### Command-line Usage

```bash
# Run full transformation
python -m src.main data/sample-transcripts/ap-process.txt outputs/test

# Run integration tests
pytest tests/test_pipeline_integration.py -v

# Run all tests
pytest tests/ -v
```

## Architecture

The system uses a modular component-based architecture. See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed design documentation.

**Key Components**:
- **TranscriptProcessor**: Analyzes transcripts and extracts process information
- **BPMNGenerator**: Creates BPMN 2.0 XML diagrams from analysis
- **RecommendationEngine**: Generates optimization recommendations (uses Opus 4.5)
- **Pipeline**: Orchestrates sequential execution of components

## Contributing

This is a personal project. Feedback and suggestions welcome!

## License

MIT
