import tkinter.messagebox as mbox


class CMessage():
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def SetMessageError(self):
        mbox.showerror(self.title, self.message)

    def SetMessageWarning(self):
        mbox.showwarning(self.title, self.message)

    def SetMessageQuestion(self):
        mbox.askquestion(self.title, self.message)

    def SetMessageInfomation(self):
        mbox.showinfo(self.title, self.message)
