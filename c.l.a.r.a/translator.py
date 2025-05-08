from googletrans import Translator
from sayAndListen import SayAndListen

class GoogleTranslator:
    def __init__(self):
        self.speech = SayAndListen()
        self.translator = Translator()
        self.languages = {
            'english': 'en',
            'spanish': 'es',
            'french': 'fr',
            'german': 'de',
            'italian': 'it',
            'portuguese': 'pt',
            'russian': 'ru',
            'japanese': 'ja',
            'korean': 'ko',
            'chinese': 'zh-cn',
            'hindi': 'hi',
            'arabic': 'ar',
            'dutch': 'nl',
            'greek': 'el',
            'hebrew': 'iw',
            'polish': 'pl',
            'turkish': 'tr',
            'vietnamese': 'vi',
            'thai': 'th',
            'swedish': 'sv'
        }
    
    def translate_text(self, text, target_lang, source_lang=None):
        """Translate text to target language"""
        try:
            # Convert language names to codes
            target_code = self.languages.get(target_lang.lower(), target_lang)
            source_code = self.languages.get(source_lang.lower(), source_lang) if source_lang else None
            
            # Translate text
            translation = self.translator.translate(text, dest=target_code, src=source_code)
            
            return f"Translation: {translation.text}"
        except Exception as e:
            return f"Error translating text: {str(e)}"
    
    def detect_language(self, text):
        """Detect language of text"""
        try:
            detection = self.translator.detect(text)
            return f"Detected language: {detection.lang}"
        except Exception as e:
            return f"Error detecting language: {str(e)}"
    
    def list_languages(self):
        """List supported languages"""
        language_list = "Supported languages:\n"
        for name, code in self.languages.items():
            language_list += f"- {name} ({code})\n"
        return language_list
    
    def process_translator_command(self, command):
        """Process translator-related commands"""
        command = command.lower()
        
        if "translate" in command:
            # Extract text and target language
            try:
                # Remove "translate" and split into text and language
                parts = command.replace("translate", "").strip().split(" to ", 1)
                if len(parts) == 2:
                    text, target_lang = parts
                    return self.translate_text(text.strip(), target_lang.strip())
                return "Please specify text and target language"
            except Exception as e:
                return f"Error processing translate command: {str(e)}"
        
        elif "detect language" in command:
            # Extract text
            text = command.replace("detect language", "").strip()
            if text:
                return self.detect_language(text)
            return "Please specify text to detect language"
        
        elif "list languages" in command:
            return self.list_languages()
        
        return "I didn't understand that translator command" 