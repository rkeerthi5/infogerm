from googletrans import Translator

# Initialize translator object
translator = Translator()

def translate_text(text, dest_language):
    # Translate the input text to the destination language
    try:
        translation = translator.translate(text, dest=dest_language)
        return f"Translated Text: {translation.text}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Take user input
    text = input("Enter text to translate: ")
    dest_language = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    # Call the translation function and display the result
    translated_text = translate_text(text, dest_language)
    print(translated_text)
