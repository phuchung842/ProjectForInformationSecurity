from tkinter import *
from Window import CWindow as CWindow
# from Test import Example
from Layout import CLayout


def Main():
    app = Tk()
    app.geometry('500x500+200+100')
    run = CLayout(app)
    # run = CWindow(app)
    app.mainloop()


if __name__ == '__main__':
    Main()
