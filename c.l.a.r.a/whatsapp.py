import webbrowser
import pyautogui
import time
from sayAndListen import SayAndListen

class WhatsAppController:
    def __init__(self):
        self.speech = SayAndListen()
        self.whatsapp_web_url = "https://web.whatsapp.com"
        self.is_whatsapp_open = False
    
    def open_whatsapp(self):
        """Open WhatsApp Web"""
        try:
            webbrowser.open(self.whatsapp_web_url)
            self.is_whatsapp_open = True
            time.sleep(5)  # Wait for WhatsApp Web to load
            return "Opening WhatsApp Web"
        except Exception as e:
            return f"Error opening WhatsApp: {str(e)}"
    
    def send_message(self, contact, message):
        """Send a message to a contact"""
        try:
            if not self.is_whatsapp_open:
                self.open_whatsapp()
            
            # Click on search box
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            
            # Type contact name
            pyautogui.write(contact)
            time.sleep(2)
            
            # Press enter to select contact
            pyautogui.press('enter')
            time.sleep(1)
            
            # Type message
            pyautogui.write(message)
            time.sleep(1)
            
            # Send message
            pyautogui.press('enter')
            
            return f"Message sent to {contact}"
        except Exception as e:
            return f"Error sending message: {str(e)}"
    
    def make_call(self, contact):
        """Make a WhatsApp call to a contact"""
        try:
            if not self.is_whatsapp_open:
                self.open_whatsapp()
            
            # Click on search box
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            
            # Type contact name
            pyautogui.write(contact)
            time.sleep(2)
            
            # Press enter to select contact
            pyautogui.press('enter')
            time.sleep(1)
            
            # Click call button (you'll need to adjust coordinates based on your screen)
            # This is a placeholder - you'll need to find the actual coordinates
            pyautogui.click(x=1000, y=100)  # Adjust these coordinates
            
            return f"Calling {contact}"
        except Exception as e:
            return f"Error making call: {str(e)}"
    
    def process_whatsapp_command(self, command):
        """Process WhatsApp-related commands"""
        command = command.lower()
        
        if "open whatsapp" in command:
            return self.open_whatsapp()
        
        elif "send message" in command:
            # Extract contact and message
            try:
                # Remove "send message" and split into contact and message
                parts = command.replace("send message", "").strip().split(" to ", 1)
                if len(parts) == 2:
                    message, contact = parts
                    return self.send_message(contact.strip(), message.strip())
                return "Please specify contact and message"
            except Exception as e:
                return f"Error processing send message command: {str(e)}"
        
        elif "call" in command:
            # Extract contact
            contact = command.replace("call", "").strip()
            if contact:
                return self.make_call(contact)
            return "Please specify who to call"
        
        return "I didn't understand that WhatsApp command" 