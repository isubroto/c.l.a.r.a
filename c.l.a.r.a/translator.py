from deep_translator import GoogleTranslator
from sayAndListen import SayAndListen

class GoogleTranslator:
    def __init__(self):
        """Initialize the translator with speech interface."""
        self.speech = SayAndListen()
        self.supported_languages = {
            'english': 'en',
            'spanish': 'es',
            'french': 'fr',
            'german': 'de',
            'italian': 'it',
            'portuguese': 'pt',
            'russian': 'ru',
            'japanese': 'ja',
            'korean': 'ko',
            'chinese': 'zh',
            'arabic': 'ar',
            'hindi': 'hi',
            'bengali': 'bn',
            'tamil': 'ta',
            'telugu': 'te',
            'kannada': 'kn',
            'malayalam': 'ml',
            'marathi': 'mr',
            'gujarati': 'gu',
            'punjabi': 'pa'
        }
    
    def translate_text(self, text, target_lang='en', source_lang=None):
        """Translate text to target language."""
        try:
            if source_lang:
                translator = GoogleTranslator(source=source_lang, target=target_lang)
            else:
                translator = GoogleTranslator(target=target_lang)
            
            translated = translator.translate(text)
            return translated
        except Exception as e:
            return f"Translation error: {str(e)}"
    
    def detect_language(self, text):
        """Detect the language of the given text."""
        try:
            translator = GoogleTranslator()
            detected = translator.detect(text)
            return detected
        except Exception as e:
            return f"Language detection error: {str(e)}"
    
    def list_languages(self):
        """Return list of supported languages."""
        return list(self.supported_languages.keys())
    
    def process_translator_command(self, command):
        """Process translation related commands."""
        command = command.lower()
        
        if "translate" in command:
            try:
                # Extract text and target language from command
                parts = command.split("translate")
                if len(parts) != 2:
                    return "Please specify what to translate and to which language."
                
                text_part = parts[1].strip()
                if "to" not in text_part:
                    return "Please specify the target language using 'to'."
                
                text, target_lang = text_part.split("to")
                text = text.strip()
                target_lang = target_lang.strip()
                
                # Get language code
                target_code = self.supported_languages.get(target_lang.lower())
                if not target_code:
                    return f"Sorry, I don't support {target_lang}. Supported languages are: {', '.join(self.list_languages())}"
                
                # Translate
                translated = self.translate_text(text, target_code)
                return f"Translation: {translated}"
                
            except Exception as e:
                return f"Error in translation: {str(e)}"
                
        elif "detect language" in command:
            try:
                text = command.split("detect language")[1].strip()
                detected = self.detect_language(text)
                return f"Detected language: {detected}"
            except Exception as e:
                return f"Error in language detection: {str(e)}"
                
        elif "list languages" in command:
            return f"Supported languages: {', '.join(self.list_languages())}"
            
        return "I can help you translate text. Just say 'translate [text] to [language]' or 'detect language [text]'." 