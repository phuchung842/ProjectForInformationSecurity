class CBelasco:
    def __init__(self, plaintext, key, ciphertext):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext

    def Encrypt(self):
        self.ciphertext = ""
        self.plaintext = self.plaintext.upper()
        self.key = self.key.upper()
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c != ' ':
                row = ord(self.key[i % len(self.key)]) - 65;
                col = ord(c) - 65;
                so = (row + col) % 26
                self.ciphertext += chr(so + 65)
            else:
                self.ciphertext = self.ciphertext + ' '
        return self.ciphertext

    # ========================================
    def Decrypt(self):
        self.plaintext = ""
        self.ciphertext = self.ciphertext.upper()
        self.key = self.key.upper()
        for i in range(len(self.ciphertext)):
            c = self.ciphertext[i]
            if c != ' ':
                row = ord(self.key[i % len(self.key)]) - 65;
                col = ord(c) - 65;
                so = (col - row + 26) % 26
                self.plaintext += chr(so + 65)
            else:
                self.plaintext = self.plaintext + ' '
        return self.plaintext
