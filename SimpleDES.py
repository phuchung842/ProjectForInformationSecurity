class CXOR:
    def Encrypt(self, p, key):
        ci = ""
        for c in p:
            if c != ' ':
                so = ord(c) - 65;
                so = so ^ key
                ci += chr(so + 65)
            else:
                ci += c
        return ci
