from cryptography.fernet import Fernet
from abc import ABC, abstractmethod
import os
from hashlib import sha256
from base64 import b64encode
class Encrypt:
    def __init__(self):
        with open('system.key', 'rb') as f:
            self.system_key = f.read()
        with open('user.key', 'rb') as f:
            self.user_key = f.read()
        self.fernet = Fernet(b64encode(sha256(self.system_key + self.user_key).digest()))

    @abstractmethod
    def encrypt(self, path):
        files = os.listdir(path)
        for file in files:
            with open(path + "/" + file, 'rb') as f:
                data = f.read()
                encrypted_data = self.fernet.encrypt(data)
            with open(path + "/" + file, 'wb') as f:
                f.write(encrypted_data)
    
    @abstractmethod
    def decrypt(self, path):
        files = os.listdir(path)
        for file in files:
            with open(path + "/" + file, 'rb') as f:
                data = f.read()
                decrypted_data = self.fernet.decrypt(data)
            with open(path + "/" + file, 'wb') as f:
                f.write(decrypted_data)




