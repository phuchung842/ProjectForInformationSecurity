import hashlib


class CMD5:
    def __init__(self, plaintext):
        self.plaintext = plaintext

    def Encrypt(self):
        return hashlib.md5(self.plaintext.encode()).hexdigest()


result = CMD5("hung")
