# from PIL import Image, ImageTk
# from tkinter import Tk, Label, BOTH
# from tkinter.ttk import Frame, Style
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Absolute positioning")
#         self.pack(fill=BOTH, expand=1)
#
#         Style().configure("TFrame", background="#333")
#
#         bard = Image.open("D:\\Stored\\Tranh\\26247.jpg")
#         bardejov = ImageTk.PhotoImage(bard)
#         label1 = Label(self, image=bardejov)
#         label1.image = bardejov
#         label1.place(x=20, y=20)
#
#         rot = Image.open("D:\\Stored\\Tranh\\1013013.jpg")
#         rotunda = ImageTk.PhotoImage(rot)
#         label2 = Label(self, image=rotunda)
#         label2.image = rotunda
#         label2.place(x=40, y=160)
#
#         minc = Image.open("D:\\Stored\\Tranh\\bur-185.jpg")
#         mincol = ImageTk.PhotoImage(minc)
#         label3 = Label(self, image=mincol)
#         label3.image = mincol
#         label3.place(x=170, y=50)
#
# root = Tk()
# root.geometry("1000x500+100+100")
# app = Example(root)
# root.mainloop()


# from tkinter import Tk, RIGHT, BOTH, RAISED
# from tkinter.ttk import Frame, Button, Style
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Button")
#         self.style = Style()
#         self.style.theme_use("default")
#
#         frame = Frame(self, relief=RAISED, borderwidth=1)
#         frame.pack(fill=BOTH, expand=True)
#         self.pack(fill=BOTH, expand=True)
#
#         closeButton = Button(self, text="Close")
#         closeButton.pack(side=RIGHT, padx=5, pady=5)
#         okButton = Button(self, text="OK",command=quit)
#         okButton.pack(side=RIGHT)
#
#
# root = Tk()
# root.geometry("300x200+300+300")
# app = Example(root)
# root.mainloop()

# from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
# from tkinter.ttk import Frame, Label, Entry
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Review")
#         self.pack(fill=BOTH, expand=True)
#
#         frame1 = Frame(self)
#         frame1.pack(fill=X)
#
#         lbl1 = Label(frame1, text="Title", width=6)
#         lbl1.pack(side=LEFT, padx=5, pady=5)
#
#         entry1 = Entry(frame1)
#         entry1.pack(fill=X, padx=5, expand=True)
#
#         frame2 = Frame(self)
#         frame2.pack(fill=X)
#
#         lbl2 = Label(frame2, text="Author", width=6)
#         lbl2.pack(side=LEFT, padx=5, pady=5)
#
#         entry2 = Entry(frame2)
#         entry2.pack(fill=X, padx=5, expand=True)
#
#         frame3 = Frame(self)
#         frame3.pack(fill=BOTH, expand=True)
#
#         lbl3 = Label(frame3, text="Review", width=6)
#         lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
#
#         txt = Text(frame3)
#         txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
#
# root = Tk()
# root.geometry("300x300+300+300")
# app = Example(root)
# root.mainloop()

