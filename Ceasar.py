class CCeasar:
    def __init__(self, plaintext, key, ciphertext):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext

    def Encrypt(self):
        self.ciphertext = ""
        self.plaintext = self.plaintext.upper()
        for c in self.plaintext:
            if c != ' ':
                so = ord(c) - 65
                so = (so + self.key) % 26
                self.ciphertext = self.ciphertext + chr(so + 65)
            else:
                self.ciphertext = self.ciphertext + c
        return self.ciphertext

    def Decrypt(self):
        self.plaintext = ""
        self.ciphertext = self.ciphertext.upper()
        for c in self.ciphertext:
            if c != ' ':
                so = ord(c) - 65
                so = (so - self.key + 26) % 26
                self.plaintext = self.plaintext + chr(so + 65)
            else:
                self.plaintext = self.plaintext + c
        return self.plaintext
