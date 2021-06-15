import os

from Ceasar import CCeasar as Ceasar
from Belasco import CBelasco as Belasco
from Vignere import CVignere as Vignere
from Trithemius import CTrithemius as Tritheminus
from SimpleDES import CXOR as XOR
from ChuyenVi import CChuyenViHaiDong as CV_2D
from ChuyenVi import CChuyenViNhieuDong as CV_ND
from MD5 import CMD5 as MD5
from AES import CAESCipher as AES

from tkinter import *


class CEncrypt():
    def __init__(self, kindcrypt_label, key_entry):
        self.kindcrypt_label = kindcrypt_label
        self.key_entry = key_entry

    def EncryptCode(self, code_entry):
        if (self.kindcrypt_label.cget("text") == "Ceasar"):
            ceasar = Ceasar(code_entry, int(self.key_entry.get()), "")
            return ceasar.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "Belasco"):
            belasco = Belasco(code_entry, self.key_entry.get(), "")
            return belasco.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            vignere = Vignere(code_entry, int(self.key_entry.get()), "")
            return vignere.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "Tritheminus"):
            tritheminus = Tritheminus(code_entry, "")
            return tritheminus.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "SimpleDES"):
            simpledes = XOR()
            return simpledes.Encrypt(code_entry, int(self.key_entry.get()))
        elif (self.kindcrypt_label.cget("text") == "CV_2D"):
            cv_2d = CV_2D(code_entry, "")
            return cv_2d.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "CV_ND"):
            cv_nd = CV_ND(code_entry, self.key_entry.get(), "")
            return cv_nd.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "MD5"):
            md5 = MD5(code_entry)
            return md5.Encrypt()
        elif (self.kindcrypt_label.cget("text") == "AES"):
            aes = AES(self.key_entry.get())
            return aes.Encrypt(code_entry)
        else:
            return 'Error'


class ExportFile():
    def __init__(self, filepath, kindcrypt_label, key_entry):
        self.filepath = filepath
        self.kindcrypt_label = kindcrypt_label
        self.key_entry = key_entry

    def Export(self):
        textfile = open(self.filepath, 'r').read()
        filename = os.path.basename(self.filepath)
        name = os.path.splitext(filename)[0]
        path = "D:\\Stored\\ProjectForInformationSecurity\\Export\\Encrypt\\" + name + "_encrypt.txt"
        file = open(path, "w")
        encrypt_text = CEncrypt(self.kindcrypt_label, self.key_entry)
        file.write(str(encrypt_text.EncryptCode(textfile)))
