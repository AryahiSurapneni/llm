import re

def calculate(text):
    try:
        numbers = list(map(int, re.findall(r'\d+', text)))
        if "Add" in text or "plus" in text or "+" in text:
            return f"{numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}"
        elif "subtract" in text or "minus" in text or "-" in text:
            return f"{numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}"
        elif "multiply" in text or "times" in text or "*" in text:
            return f"{numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}"
        elif "divide" in text or "/" in text:
            return f"{numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}"
        else:
            return "Operation not recognized."
    except:
        return "Failed to parse math expression."
