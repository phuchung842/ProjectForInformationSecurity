from Ceasar import CCeasar as Ceasar
from Belasco import CBelasco as Belasco
from Vignere import CVignere as Vignere
from Trithemius import CTrithemius as Tritheminus
from SimpleDES import CXOR as XOR
from ChuyenVi import CChuyenViHaiDong as CV_2D
from ChuyenVi import CChuyenViNhieuDong as CV_ND
from AES import CAESCipher as AES

from tkinter import *


class CDecrypt():
    def __init__(self, kindcrypt_label, decode_entry, code_entry, key_entry):
        self.kindcrypt_label = kindcrypt_label
        self.decode_entry = decode_entry
        self.code_entry = code_entry
        self.key_entry = key_entry

    def DecryptCode(self):
        if (self.kindcrypt_label.cget("text") == "Ceasar"):
            self.code_entry.delete(0, END)
            ceasar = Ceasar("", int(self.key_entry.get()), self.decode_entry.get())
            self.code_entry.insert(END, ceasar.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "Belasco"):
            self.code_entry.delete(0, END)
            belasco = Belasco("", self.key_entry.get(), self.decode_entry.get())
            self.code_entry.insert(END, belasco.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            self.code_entry.delete(0, END)
            vignere = Vignere("", self.key_entry.get(), self.decode_entry.get())
            self.code_entry.insert(END, vignere.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "Tritheminus"):
            self.code_entry.delete(0, END)
            tritheminus = Tritheminus("", self.decode_entry.get())
            self.code_entry.insert(END, tritheminus.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "SimpleDES"):
            self.code_entry.delete(0, END)
            simpledes = XOR()
            self.code_entry.insert(END, simpledes.Encrypt(self.decode_entry.get(), int(self.key_entry.get())))
        elif (self.kindcrypt_label.cget("text") == "CV_2D"):
            self.code_entry.delete(0, END)
            cv_2d = CV_2D("", self.decode_entry.get())
            self.code_entry.insert(END, cv_2d.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "CV_ND"):
            self.code_entry.delete(0, END)
            cv_nd = CV_ND("", self.key_entry.get(), self.decode_entry.get())
            self.code_entry.insert(END, cv_nd.Decrypt())
        elif (self.kindcrypt_label.cget("text") == "AES"):
            self.code_entry.delete(0, END)
            aes = AES(self.key_entry.get())
            self.code_entry.insert(END, aes.Decrypt(self.decode_entry.get()))
        else:
            print('Error')