# from tkinter import Tk, W, E
# from tkinter.ttk import Frame, Button, Style
# from tkinter.ttk import Entry
#
# class Example(Frame):
#
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.parent.title("Calculator")
#
#         Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
#
#         self.columnconfigure(0, pad=3)
#         self.columnconfigure(1, pad=3)
#         self.columnconfigure(2, pad=3)
#         self.columnconfigure(3, pad=3)
#
#         self.rowconfigure(0, pad=3)
#         self.rowconfigure(1, pad=3)
#         self.rowconfigure(2, pad=3)
#         self.rowconfigure(3, pad=3)
#         self.rowconfigure(4, pad=3)
#
#         entry = Entry(self)
#         entry.grid(row=0, columnspan=4, sticky=W+E)
#         cls = Button(self, text="Cls")
#         cls.grid(row=1, column=0)
#         bck = Button(self, text="Back")
#         bck.grid(row=1, column=1)
#         lbl = Button(self)
#         lbl.grid(row=1, column=2)
#         clo = Button(self, text="Close")
#         clo.grid(row=1, column=3)
#         sev = Button(self, text="7")
#         sev.grid(row=2, column=0)
#         eig = Button(self, text="8")
#         eig.grid(row=2, column=1)
#         nin = Button(self, text="9")
#         nin.grid(row=2, column=2)
#         div = Button(self, text="/")
#         div.grid(row=2, column=3)
#
#         fou = Button(self, text="4")
#         fou.grid(row=3, column=0)
#         fiv = Button(self, text="5")
#         fiv.grid(row=3, column=1)
#         six = Button(self, text="6")
#         six.grid(row=3, column=2)
#         mul = Button(self, text="*")
#         mul.grid(row=3, column=3)
#
#         one = Button(self, text="1")
#         one.grid(row=4, column=0)
#         two = Button(self, text="2")
#         two.grid(row=4, column=1)
#         thr = Button(self, text="3")
#         thr.grid(row=4, column=2)
#         mns = Button(self, text="-")
#         mns.grid(row=4, column=3)
#
#         zer = Button(self, text="0")
#         zer.grid(row=5, column=0)
#         dot = Button(self, text=".")
#         dot.grid(row=5, column=1)
#         equ = Button(self, text="=")
#         equ.grid(row=5, column=2)
#         pls = Button(self, text="+")
#         pls.grid(row=5, column=3)
#
#         self.pack()
#
# root = Tk()
# app = Example(root)
# root.mainloop()

# from tkinter import Tk, Frame, Checkbutton
# from tkinter import BooleanVar, BOTH
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Checkbutton")
#         self.pack(fill=BOTH, expand=True)
#         self.var = BooleanVar()
#
#         cb = Checkbutton(self, text="Show Title", variable=self.var, command=self.onClick)
#         cb.select()
#         cb.place(x=50, y=50)
#
#     def onClick(self):
#         if self.var.get() == True:
#             self.master.title("Checkbutton")
#         else:
#             self.master.title("")
#
# root = Tk()
# root.geometry("250x150+300+300")
# app = Example(root)
# root.mainloop()

# from PIL import Image, ImageTk
# from tkinter import Tk, Frame, Label
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Label")
#
#         self.img = Image.open("D:\\Stored\\Tranh\\bur-185.jpg")
#         tatras = ImageTk.PhotoImage(self.img)
#         label = Label(self, image=tatras)
#
#         label.image = tatras
#
#         label.pack()
#         self.pack()
#
#     def setGeometry(self):
#         w, h = self.img.size
#         self.parent.geometry(("%dx%d+300+300") % (w, h))
#
# root = Tk()
# ex = Example(root)
# ex.setGeometry()
# root.mainloop()
#
# from tkinter import Tk, BOTH, IntVar, LEFT
# from tkinter.ttk import Frame, Label, Scale, Style
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Scale")
#         self.style = Style()
#         self.style.theme_use("clam")
#
#         self.pack(fill=BOTH, expand=1)
#
#         scale = Scale(self, from_=0, to=100, command=self.onScale)
#         scale.pack(side=LEFT, padx=15)
#
#         self.var = IntVar()
#         self.label = Label(self, text=0, textvariable=self.var)
#         self.label.pack(side=LEFT)
#
#     def onScale(self, val):
#         v = int(float(val))
#         self.var.set(v)
#
# root = Tk()
# ex = Example(root)
# root.geometry("250x100+300+300")
# root.mainloop()

# from tkinter import Frame, Tk, Menu
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Simple Menu")
#
#         menuBar = Menu(self.parent)
#         self.parent.config(menu=menuBar)
#
#         fileMenu = Menu(menuBar)
#         fileMenu.add_command(label="Exit", command=self.onExit)
#         menuBar.add_cascade(label="File", menu=fileMenu,command=self.quit)
#
#     def onExit(self):
#         self.quit()
#
# root = Tk()
# root.geometry("250x150+300+300")
# app = Example(root)
# root.mainloop()

