from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from SetKindCrypt import CSetKindCrypt as Set
from Encypt import CEncrypt
from EncryptFile import ExportFile as E_ExportFile
from DecryptFile import ExportFile as D_ExportFile
from Decrypt import CDecrypt
from Message import CMessage


class CLayout(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Encryt&Decrypt")

        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure('TButton', background='white', foreground='black', width=20, borderwidth=1,
                             focusthickness=3, focuscolor='none')
        self.style.map('TButton', background=[('active', 'grey')], foreground=[('active', 'white')])
        self.style.configure('TLabel', background='#f0f0f0')
        self.style.configure('Danger.TLabel', foreground='red')
        self.style.configure('TEntry', background='#caf0f8')

        self.menubar = Menu(self.parent)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.onExit)

        self.subedit_theme = Menu(self.menubar)
        self.subedit_theme.add_command(label="Default", command=lambda: self.WSetTheme("default"))
        self.subedit_theme.add_command(label="Clam", command=lambda: self.WSetTheme("clam"))
        self.subedit_theme.add_command(label="Alt", command=lambda: self.WSetTheme("alt"))
        self.subedit_theme.add_command(label="Classic", command=lambda: self.WSetTheme("classic"))

        self.subedit_color = Menu(self.menubar)
        self.subedit_color.add_command(label='Light', command=lambda: self.WSetColor("Light"))
        self.subedit_color.add_command(label='Dark', command=lambda: self.WSetColor("Dark"))

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_cascade(label="Color", menu=self.subedit_color)
        self.editmenu.add_cascade(label='Theme', menu=self.subedit_theme)

        self.subtype_classic = Menu(self.menubar)
        self.subtype_classic.add_command(label="Ceasar", command=lambda: self.WSetKind("Ceasar"))
        self.subtype_classic.add_command(label="Belasco", command=lambda: self.WSetKind("Belasco"))
        self.subtype_classic.add_command(label="Tritheminus", command=lambda: self.WSetKind("Tritheminus"))
        self.subtype_classic.add_command(label="Vignere", command=lambda: self.WSetKind("Vignere"))
        self.subtype_classic.add_command(label="CV_2D", command=lambda: self.WSetKind("CV_2D"))
        self.subtype_classic.add_command(label="CV_ND", command=lambda: self.WSetKind("CV_ND"))
        self.subtype_classic.add_command(label="SimpleDES", command=lambda: self.WSetKind("SimpleDES"))

        self.subtype_modern = Menu(self.menubar)

        self.subtype_modern.add_command(label="MD5", command=lambda: self.WSetKind("MD5"))
        self.subtype_modern.add_command(label="AES", command=lambda: self.WSetKind("AES"))

        self.typemenu = Menu(self.menubar, tearoff=0)
        self.typemenu.add_cascade(label="Classic", menu=self.subtype_classic)
        self.typemenu.add_separator()
        self.typemenu.add_cascade(label="Modern", menu=self.subtype_modern)

        self.aboutmenu = Menu(self.menubar, tearoff=0)
        self.aboutmenu.add_command(label='About')
        self.aboutmenu.add_command(label='Help')

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Type", menu=self.typemenu)
        self.menubar.add_cascade(label="About", menu=self.aboutmenu)

        self.parent.config(menu=self.menubar)

        # Code
        self.code_text = StringVar()
        self.code_label = Label(self.parent, text="Code", font=('bold', 13))
        self.code_label.grid(row=0, column=2, sticky=W)
        self.code_entry = Entry(self.parent, textvariable=self.code_text, width=30)
        self.code_entry.grid(row=0, column=3, sticky=E)
        # Decode
        self.decode_text = StringVar()
        self.decode_label = Label(self.parent, text="Decode", font=('bold', 13))
        self.decode_label.grid(row=1, column=2, sticky=E)
        self.decode_entry = Entry(self.parent, textvariable=self.decode_text, width=30)
        self.decode_entry.grid(row=1, column=3)
        # Key
        self.key_text = StringVar()
        self.key_label = Label(self.parent, text="Key", font=('bold', 13), )
        self.key_label.grid(row=2, column=2, sticky=W)
        self.key_entry = Entry(self.parent, textvariable=self.key_text, width=30)
        self.key_entry.grid(row=2, column=3)

        # Buttons
        self.btn_encrypt = Button(self.parent, text="Encrypt", width=28, command=self.WEncryptCode)
        self.btn_encrypt.grid(row=0, column=0, pady=20, padx=10, columnspan=2)
        self.btn_decrypt = Button(self.parent, text="Decrypt", width=28, command=self.WDecryptCode)
        self.btn_decrypt.grid(row=1, column=0, pady=20, padx=10, columnspan=2)
        self.btn_clear = Button(self.parent, text="Clear", width=28, command=self.WClear)
        self.btn_clear.grid(row=2, column=0, pady=20, padx=10, columnspan=2)
        # Type
        self.kind_label = Label(self.parent, text="Type: ", font=('bold', 13))
        self.kind_label.grid(row=3, column=2, sticky=W)
        self.kindcrypt_label = Label(self.parent, style='Danger.TLabel', text="Ceasar", font=('bold', 13))
        self.kindcrypt_label.grid(row=3, column=3, sticky=W)

        # File
        self.filecode_text = StringVar()
        self.filecode_label = Label(self.parent, text="File Code", font=('bold', 13))
        self.filecode_label.grid(row=4, column=0)
        self.filecode_entry = Entry(self.parent, textvariable=self.filecode_text, width=72)
        self.filecode_entry.grid(row=5, column=0, columnspan=4, sticky=E)

        self.filecode_btn_encrypt = Button(self.parent, text="Encryt File", width=28, command=self.EncryptFile)
        self.filecode_btn_encrypt.grid(row=6, column=0, pady=20, padx=10, sticky=W, columnspan=4)
        self.fileopen_btn_encrypt = Button(self.parent, text="Open File", width=28,
                                           command=lambda: self.BrowseFiles("encrypt"))
        self.fileopen_btn_encrypt.grid(row=6, column=0, pady=20, sticky=E, columnspan=4)

        self.filedecode_text = StringVar()
        self.filedecode_label = Label(self.parent, text="File Decode", font=('bold', 13))
        self.filedecode_label.grid(row=7, column=0)
        self.filedecode_entry = Entry(self.parent, textvariable=self.filedecode_text, width=72)
        self.filedecode_entry.grid(row=8, column=0, columnspan=4, sticky=E)

        self.filedecode_btn_decrypt = Button(self.parent, text="Decryt File", width=28, command=self.DecryptFile)
        self.filedecode_btn_decrypt.grid(row=9, column=0, pady=20, padx=10, sticky=W, columnspan=4)
        self.fileopen_btn_decrypt = Button(self.parent, text="Open File", width=28,
                                           command=lambda: self.BrowseFiles("decrypt"))
        self.fileopen_btn_decrypt.grid(row=9, column=0, pady=20, sticky=E, columnspan=4)

        self.filepath = ""

    def EncryptFile(self):
        flag = True
        if (self.kindcrypt_label.cget("text") == "MD5"):
            if (self.filecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()
        elif (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
            self.key_entry.insert(END, "")
            if (self.filecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()
        else:
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.filecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()

        if (flag == True):
            E_ExportFile(self.filepath, self.kindcrypt_label, self.key_entry).Export()
            msg = CMessage("Info", "Encrypt success").SetMessageInfomation()

    def DecryptFile(self):
        flag = True
        if (self.kindcrypt_label.cget("text") == "MD5"):
            if (self.filedecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()
        elif (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
            self.key_entry.insert(END, "")
            if (self.filedecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()
        else:
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.filedecode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Don't have file").SetMessageError()

        if (flag == True):
            D_ExportFile(self.filepath, self.kindcrypt_label, self.key_entry).Export()
            msg = CMessage("Info", "Decrypt success").SetMessageInfomation()

    def BrowseFiles(self, name):
        if (name == "decrypt"):
            self.filepath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                       filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
            self.filedecode_entry.delete(0, END)
            self.filedecode_entry.insert(END, self.filepath)
        else:
            self.filepath = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                       filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
            self.filecode_entry.delete(0, END)
            self.filecode_entry.insert(END, self.filepath)

    def WSetTheme(self, theme_name):
        self.style.theme_use(theme_name)

    def WSetColor(self, color_name):
        if (color_name == "Dark"):
            self.parent.configure(bg='#03045e')
            self.style.configure('TButton', background='#0077b6', foreground='#caf0f8', width=20, borderwidth=1,
                                 focusthickness=3, focuscolor='none')
            self.style.map('TButton', background=[('active', '#caf0f8')], foreground=[('active', '#03045e')])
            self.style.configure('TLabel', background='#03045e', foreground='#caf0f8')
            self.style.configure('Danger.TLabel', foreground='yellow')
            self.style.configure('TEntry', bg='#caf0f8')
        else:
            self.parent.configure(bg='#f0f0f0')
            self.style.configure('TButton', background='white', foreground='black', width=20, borderwidth=1,
                                 focusthickness=3, focuscolor='none')
            self.style.map('TButton', background=[('active', 'grey')], foreground=[('active', 'white')])
            self.style.configure('TLabel', background='#f0f0f0', foreground='black')
            self.style.configure('Danger.TLabel', foreground='red')
            self.style.configure('TEntry', background='white')

    def WSetKind(self, kind_name):
        set = Set(self.kindcrypt_label, self.key_label, self.key_entry, self.decode_entry)
        set.SetKind(kind_name)

    def WEncryptCode(self):
        flag = True
        if (self.kindcrypt_label.cget("text") == "MD5"):
            if (self.code_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Code need to fill").SetMessageError()
        elif (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
            self.key_entry.insert(END, "")
            if (self.code_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Code need to fill").SetMessageError()
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            if (self.key_entry.get().isnumeric()):
                flag = False
                msg = CMessage("Error", "Key need to a character").SetMessageInfomation()
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.code_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Code need to fill").SetMessageError()
        else:
            if(self.kindcrypt_label.cget("text")!="CV_ND"):
                if (self.key_entry.get().isnumeric() == False):
                    flag = False
                    msg = CMessage("Error", "Key need to a number").SetMessageInfomation()
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.code_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Code need to fill").SetMessageError()

        if (flag == True):
            encrypt = CEncrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
            encrypt.EncryptCode()

    def WDecryptCode(self):
        flag = True
        if (self.kindcrypt_label.cget("text") == "MD5"):
            flag = False
        elif (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
            self.key_entry.insert(END, "")
            if (self.decode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Decode need to fill").SetMessageError()
        elif (self.kindcrypt_label.cget("text") == "Vignere"):
            if (self.key_entry.get().isnumeric()):
                flag = False
                msg = CMessage("Error", "Key need to a character").SetMessageInfomation()
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.decode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Decode need to fill").SetMessageError()
        else:
            if(self.kindcrypt_label.cget("text")!="CV_ND"):
                if (self.key_entry.get().isnumeric() == False):
                    flag = False
                    msg = CMessage("Error", "Key need to a number").SetMessageInfomation()
            if (self.key_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Key need to fill").SetMessageError()
            if (self.decode_entry.get() == ""):
                flag = False
                msg = CMessage("Error", "Decode need to fill").SetMessageError()

        if (flag == True):
            decrypt = CDecrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
            decrypt.DecryptCode()

    def WClear(self):
        self.code_entry.delete(0, END)
        self.decode_entry.configure(state='normal')
        self.decode_entry.delete(0, END)
        self.key_entry.delete(0, END)

    def onExit(self):
        self.quit()
