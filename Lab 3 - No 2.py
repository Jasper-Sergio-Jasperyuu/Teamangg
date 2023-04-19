from tkinter import *
class MyWindow:
    def __init__(self, win):

        self.txt1 = Entry(win, bd=3)
        self.txt1.place(x = 100, y = 50, width = 150, height = 50)


window = Tk()
mywin = MyWindow(window)
window.geometry("350x150+10+10")
window.title("Text Field")
window.mainloop()