# from tkinter import *
#
# option = [
#     "1",
#     '2',
#     '3',
#     '4'
# ]
# master = Tk()
# variable = StringVar(master)
# variable.set(option[0])
# w = OptionMenu(master, variable, *option)
# w.pack()
#
#
# def ok():
#     print("VALUE IS" + variable.get())
#
#
# button = Button(master, text="OK", command=ok)
# button.pack()
# mainloop()


# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *
#
# # creates a Tk() object
# master = Tk()
#
# # sets the geometry of main
# # root window
# master.geometry("200x200")
#
#
# # function to open a new window
# # on a button click
# def openNewWindow():
#
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
#
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window")
#
#     # sets the geometry of toplevel
#     newWindow.geometry("200x200")
#
#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text ="This is a new window").pack()
#
#
# label = Label(master,
#               text ="This is the main window")
#
# label.pack(pady = 10)
#
# # a button widget which will open a
# # new window on button click
# btn = Button(master,
#              text ="Click to open a new window",
#              command = openNewWindow)
# btn.pack(pady = 10)
#
# # mainloop, runs infinitely
# mainloop()

# import hashlib
#
# result=hashlib.md5(b'abcdehgj')
# stra="dsajgdas"
# print((hashlib.md5(stra.encode())).hexdigest())
#
# print(result.digest())


# import hashlib
#
# l = ["riyad", "onni", "arman"]
#
# def check_user(h):
#     for i in l:
#         if h == hashlib.md5(i.encode('utf-8')).hexdigest():
#             return i
#
#
# print(check_user(hashlib.md5(l[2].encode('utf-8')).hexdigest()))


