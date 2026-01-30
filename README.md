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
├── skills/                          # Claude skills for specific tasks
│   ├── transcript-analysis/         # Extract process info from transcripts
│   ├── process-optimization/        # Identify improvements & automation
│   ├── bpmn-generation/            # Generate BPMN diagrams
│   └── voice-walkthrough/          # Create audio explanations
├── notebooks/                       # Jupyter notebooks for prototyping
├── src/                            # Production Python code
│   ├── agent.py                    # Main agent orchestration
│   └── utils/                      # Helper functions
├── tests/                          # Unit and integration tests
├── config/                         # Configuration files
├── outputs/                        # Generated artifacts
├── data/                           # Sample transcripts and test data
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

### Phase 1: Core Pipeline (Current)
- [x] Create transcript analysis skill
- [x] Integrate BPMN generation skill
- [x] Create process optimization skill
- [ ] Test end-to-end pipeline in Jupyter

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

## Usage Example

```python
from anthropic import Anthropic
from pathlib import Path

client = Anthropic(api_key="your-key")

# Load transcript
transcript = Path("data/sample-transcripts/ap-process.txt").read_text()

# Analyze transcript
analysis = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=Path("skills/transcript-analysis/SKILL.md").read_text(),
    messages=[{"role": "user", "content": transcript}]
)

# Generate BPMN
bpmn = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=Path("skills/bpmn-generation/SKILL.md").read_text(),
    messages=[{"role": "user", "content": analysis.content[0].text}]
)

# Get recommendations
recommendations = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=Path("skills/process-optimization/SKILL.md").read_text(),
    messages=[{"role": "user", "content": f"{analysis.content[0].text}\n\n{bpmn.content[0].text}"}]
)
```

## Contributing

This is a personal project. Feedback and suggestions welcome!

## License

MIT
