# Deep Research Agent

A sophisticated terminal-based Deep Research Agent built with OpenAI AI Agents SDK, powered by Google's Gemini API and enhanced with Rich CLI formatting. This agent performs thorough research by analyzing queries, browsing the web, and synthesizing insights into clear, well-structured reports.  

## Project Overview

The Deep Research Agent is an advanced AI-powered research tool that:
- Breaks down complex research queries into focused search topics
- Performs intelligent web searches using DuckDuckGo
- Analyzes and summarizes search results
- Makes decisions about follow-up research needs
- Synthesizes findings into comprehensive markdown reports
- Presents all information with a beautiful terminal interface

## Installation

### Prerequisites

- Python 3.7 or higher
- UV package manager (install from https://github.com/astral/uv)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/DevHammad0/Deep_Research_Agent.git
cd deep_research_agent
```

2. Install dependencies using UV:
```bash
uv pip install -r requirements.txt
```

3. Set up your Gemini API key:
```bash
# On Windows (PowerShell):
Copy `.env.example` to `.env` and fill in your values:  
- `GEMINI_API_KEY`: Your Google Gemini API key

```

### Project Structure

```
DEEP_RESEARCH_AGENT/
├── src/
│   └── deep_research_agent/
│       ├── research_agents/  # Specialized agent implementations
│       │   ├── follow_up_agent.py  # Research completion decisions
│       │   ├── query_agents.py  # Query analysis and generation
│       │   ├── search_agent.py  # Web content analysis
│       │   └── synthesis_agent.py  # Report generation
│       ├── coordinator.py  # Research workflow orchestrator
│       ├── main.py  # Entry point
│       ├── model_setup.py  # GEMINI model configurations
│       └── models.py  # Data models and types
├── README.md  # Project documentation
├── requirements.txt  # Project dependencies
├── pyproject.toml

```

## Core Components

### 1. Research Coordinator (`coordinator.py`)
The central orchestrator that:
- Manages the research workflow
- Coordinates between different specialized agents
- Handles web searches using DuckDuckGo
- Controls the research iteration process
- Manages the final report synthesis

### 2. Specialized Agents

#### Query Agent (`research_agents/query_agents.py`)
- Analyzes the initial research query
- Breaks down complex topics into searchable components
- Generates focused search queries
- Provides reasoning for the query strategy

#### Search Agent (`research_agents/search_agent.py`)
- Processes search results
- Scrapes and analyzes web content
- Generates concise summaries of findings
- Filters out irrelevant information

#### Follow-up Agent (`research_agents/follow_up_agent.py`)
- Evaluates research completeness
- Decides if more research is needed
- Generates follow-up queries for gaps in knowledge
- Provides reasoning for decisions

#### Synthesis Agent (`research_agents/synthesis_agent.py`)
- Combines all research findings
- Creates structured markdown reports
- Includes source citations
- Generates table of contents

## How It Works

1. **Query Analysis**
   - User inputs a research query
   - Query Agent breaks it down into focused search queries
   - System displays the analysis and generated queries

2. **Research Process**
   - Performs DuckDuckGo searches for each query
   - Search Agent analyzes and summarizes each result
   - Progress is displayed in real-time with Rich formatting

3. **Iterative Research**
   - Follow-up Agent evaluates findings
   - Decides if more research is needed
   - Generates additional queries if necessary
   - Maximum of 3 research iterations

4. **Report Generation**
   - Synthesis Agent combines all findings
   - Creates a structured markdown report
   - Includes citations and sources
   - Presents the final report with Rich formatting

## Usage

Run the agent from the terminal:
```bash
python -m src.deep_research_agent.main
```

Example interaction:
```
> Welcome to the Deep Research Agent!
> What would you like to research? Impact of quantum computing on cryptography

[Query Analysis]
Generated Search Queries:
1. Current state quantum computing cryptography impact
2. Post-quantum cryptography methods developments
3. Quantum computing threats traditional encryption

[Searching...]
✓ Found 3 sources across 3 queries

[Analyzing findings...]
✓ Research complete!

[Final Report]
# Impact of Quantum Computing on Cryptography
...
```

## Rich Integration

The project leverages Rich for enhanced terminal output:

1. **Status Updates**
   - Real-time progress indicators
   - Colored status messages
   - Spinners for ongoing operations

2. **Content Formatting**
   - Markdown rendering for reports
   - Panels for sectioning content
   - Colored output for different types of information
   - Tables for structured data

3. **User Interaction**
   - Styled prompts for user input
   - Error messages with appropriate styling
   - Clear visual hierarchy of information

## Project Structure

```
src/deep_research_agent/
├── main.py                 # Entry point and CLI interface
├── coordinator.py          # Research workflow orchestrator
├── models.py              # Data models and types
├── research_agents/       # Specialized agent implementations
│   ├── query_agents.py    # Query analysis and generation
│   ├── search_agent.py    # Web content analysis
│   ├── follow_up_agent.py # Research completion decisions
│   └── synthesis_agent.py # Report generation
└── model_setup.py        # OpenAI model configurations
```

## Implementation Insights

1. **Modular Agent Design**
   - Each agent has a specific, focused responsibility
   - Clear separation of concerns
   - Easy to extend or modify individual components

2. **Iterative Research Approach**
   - Maximum of 3 research iterations
   - Smart decision-making about when to stop
   - Prevents endless research loops

3. **Error Handling**
   - Robust web scraping with timeouts
   - Graceful handling of failed requests
   - Clear error messaging

4. **Performance Considerations**
   - Text content truncation for large web pages
   - Concurrent processing where possible
   - Efficient text processing with BeautifulSoup

## Dependencies

- `openai-agents`: Core agent functionality
- `rich`: Terminal formatting and UI
- `duckduckgo-search`: Web search capability
- `bs4`: Web content parsing
- `pydantic`: Data validation and modeling
- `requests`: HTTP requests
- `python-dotenv`: Environment management