# Import Required Module
# from tkinter import *
# from tkinter.ttk import *
#
# # Create Object
# root = Tk()
#
# # Set geometry (widthxheight)
# root.geometry('100x100')
#
# # This will create style object
# style = Style()
#
# # This will be adding style, and
# # naming that style variable as
# # W.Tbutton (TButton is used for ttk.Button).
# style.configure('W.TButton', font =
# ('calibri', 10, 'bold', 'underline'),
#                 foreground = 'red')
#
# # Style will be reflected only on
# # this button because we are providing
# # style only on this Button.
# # ''' Button 1'''
# btn1 = Button(root, text = 'Quit !',
#               style = 'W.TButton',
#               command = root.destroy)
# btn1.grid(row = 0, column = 3, padx = 100)
#
# # ''' Button 2'''
#
# btn2 = Button(root, text = 'Click me !', command = None)
# btn2.grid(row = 1, column = 3, pady = 10, padx = 100)
#
# # Execute Tkinter
# root.mainloop()
#
# from tkinter import *
# from tkinter.ttk import *
#
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.parent.title("Encryt&Decrypt")
#
#         self.style = Style()
#         self.style.theme_use("clam")
#         self.style.configure('TButton', background='white', foreground='black', width=20, borderwidth=1,
#                              focusthickness=3, focuscolor='none')
#         self.style.map('TButton', background=[('active', 'grey')], foreground=[('active', 'yellow')])
#         self.style.configure('TLabel', background='#f0f0f0')
#         self.style.configure('Danger.TLabel', foreground='red')
#         self.style.configure('TEntry', background='#caf0f8')
#
#         self.menubar = Menu(self.parent)
#
#         self.filemenu = Menu(self.menubar, tearoff=0)
#         self.filemenu.add_command(label="Exit", command=self.onExit)
#
#         self.subedit_theme = Menu(self.menubar)
#         self.subedit_theme.add_command(label="Default", command=lambda: self.WSetTheme("default"))
#         self.subedit_theme.add_command(label="Clam", command=lambda: self.WSetTheme("clam"))
#         self.subedit_theme.add_command(label="Alt", command=lambda: self.WSetTheme("alt"))
#         self.subedit_theme.add_command(label="Classic", command=lambda: self.WSetTheme("classic"))
#
#         self.subedit_color = Menu(self.menubar)
#         self.subedit_color.add_command(label='Light', command=lambda: self.WSetColor("Light"))
#         self.subedit_color.add_command(label='Dark', command=lambda: self.WSetColor("Dark"))
#
#         self.editmenu = Menu(self.menubar, tearoff=0)
#         self.editmenu.add_cascade(label="Color", menu=self.subedit_color)
#         self.editmenu.add_cascade(label='Theme', menu=self.subedit_theme)
#
#         self.subtype_classic = Menu(self.menubar)
#         self.subtype_classic.add_command(label="Ceasar", command=lambda: self.WSetKind("Ceasar"))
#         self.subtype_classic.add_command(label="Belasco", command=lambda: self.WSetKind("Belasco"))
#         self.subtype_classic.add_command(label="Tritheminus", command=lambda: self.WSetKind("Tritheminus"))
#         self.subtype_classic.add_command(label="Vignere", command=lambda: self.WSetKind("Vignere"))
#         self.subtype_classic.add_command(label="CV_2D", command=lambda: self.WSetKind("CV_2D"))
#         self.subtype_classic.add_command(label="CV_ND", command=lambda: self.WSetKind("CV_ND"))
#         self.subtype_classic.add_command(label="SimpleDES", command=lambda: self.WSetKind("SimpleDES"))
#
#         self.subtype_modern = Menu(self.menubar)
#         self.subtype_modern.add_command(label="MD5", command=lambda: self.WSetKind("MD5"))
#         self.subtype_modern.add_command(label="AES", command=lambda: self.WSetKind("AES"))
#
#         self.typemenu = Menu(self.menubar, tearoff=0)
#         self.typemenu.add_cascade(label="Classic", menu=self.subtype_classic)
#         self.typemenu.add_separator()
#         self.typemenu.add_cascade(label="Modern", menu=self.subtype_modern)
#
#         self.aboutmenu = Menu(self.menubar, tearoff=0)
#         self.aboutmenu.add_command(label='About')
#         self.aboutmenu.add_command(label='Help')
#
#         self.menubar.add_cascade(label="File", menu=self.filemenu)
#         self.menubar.add_cascade(label="Edit", menu=self.editmenu)
#         self.menubar.add_cascade(label="Type", menu=self.typemenu)
#         self.menubar.add_cascade(label="About", menu=self.aboutmenu)
#
#         self.parent.config(menu=self.menubar)
#
#         # Code
#         self.code_text = StringVar()
#         self.code_label = Label(self.parent, text="Code", font=('bold', 13))
#         self.code_label.grid(row=0, column=2, sticky=W)
#         self.code_entry = Entry(self.parent, textvariable=self.code_text, width=30)
#         self.code_entry.grid(row=0, column=3, sticky=E)
#         # Decode
#         self.decode_text = StringVar()
#         self.decode_label = Label(self.parent, text="Decode", font=('bold', 13))
#         self.decode_label.grid(row=1, column=2, sticky=E)
#         self.decode_entry = Entry(self.parent, textvariable=self.decode_text, width=30)
#         self.decode_entry.grid(row=1, column=3)
#         # Key
#         self.key_text = StringVar()
#         self.key_label = Label(self.parent, text="Key", font=('bold', 13), )
#         self.key_label.grid(row=2, column=2, sticky=W)
#         self.key_entry = Entry(self.parent, textvariable=self.key_text, width=30)
#         self.key_entry.grid(row=2, column=3)
#
#         # Buttons
#         self.btn_encrypt = Button(self.parent, text="Encrypt", width=28, command=self.WEncryptCode)
#         self.btn_encrypt.grid(row=0, column=0, pady=20, padx=10, columnspan=2)
#         self.btn_decrypt = Button(self.parent, text="Decrypt", width=28, command=self.WDecryptCode)
#         self.btn_decrypt.grid(row=1, column=0, pady=20, padx=10, columnspan=2)
#         self.btn_clear = Button(self.parent, text="Clear", width=28, command=self.WClear)
#         self.btn_clear.grid(row=2, column=0, pady=20, padx=10, columnspan=2)
#         #
#         self.kind_label = Label(self.parent, text="Type: ", font=('bold', 13))
#         self.kind_label.grid(row=4, column=2, sticky=W)
#         self.kindcrypt_label = Label(self.parent, style='Danger.TLabel', text="Ceasar", font=('bold', 13))
#         self.kindcrypt_label.grid(row=4, column=3, sticky=W)
#
#     def WSetTheme(self, theme_name):
#         self.style.theme_use(theme_name)
#
#     def WSetColor(self, color_name):
#         if (color_name == "Dark"):
#             self.parent.configure(bg='#03045e')
#             self.style.configure('TButton', background='#0077b6', foreground='#caf0f8', width=20, borderwidth=1,
#                                  focusthickness=3, focuscolor='none')
#             self.style.map('TButton', background=[('active', '#caf0f8')], foreground=[('active', '#03045e')])
#             self.style.configure('TLabel', background='#03045e', foreground='#caf0f8')
#             self.style.configure('Danger.TLabel', foreground='yellow')
#             self.style.configure('TEntry', bg='#caf0f8')
#         else:
#             self.parent.configure(bg='#f0f0f0')
#             self.style.configure('TButton', background='white', foreground='black', width=20, borderwidth=1,
#                                  focusthickness=3, focuscolor='none')
#             self.style.map('TButton', background=[('active', 'grey')], foreground=[('active', 'yellow')])
#             self.style.configure('TLabel', background='#f0f0f0', foreground='black')
#             self.style.configure('Danger.TLabel', foreground='red')
#             self.style.configure('TEntry', background='white')
#
#         # quitButton = Button(self, text="Quit", command=self.quit)
#         # quitButton.place(x=50, y=50)
#     def WSetKind(self, kind_name):
#         print('test')
#         # set = Set(self.kindcrypt_label, self.key_label, self.key_entry)
#         # set.SetKind(kind_name)
#
#     def WEncryptCode(self):
#         print('test')
#         # flag = True
#         # if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
#         #     self.key_entry.insert(END, "")
#         #     if (self.code_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Code need to fill").SetMessageError()
#         # else:
#         #     if (self.key_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Key need to fill").SetMessageError()
#         #     if (self.code_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Code need to fill").SetMessageError()
#         #
#         # if (flag == True):
#         #     encrypt = CEncrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
#         #     encrypt.EncryptCode()
#
#     def WDecryptCode(self):
#         print('test')
#         # flag = True
#         # if (self.kindcrypt_label.cget("text") == "Tritheminus" or self.kindcrypt_label.cget("text") == "CV_2D"):
#         #     self.key_entry.insert(END, "")
#         #     if (self.decode_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Decode need to fill").SetMessageError()
#         # else:
#         #     if (self.key_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Key need to fill").SetMessageError()
#         #     if (self.decode_entry.get() == ""):
#         #         flag = False
#         #         msg = CMessage("Error", "Decode need to fill").SetMessageError()
#         #
#         # if (flag == True):
#         #     decrypt = CDecrypt(self.kindcrypt_label, self.decode_entry, self.code_entry, self.key_entry)
#         #     decrypt.DecryptCode()
#
#     def WClear(self):
#         print('test')
#         # self.code_entry.insert(END, "")
#         # self.decode_entry.insert(END, "")
#         # self.key_entry.insert(END, "")
#     def onExit(self):
#         self.quit()
# root = Tk()
# root.geometry("550x500+300+300")
# app = Example(root)
# root.mainloop()
from Ceasar import CCeasar as Ceasar

k = 3
f = open("D:\\test.txt", "r")
print(f.read())
f.close()
