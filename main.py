from googletrans import Translator

translator = Translator()

input_text = input("Enter live commentary (English/Hindi): ")

languages = {
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ar": "Arabic",
    "ja": "Japanese",
    "ko": "Korean",
    "ta": "Tamil",
    "te": "Telugu",
    "mr": "Marathi",
    "bn": "Bengali",
    "pt": "Portuguese",
    "ru": "Russian"
}

print("\n--- Translated Output ---")

for code, name in languages.items():
    translated = translator.translate(input_text, dest=code).text
    print(f"{name}: {translated}")
