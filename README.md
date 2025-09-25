# LangChain LLM Prompt Tool

A lightweight command-line application for sending prompts and parameters to Google's Gemini models using LangChain. Streamline your LLM interactions with configurable parameters and template substitution.

## Usage

Run the tool from any directory:

```bash
# Send a simple prompt
llm-prompt "Explain quantum computing"

# Use with parameters
llm-prompt "Write a story about {topic}" --topic "space exploration" --max-tokens 500

# Set temperature and other model parameters
llm-prompt "Generate creative ideas for {theme}" --theme "sustainable living" --temperature 0.9

# Configure output
llm-prompt "Summarise this concept: {concept}" --concept "machine learning" --max-tokens 200
```

## Tech Stack

### Dependencies

- **Python 3.8+** - Core runtime
- **langchain** - LLM orchestration framework
- **google-generativeai** - Google Gemini API client
- **click** - Command-line interface creation
- **pydantic** - Data validation and settings management
- **python-dotenv** - Environment variable management
- **jinja2** - Template rendering for parameterised prompts

### Development Dependencies

- **pytest** - Testing framework
- **black** - Code formatting
- **flake8** - Linting
- **mypy** - Type checking

## Configuration

Create a `.env` file in your project root:

```env
GOOGLE_API_KEY=your_api_key_here
DEFAULT_MODEL=gemini-1.5-pro
DEFAULT_MAX_TOKENS=1000
DEFAULT_TEMPERATURE=0.7
```

## Installation

### Option 1: Using uv (recommended)
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and set up project
uv init langchain-llm-prompt-tool
cd langchain-llm-prompt-tool
uv add langchain google-generativeai click pydantic python-dotenv jinja2

# Install in development mode
uv add --dev pytest black flake8 mypy
```

### Option 2: Using pip
```bash
# Clone the repository
git clone https://github.com/yourusername/langchain-llm-prompt-tool.git
cd langchain-llm-prompt-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Examples

### Basic Prompt
```bash
llm-prompt "What are the benefits of renewable energy?"
```

### Parameterised Template
```bash
llm-prompt "Act as a {role} and explain {concept} to a {audience}" \
  --role "data scientist" \
  --concept "neural networks" \
  --audience "business stakeholder"
```

### With Model Parameters
```bash
llm-prompt "Write a creative short story about {theme}" \
  --theme "time travel" \
  --temperature 0.9 \
  --max-tokens 800
```
