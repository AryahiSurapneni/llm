from googletrans import Translator

translator = Translator()

def translate_to_german(text):
    try:
        translation = translator.translate(text, src='en', dest='de')
        return translation.text
    except Exception as e:
        return f"Translation failed: {str(e)}"

if __name__ == "__main__":
    print(translate_to_german("Good Morning"))