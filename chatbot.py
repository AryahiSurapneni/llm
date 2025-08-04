import requests

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "llama3-70b-8192"  # You can also try mixtral-8x7b-32768 or gemma-7b-it

def ask_llm(user_prompt):
    system_prompt = (
        "You are a smart assistant. Always respond step-by-step. "
        "Do not answer math questions. If asked a math problem, respond with: "
        "'I can't solve math problems directly. Please use a calculator tool.'"
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
    result = response.json()
    return result["choices"][0]["message"]["content"].strip()

def main():
    print("Welcome to the Smart Assistant (Level 1) - Groq API Version")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            answer = ask_llm(user_input)
            print(f"Assistant:\n{answer}")
        except KeyboardInterrupt:
            print("\nSession terminated.")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

if __name__ == "__main__":
    main()
