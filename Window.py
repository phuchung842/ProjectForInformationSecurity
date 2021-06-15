from tkinter.ttk import *
from tkinter import *

from SetKindCrypt import CSetKindCrypt as Set
from Encypt import CEncrypt
from Decrypt import CDecrypt
from Message import CMessage


class CWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Encryp & Decypt")

        self.style = Style()
        self.style.theme_use("clam")

        self.pack(fill=BOTH, expand=1)

        # Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        menubar = Menu(self)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.onExit)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Color")

        typemenu = Menu(menubar, tearoff=0)
        typemenu.add_command(label="Ceasar", command=lambda: self.WSetKind("Ceasar"))
        typemenu.add_command(label="Belasco", command=lambda: self.WSetKind("Belasco"))
        typemenu.add_command(label="Tritheminus", command=lambda: self.WSetKind("Tritheminus"))
        typemenu.add_command(label="Vignere", command=lambda: self.WSetKind("Vignere"))
        typemenu.add_command(label="CV_2D", command=lambda: self.WSetKind("CV_2D"))
        typemenu.add_command(label="CV_ND", command=lambda: self.WSetKind("CV_ND"))
        typemenu.add_command(label="SimpleDES", command=lambda: self.WSetKind("SimpleDES"))
        typemenu.add_separator()
        typemenu.add_command(label="MD5", command=lambda: self.WSetKind("MD5"))
        typemenu.add_command(label="AES", command=lambda: self.WSetKind("AES"))

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label='About')
        aboutmenu.add_command(label='Help')

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Type", menu=typemenu)
        menubar.add_cascade(label="About", menu=aboutmenu)

        self.parent.config(menu=menubar)

        # Code
        code_text = StringVar()
        code_label = Label(self, text="Code", font=('bold', 13), pady=20, padx=10)
        code_label.grid(row=0, column=2, sticky=W)
        code_entry = Entry(self, textvariable=code_text, width=30)
        code_entry.grid(row=0, column=3, sticky=E)
        # Decode
        decode_text = StringVar()
        decode_label = Label(self, text="Decode", font=('bold', 13), pady=20, padx=10)
        decode_label.grid(row=1, column=2, sticky=E)
        decode_entry = Entry(self, textvariable=decode_text, width=30)
        decode_entry.grid(row=1, column=3)
        # Key
        key_text = StringVar()
        key_label = Label(self, text="Key", font=('bold', 13), pady=20, padx=10)
        key_label.grid(row=2, column=2, sticky=W)
        key_entry = Entry(self, textvariable=key_text, width=30)
        key_entry.grid(row=2, column=3)

        # Buttons
        btn_encrypt = Button(self, text="Encrypt", width=28, height=3, command=self.WEncryptCode)
        btn_encrypt.grid(row=0, column=0, pady=20, padx=10, columnspan=2)
        btn_decrypt = Button(self, text="Decrypt", width=28, height=3, command=self.WDecryptCode)
        btn_decrypt.grid(row=1, column=0, pady=20, padx=10, columnspan=2)
        btn_clear = Button(self, text="Clear", width=28, height=3, command=self.WClear)
        btn_clear.grid(row=2, column=0, pady=20, padx=10, columnspan=2)
        #
        kind_label = Label(self, text="Type: ", font=('bold', 13), pady=20, padx=10)
        kind_label.grid(row=4, column=2, sticky=W)
        kindcrypt_label = Label(self, text="Ceasar", fg="red", font=('bold', 13))
        kindcrypt_label.grid(row=4, column=3, sticky=W)

    def WSetKind(self, kind_name):
        print('test')
        # set = Set(self.kindcrypt_label, self.key_label, self.key_entry)
        # set.SetKind(kind_name)

    def WEncryptCode(self):
        print('test')
        # flag = True
        # if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
        #     self.key_entry.insert(END, "")
        #     if (self.code_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Code need to fill").SetMessageError()
        # else:
        #     if (self.key_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Key need to fill").SetMessageError()
        #     if (self.code_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Code need to fill").SetMessageError()
        #
        # if (flag == True):
        #     encrypt = CEncrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
        #     encrypt.EncryptCode()

    def WDecryptCode(self):
        print('test')
        # flag = True
        # if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
        #     self.key_entry.insert(END, "")
        #     if (self.decode_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Decode need to fill").SetMessageError()
        # else:
        #     if (self.key_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Key need to fill").SetMessageError()
        #     if (self.decode_entry.get() == ""):
        #         flag = False
        #         msg = CMessage("Error", "Decode need to fill").SetMessageError()
        #
        # if (flag == True):
        #     decrypt = CDecrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
        #     decrypt.DecryptCode()

    def WClear(self):
        print('test')
        # self.code_entry.insert(END, "")
        # self.decode_entry.insert(END, "")
        # self.key_entry.insert(END, "")

        # testing
        # self.menubar=Menu(self.parent)
        #
        # self.filemenu=Menu(self.menubar,tearoff=0)
        # self.filemenu.add_command(label="Exit",command=self.onExit)
        #
        # self.editmenu=Menu(self.menubar,tearoff=0)
        # self.editmenu.add_command(label="Color")
        #
        # self.typemenu=Menu(self.menubar,tearoff=0)
        # self.typemenu.add_command(label="Ceasar",command=lambda: self.WSetKind("Ceasar"))
        # self.typemenu.add_command(label="Belasco",command=lambda: self.WSetKind("Belasco"))
        # self.typemenu.add_command(label="Tritheminus",command=lambda: self.WSetKind("Tritheminus"))
        # self.typemenu.add_command(label="Vignere",command=lambda: self.WSetKind("Vignere"))
        # self.typemenu.add_command(label="CV_2D",command=lambda: self.WSetKind("CV_2D"))
        # self.typemenu.add_command(label="CV_ND",command=lambda: self.WSetKind("CV_ND"))
        # self.typemenu.add_command(label="SimpleDES",command=lambda: self.WSetKind("SimpleDES"))
        # self.typemenu.add_separator()
        # self.typemenu.add_command(label="MD5",command=lambda: self.WSetKind("MD5"))
        # self.typemenu.add_command(label="AES",command=lambda: self.WSetKind("AES"))
        #
        # self.aboutmenu=Menu(self.menubar,tearoff=0)
        # self.aboutmenu.add_command(label='About')
        # self.aboutmenu.add_command(label='Help')
        #
        # self.menubar.add_cascade(label="File",menu=self.filemenu)
        # self.menubar.add_cascade(label="Edit",menu=self.editmenu)
        # self.menubar.add_cascade(label="Type", menu=self.typemenu)
        # self.menubar.add_cascade(label="About",menu=self.aboutmenu)
        #
        # self.parent.config(menu=self.menubar)
        #
        # # Code
        # self.code_text = StringVar()
        # self.code_label = Label(self.parent, text="Code", font=('bold', 13), pady=20, padx=10)
        # self.code_label.grid(row=0, column=2, sticky=W)
        # self.code_entry = Entry(self.parent, textvariable=self.code_text, width=30)
        # self.code_entry.grid(row=0, column=3, sticky=E)
        # # Decode
        # self.decode_text = StringVar()
        # self.decode_label = Label(self.parent, text="Decode", font=('bold', 13), pady=20, padx=10)
        # self.decode_label.grid(row=1, column=2, sticky=E)
        # self.decode_entry = Entry(self.parent, textvariable=self.decode_text, width=30)
        # self.decode_entry.grid(row=1, column=3)
        # # Key
        # self.key_text = StringVar()
        # self.key_label = Label(self.parent, text="Key", font=('bold', 13), pady=20, padx=10)
        # self.key_label.grid(row=2, column=2, sticky=W)
        # self.key_entry = Entry(self.parent, textvariable=self.key_text, width=30)
        # self.key_entry.grid(row=2, column=3)
        #
        # # Buttons
        # btn_encrypt = Button(self.parent, text="Encrypt", width=28, height=3, command=self.WEncryptCode)
        # btn_encrypt.grid(row=0, column=0, pady=20, padx=10, columnspan=2)
        # btn_decrypt = Button(self.parent, text="Decrypt", width=28, height=3, command=self.WDecryptCode)
        # btn_decrypt.grid(row=1, column=0, pady=20, padx=10, columnspan=2)
        # btn_clear = Button(self.parent, text="Clear", width=28, height=3, command=self.WClear)
        # btn_clear.grid(row=2, column=0, pady=20, padx=10, columnspan=2)
        # #
        # self.kind_label = Label(self.parent, text="Type: ", font=('bold', 13), pady=20, padx=10)
        # self.kind_label.grid(row=4, column=2, sticky=W)
        # self.kindcrypt_label = Label(self.parent, text="Ceasar", fg="red", font=('bold', 13))
        # self.kindcrypt_label.grid(row=4, column=3, sticky=W)

        # testing

        #
        # self.btn_ceasar = Button(self.parent, text="Ceasar", bg="grey", fg="white", width=12,
        #                          command=lambda: self.WSetKind("Ceasar"))
        # self.btn_ceasar.grid(row=4, column=0, pady=20, padx=10)
        # self.btn_belasco = Button(self.parent, text="Belasco", bg="grey", fg="white", width=12,
        #                           command=lambda: self.WSetKind("Belasco"))
        # self.btn_belasco.grid(row=4, column=1)
        # self.btn_tritheminus = Button(self.parent, text="Tritheminus", bg="grey", fg="white", width=12,
        #                               command=lambda: self.WSetKind("Tritheminus"))
        # self.btn_tritheminus.grid(row=5, column=0)
        # self.btn_vignere = Button(self.parent, text="Vignere", bg="grey", fg="white", width=12,
        #                           command=lambda: self.WSetKind("Vignere"))
        # self.btn_vignere.grid(row=5, column=1)
        # self.btn_chuyenvihaidong = Button(self.parent, text="CV_2D", bg="grey", fg="white", width=12,
        #                                   command=lambda: self.WSetKind("CV_2D"))
        # self.btn_chuyenvihaidong.grid(row=6, column=0, pady=20, padx=10)
        # self.btn_chuyenvinhieudong = Button(self.parent, text="CV_ND", bg="grey", fg="white", width=12,
        #                                     command=lambda: self.WSetKind("CV_ND"))
        # self.btn_chuyenvinhieudong.grid(row=6, column=1)
        # self.btn_simpledes = Button(self.parent, text="SimpleDES", bg="grey", fg="white", width=12,
        #                             command=lambda: self.WSetKind("SimpleDES"))
        # self.btn_simpledes.grid(row=7, column=0)

        # self.pack()

    def onExit(self):
        self.quit()

    # def WSetKind(self, kind_name):
    #     set = Set(self.kindcrypt_label, self.key_label, self.key_entry)
    #     set.SetKind(kind_name)
    #
    # def WEncryptCode(self):
    #     flag = True
    #     if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
    #         self.key_entry.insert(END, "")
    #         if (self.code_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Code need to fill").SetMessageError()
    #     else:
    #         if (self.key_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Key need to fill").SetMessageError()
    #         if (self.code_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Code need to fill").SetMessageError()
    #
    #     if (flag == True):
    #         encrypt = CEncrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
    #         encrypt.EncryptCode()
    #
    # def WDecryptCode(self):
    #     flag = True
    #     if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
    #         self.key_entry.insert(END, "")
    #         if (self.decode_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Decode need to fill").SetMessageError()
    #     else:
    #         if (self.key_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Key need to fill").SetMessageError()
    #         if (self.decode_entry.get() == ""):
    #             flag = False
    #             msg = CMessage("Error", "Decode need to fill").SetMessageError()
    #
    #     if (flag == True):
    #         decrypt = CDecrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
    #         decrypt.DecryptCode()
    #
    # def WClear(self):
    #     self.code_entry.insert(END, "")
    #     self.decode_entry.insert(END, "")
    #     self.key_entry.insert(END, "")
