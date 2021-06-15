import os
from Ceasar import CCeasar as Ceasar
from Belasco import CBelasco as Belasco
from Vignere import CVignere as Vignere
from Trithemius import CTrithemius as Tritheminus
from SimpleDES import CXOR as XOR
from ChuyenVi import CChuyenViHaiDong as CV_2D
from ChuyenVi import CChuyenViNhieuDong as CV_ND
from AES import CAESCipher as AES


class CDecrypt():
    def __init__(self, kindcrypt_label, key_entry):
        self.kindcrypt_label = kindcrypt_label
        self.key_entry = key_entry

    def DecryptCode(self, decode_entry):
        if (self.kindcrypt_label.cget("text") == "Ceasar"):
            ceasar = Ceasar("", int(self.key_entry.get()), decode_entry)
            return ceasar.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "Belasco"):
            belasco = Belasco("", self.key_entry.get(), decode_entry)
            return belasco.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            vignere = Vignere("", int(self.key_entry.get()), decode_entry)
            return vignere.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "Tritheminus"):
            tritheminus = Tritheminus("", decode_entry)
            return tritheminus.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "SimpleDES"):
            simpledes = XOR()
            return simpledes.Encrypt(decode_entry, int(self.key_entry.get()))
        elif (self.kindcrypt_label.cget("text") == "CV_2D"):
            cv_2d = CV_2D("", decode_entry)
            return cv_2d.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "CV_ND"):
            cv_nd = CV_ND("", self.key_entry.get(), decode_entry)
            return cv_nd.Decrypt()
        elif (self.kindcrypt_label.cget("text") == "AES"):
            aes = AES(self.key_entry.get())
            return aes.Decrypt(decode_entry)
        else:
            return "Error"


class ExportFile():
    def __init__(self, filepath, kindcrypt_label, key_entry):
        self.filepath = filepath
        self.kindcrypt_label = kindcrypt_label
        self.key_entry = key_entry

    def Export(self):
        textfile = open(self.filepath, 'r').read()
        filename = os.path.basename(self.filepath)
        name = os.path.splitext(filename)[0]
        path = "D:\\Stored\\ProjectForInformationSecurity\\Export\\Decrypt\\" + name + "_decrypt.txt"
        file = open(path, "w")
        encrypt_text = CDecrypt(self.kindcrypt_label, self.key_entry)
        file.write(encrypt_text.DecryptCode(textfile))
