from tkinter import *


class CSetKindCrypt():
    def __init__(self, kindcrypt_label, key_label, key_entry, decode_entry):
        self.kindcrypt_label = kindcrypt_label
        self.key_label = key_label
        self.key_entry = key_entry
        self.decode_entry = decode_entry

    def SetKind(self, kind_name):
        if (kind_name == "MD5"):
            self.decode_entry.configure(state='normal')
            self.decode_entry.delete(0, END)
            self.kindcrypt_label.config(text=kind_name)
            self.decode_entry.configure(state='readonly')
            self.key_label.grid_remove()
            self.key_entry.grid_remove()
        elif (kind_name == "Tritheminus" or kind_name == "CV_2D"):
            self.kindcrypt_label.config(text=kind_name)
            self.decode_entry.configure(state='normal')
            self.key_label.grid_remove()
            self.key_entry.grid_remove()
        else:
            self.kindcrypt_label.config(text=kind_name)
            self.decode_entry.configure(state='normal')
            self.key_label.grid(row=2, column=2, sticky=W)
            self.key_entry.grid(row=2, column=3)

# def Ceasar(self):
#     self.kindcrypt_label.config(text="Ceasar")
#     self.key_label.grid(row=0, column=4, sticky=W)
#     self.key_entry.grid(row=0, column=5)
#
# def Belasco(self):
#     self.kindcrypt_label.config(text="Belasco")
#     self.key_label.grid(row=0, column=4, sticky=W)
#     self.key_entry.grid(row=0, column=5)
#
# def Tritheminus(self):
#     self.kindcrypt_label.config(text="Tritheminus")
#     self.key_label.grid_remove()
#     self.key_entry.grid_remove()
#
# def Vignere(self):
#     self.kindcrypt_label.config(text="Vignere")
#     self.key_label.grid(row=0, column=4, sticky=W)
#     self.key_entry.grid(row=0, column=5)
#
# def SimpleDES(self):
#     self.kindcrypt_label.config(text="SimpleDES")
#     self.key_label.grid_remove()
#     self.key_entry.grid_remove()
#
# def ChuyenVi2Dong(self):
#     self.kindcrypt_label.config(text="CV_2D")
#     self.key_label.grid_remove()
#     self.key_entry.grid_remove()
#
# def ChuyenViNhieuDong(self):
#     self.kindcrypt_label.config(text="CV_ND")
#     self.key_label.grid(row=0, column=4, sticky=W)
#     self.key_entry.grid(row=0, column=5)
