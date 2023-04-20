from tkinter import *

win = Tk()
win.geometry("300x150+30+30")
win.title("Father of Computer")

label = Label(win, text="Charles Babbage", font=("Arial", 14), fg="black", bg="Cyan")
label.place(x=70, y=50)

win.mainloop()
