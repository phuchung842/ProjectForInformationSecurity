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
    def __init__(self, kindcrypt_label, decode_entry, code_entry, key_entry):
        self.kindcrypt_label = kindcrypt_label
        self.decode_entry = decode_entry
        self.code_entry = code_entry
        self.key_entry = key_entry

    def EncryptCode(self):
        if (self.kindcrypt_label.cget("text") == "Ceasar"):
            self.decode_entry.delete(0, END)
            ceasar = Ceasar(self.code_entry.get(), int(self.key_entry.get()), "")
            self.decode_entry.insert(END, ceasar.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "Belasco"):
            self.decode_entry.delete(0, END)
            belasco = Belasco(self.code_entry.get(), self.key_entry.get(), "")
            self.decode_entry.insert(END, belasco.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            self.decode_entry.delete(0, END)
            vignere = Vignere(self.code_entry.get(), self.key_entry.get(), "")
            self.decode_entry.insert(END, vignere.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "Tritheminus"):
            self.decode_entry.delete(0, END)
            tritheminus = Tritheminus(self.code_entry.get(), "")
            self.decode_entry.insert(END, tritheminus.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "SimpleDES"):
            self.decode_entry.delete(0, END)
            simpledes = XOR()
            self.decode_entry.insert(END, simpledes.Encrypt(self.code_entry.get(), int(self.key_entry.get())))
        elif (self.kindcrypt_label.cget("text") == "CV_2D"):
            self.decode_entry.delete(0, END)
            cv_2d = CV_2D(self.code_entry.get(), "")
            self.decode_entry.insert(END, cv_2d.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "CV_ND"):
            self.decode_entry.delete(0, END)
            cv_nd = CV_ND(self.code_entry.get(), self.key_entry.get(), "")
            self.decode_entry.insert(END, cv_nd.Encrypt())
        elif (self.kindcrypt_label.cget("text") == "MD5"):
            self.decode_entry.configure(state='normal')
            self.decode_entry.delete(0, END)
            md5 = MD5(self.code_entry.get())
            self.decode_entry.insert(END, md5.Encrypt())
            self.decode_entry.configure(state='readonly')
        elif (self.kindcrypt_label.cget("text") == "AES"):
            self.decode_entry.delete(0, END)
            aes = AES(self.key_entry.get())
            self.decode_entry.insert(END, aes.Encrypt(self.code_entry.get()))
        else:
            print('Error')
