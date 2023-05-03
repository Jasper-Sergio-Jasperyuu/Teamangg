from tkinter import *
win = Tk()
win.geometry("355x180+10+10")
win.resizable(False,False)
win.configure(bg="lightyellow")

txt = ["a", "a^2", "a^3"]
for t in range (3):
    indic = Label(text=txt[t], relief="ridge", bd=1, font=("Century Gothic", 15), background="white", height=2, width=9)
    indic.grid(row=0, column=t, padx=2)
for lable in range (1,5):
    lable
    powone = Label(text = lable,relief="ridge", bg="light goldenrod", font=("Century Gothic", 15), width=9)
    powone.grid(row=lable, column=0, padx=2, pady=1)
    powtwo = Label(text = lable**2,relief="ridge", bg="light goldenrod", font=("Century Gothic", 15), width=9)
    powtwo.grid(row=lable, column=1, padx=2, pady=1)
    powthree = Label(text = lable**3,relief="ridge", bg="light goldenrod", font=("Century Gothic", 15), width=9)
    powthree.grid(row=lable, column=2, padx=2, pady=1)

win.mainloop()