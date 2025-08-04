import requests
from calculator_tool import calculate

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "llama3-70b-8192"

def is_math_question(user_prompt):
    math_keywords = ["add", "plus", "sum", "subtract", "minus", "multiply", "times", "divide", "+", "-", "*", "/"]
    return any(keyword in user_prompt.lower() for keyword in math_keywords)

def ask_llm(user_prompt):
    system_prompt = (
        "You are a smart assistant. Always answer step-by-step. "
        "If the question is a math problem, say: 'Let me use the calculator tool.'"
    )

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def main():
    print("Smart Assistant (Level 2: LLM + Calculator Tool)")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            if is_math_question(user_input):
                print("Assistant: Let me use the calculator tool.")
                result = calculate(user_input)
                print(f"Calculator Tool: {result}")
            else:
                response = ask_llm(user_input)
                print(f"Assistant:\n{response}")
        except KeyboardInterrupt:
            print("\nSession ended.")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

if __name__ == "__main__":
    main()
