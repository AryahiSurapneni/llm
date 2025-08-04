# Agentic Smart Assistant CLI

A multi-level command-line assistant powered by the Groq API, utilizing the Llama3-70B model. This assistant provides structured, step-by-step answers, performs basic arithmetic, translates text to German, and logs all interactions for review. It progresses through three levels: LLM-only, LLM + calculator tool, and full agentic multi-tasking.

## Features

- Step-by-Step Reasoning: Responds to queries with logically structured, clear explanations.
- Groq API Integration: Uses Groq-hosted LLaMA3-70B model for fast, accurate inference.
- Modular Tools: Integrates a calculator and translation tool to handle specific task types.
- Agentic Multi-Step Reasoning: Decomposes multi-part instructions and remembers sub-task results.
- Interaction Logging: Automatically saves conversation history to `interaction_logs.json` upon exit.

## Requirements

- Python 3.8+
- `requests` Python package
- `googletrans==4.0.0-rc1` (used in Level 3 for translation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AryahiSurapneni/llm.git
   cd llm  
2.  Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate         # For Windows
   source .venv/bin/activate      # For macOS/Linux


   
