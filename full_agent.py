import openai
from calculator_tool import add, multiply
from translator_tool import translate_to_german

# Using Groq API Key
openai.api_key = "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"

def detect_tasks(user_input):
    tasks = []
    if "translate" in user_input.lower():
        tasks.append("translate")
    if any(op in user_input.lower() for op in ["add", "plus", "+"]):
        tasks.append("add")
    if any(op in user_input.lower() for op in ["multiply", "times", "*"]):
        tasks.append("multiply")
    if not tasks:
        tasks.append("llm")
    return tasks

def parse_numbers(text, operation):
    import re
    nums = list(map(int, re.findall(r'\d+', text)))
    if operation == "add":
        return nums[0], nums[1]
    elif operation == "multiply":
        return nums[0], nums[1]
    return None, None

def run_agentic_task(user_input):
    tasks = detect_tasks(user_input)
    memory = []

    for task in tasks:
        if task == "add":
            a, b = parse_numbers(user_input, "add")
            result = add(a, b)
            memory.append(f"Addition Result: {a} + {b} = {result}")
        elif task == "multiply":
            a, b = parse_numbers(user_input, "multiply")
            result = multiply(a, b)
            memory.append(f"Multiplication Result: {a} * {b} = {result}")
        elif task == "translate":
            import re
            match = re.search(r"translate '(.*?)'", user_input.lower())
            if match:
                phrase = match.group(1)
                result = translate_to_german(phrase)
                memory.append(f"Translation to German: '{phrase}' → '{result}'")
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            memory.append(f"LLM Response: {response.choices[0].message['content']}")

    return "\n".join(memory)

if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        output = run_agentic_task(query)
        print(f"\nAgent:\n{output}\n")