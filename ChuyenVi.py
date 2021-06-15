class CChuyenViHaiDong:
    def __init__(self, plaintext, ciphertext):
        self.plaintext = plaintext
        self.ciphertext = ciphertext

    # ========================================
    def Encrypt(self):
        self.plaintext = self.plaintext.upper()
        self.ciphertext = self.plaintext[0]
        for i in range(1, len(self.plaintext), 2):
            self.ciphertext += self.plaintext[i]
        for i in range(2, len(self.plaintext), 2):
            self.ciphertext += self.plaintext[i]
        return self.ciphertext

    # ========================================
    def Decrypt(self):
        self.ciphertext = self.ciphertext.upper()
        self.plaintext = list(self.ciphertext)
        k = 1
        for i in range(1, len(self.plaintext), 2):
            self.plaintext[i] = self.ciphertext[k]
            k = k + 1
        for i in range(2, len(self.plaintext), 2):
            self.plaintext[i] = self.ciphertext[k]
            k = k + 1
        return ''.join(x for x in self.plaintext)


import numpy as np
import math


# ========================================
class CChuyenViNhieuDong:
    def __init__(self, plaintext, key, ciphertext):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
        self.key = [x for x in str(self.key).split(',')]
        self.key = [int(i) for i in self.key]

    # ========================================
    # ========================================
    def FindX(self, x):
        for i in range(len(self.key)):
            if self.key[i] == x:
                return i
        return -1;

    # ========================================
    def Encrypt(self):
        self.plaintext = self.plaintext.upper()
        soCot = len(self.key)
        soDong = math.ceil(len(self.plaintext) / soCot)
        tam = []
        k = 0
        for i in range(soDong):
            row = []
            for j in range(soCot):
                if k >= len(self.plaintext): row += ['*']; continue
                row += [self.plaintext[k]];
                k += 1
            tam += [row]
        self.ciphertext = ""
        for i in range(1, len(self.key) + 1, 1):
            viTriCot = self.FindX(i)
            for r in tam:
                self.ciphertext += r[viTriCot]
        return self.ciphertext

    # ========================================
    def Decrypt(self):
        self.ciphertext = self.ciphertext.upper()
        soCot = len(self.key)
        soDong = math.ceil(len(self.ciphertext) / soCot)
        tam = np.zeros((soDong, soCot))
        i = 0
        for k in range(1, len(self.key) + 1, 1):
            viTriCot = self.FindX(k)
            for r in range(soDong):
                tam[r][viTriCot] = ord(self.ciphertext[i]);
                i += 1
        self.plaintext = ""
        for r in tam:
            for c in r:
                self.plaintext += chr(int(c))
        return self.plaintext.rstrip('*')
