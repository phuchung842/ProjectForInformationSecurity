class CTrithemius:
    def __init__(self, plaintext, ciphertext):
        self.plaintext = plaintext
        self.ciphertext = ciphertext

    # ========================================
    def Encrypt(self):
        self.ciphertext = ""
        self.plaintext = self.plaintext.upper()
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c != ' ':
                so = ord(c) - 65;
                so = (so + (i % 26)) % 26
                self.ciphertext += chr(so + 65)
            else:
                self.ciphertext += ' '
        return self.ciphertext

    # ========================================
    def Decrypt(self):
        self.plaintext = ""
        self.ciphertext = self.ciphertext.upper()
        for i in range(len(self.ciphertext)):
            c = self.ciphertext[i]
            if c != ' ':
                so = ord(c) - 65
                so = (so - (i % 26) + 26) % 26
                self.plaintext += chr(so + 65)
            else:
                self.plaintext += ' '
        return self.plaintext
