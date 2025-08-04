# Agentic Smart Assistant CLI

A command-line assistant powered by the Groq API, utilizing the Llama3-70B model. This assistant is designed to perform multi-step reasoning, respond clearly to user questions, handle basic arithmetic, translate English to German, and log all interactions for review. It supports three levels of capability: LLM-only, LLM with calculator tool, and full agentic reasoning with memory.

## Features

- **Step-by-Step Responses**: Delivers structured, easy-to-follow answers for complex or factual questions.
- **Groq API Integration**: Leverages the high-speed inference capabilities of the Groq Llama3-70B model.
- **Greeting Handler**: Provides custom responses to greetings like "hi" or "hello".
- **Calculator Tool Integration**: Handles basic math operations like addition and multiplication.
- **Translation Tool**: Translates English phrases into German.
- **Agentic Multi-Step Reasoning**: Breaks down complex user queries and processes them sequentially.
- **Interaction Logging**: Automatically saves the full conversation history to `interaction_logs.json` upon exit.

## Requirements

- Python 3.8+
- requests Python package
- googletrans==4.0.0-rc1 package

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AryahiSurapneni/llm.git
   cd llm
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate         # For Windows
   source .venv/bin/activate        # For macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install requests
   pip install googletrans==4.0.0-rc1
   ```

4. **Set up your API Key:**
   Open the Python files (`chatbot.py`, `chatbot_with_tool.py`, `full_agent.py`, and `translator_tool.py`) and replace `"YOUR_GROQ_API_KEY_HERE"` with your actual Groq API key:
   ```python
   GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"
   ```

## Usage

Run the assistant at your desired level from the terminal:

### Level 1 – LLM-Only Smart Assistant
```bash
python chatbot.py
```

### Level 2 – LLM + Calculator Tool
```bash
python chatbot_with_tool.py
```

### Level 3 – Agentic AI with Multi-Tool Reasoning
```bash
python full_agent.py
```

You will be greeted with a prompt. Type your question and press Enter.

```
Agentic Smart Assistant
Type your question or 'exit' to quit

You:
```

To end the session, simply type `exit`. The full interaction will be saved to `interaction_logs.json`.

### Example Interaction (Level 3)

```
Agentic Smart Assistant
Type your question or 'exit' to quit

You: Translate 'Good Morning' into German and then multiply 5 and 6.
Agent:
Translation to German: 'Good Morning' → 'Guten Morgen'
Multiplication Result: 5 * 6 = 30

You: What is the distance between Earth and Mars?
Agent:
LLM Response: The average distance between Earth and Mars is about 225 million kilometers...

You: exit
Session ended. Logs saved to interaction_logs.json
```

## File Structure

```
.
├── chatbot.py                 # Level 1 assistant (LLM only)
├── chatbot_with_tool.py       # Level 2 assistant (LLM + calculator)
├── full_agent.py              # Level 3 assistant (multi-step agentic reasoning)
├── calculator_tool.py         # Local tool for addition and multiplication
├── translator_tool.py         # Translation to German using Groq LLM
├── interaction_logs.json      # Auto-generated file to log conversations
└── README.md                  # This README file
```
