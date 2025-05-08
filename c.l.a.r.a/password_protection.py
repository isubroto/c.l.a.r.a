import json
import os
import hashlib
import getpass
from sayAndListen import SayAndListen

class PasswordManager:
    def __init__(self):
        self.speech = SayAndListen()
        self.passwords_file = 'passwords.json'
        self.master_password = None
        self.passwords = {}
        self.load_passwords()
    
    def load_passwords(self):
        """Load saved passwords from file"""
        try:
            if os.path.exists(self.passwords_file):
                with open(self.passwords_file, 'r') as f:
                    self.passwords = json.load(f)
        except Exception as e:
            print(f"Error loading passwords: {e}")
            self.passwords = {}
    
    def save_passwords(self):
        """Save passwords to file"""
        try:
            with open(self.passwords_file, 'w') as f:
                json.dump(self.passwords, f, indent=4)
        except Exception as e:
            print(f"Error saving passwords: {e}")
    
    def _hash_password(self, password):
        """Hash a password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def set_master_password(self, password):
        """Set the master password"""
        try:
            self.master_password = self._hash_password(password)
            return "Master password set successfully"
        except Exception as e:
            return f"Error setting master password: {str(e)}"
    
    def verify_master_password(self, password):
        """Verify the master password"""
        try:
            return self._hash_password(password) == self.master_password
        except Exception as e:
            return False
    
    def add_password(self, service, username, password):
        """Add a new password entry"""
        try:
            if service in self.passwords:
                return f"Password for {service} already exists"
            
            self.passwords[service] = {
                'username': username,
                'password': self._hash_password(password)
            }
            self.save_passwords()
            return f"Password for {service} added successfully"
        except Exception as e:
            return f"Error adding password: {str(e)}"
    
    def get_password(self, service):
        """Get a password entry"""
        try:
            if service in self.passwords:
                return f"Username: {self.passwords[service]['username']}\nPassword: {self.passwords[service]['password']}"
            return f"No password found for {service}"
        except Exception as e:
            return f"Error getting password: {str(e)}"
    
    def update_password(self, service, username, password):
        """Update an existing password entry"""
        try:
            if service not in self.passwords:
                return f"No password found for {service}"
            
            self.passwords[service] = {
                'username': username,
                'password': self._hash_password(password)
            }
            self.save_passwords()
            return f"Password for {service} updated successfully"
        except Exception as e:
            return f"Error updating password: {str(e)}"
    
    def delete_password(self, service):
        """Delete a password entry"""
        try:
            if service not in self.passwords:
                return f"No password found for {service}"
            
            del self.passwords[service]
            self.save_passwords()
            return f"Password for {service} deleted successfully"
        except Exception as e:
            return f"Error deleting password: {str(e)}"
    
    def list_services(self):
        """List all services with saved passwords"""
        if not self.passwords:
            return "No passwords saved"
        
        service_list = "Saved passwords for:\n"
        for service in self.passwords:
            service_list += f"- {service}\n"
        return service_list
    
    def process_password_command(self, command):
        """Process password-related commands"""
        command = command.lower()
        
        if "set master password" in command:
            # Get master password securely
            password = getpass.getpass("Enter master password: ")
            return self.set_master_password(password)
        
        elif "add password" in command:
            # Extract service, username, and password
            try:
                # Remove "add password" and split into parts
                parts = command.replace("add password", "").strip().split(" for ", 1)
                if len(parts) == 2:
                    service = parts[1].strip()
                    username = input("Enter username: ")
                    password = getpass.getpass("Enter password: ")
                    return self.add_password(service, username, password)
                return "Please specify service, username, and password"
            except Exception as e:
                return f"Error processing add password command: {str(e)}"
        
        elif "get password" in command:
            # Extract service
            service = command.replace("get password", "").strip()
            if service:
                return self.get_password(service)
            return "Please specify service"
        
        elif "update password" in command:
            # Extract service, username, and password
            try:
                # Remove "update password" and split into parts
                parts = command.replace("update password", "").strip().split(" for ", 1)
                if len(parts) == 2:
                    service = parts[1].strip()
                    username = input("Enter new username: ")
                    password = getpass.getpass("Enter new password: ")
                    return self.update_password(service, username, password)
                return "Please specify service, username, and password"
            except Exception as e:
                return f"Error processing update password command: {str(e)}"
        
        elif "delete password" in command:
            # Extract service
            service = command.replace("delete password", "").strip()
            if service:
                return self.delete_password(service)
            return "Please specify service"
        
        elif "list passwords" in command:
            return self.list_services()
        
        return "I didn't understand that password command" 