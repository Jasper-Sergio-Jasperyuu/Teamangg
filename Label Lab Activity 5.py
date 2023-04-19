from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl1 = Label(win, text="Laboratory Activity 5")
        self.lbl1.place(x=150, y=80)
        self.lbl2 = Label(win, text= "Submitted to Mam Sayo")
        self.lbl2.place(x=140, y=100)

window = Tk()
mywin = MyWindow(window)
window.geometry("400x200+10+10")
window.title("Label")
window.mainloop()