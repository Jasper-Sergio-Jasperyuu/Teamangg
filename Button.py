from tkinter import *
color = ['blue', 'yellow', 'skyblue', 'lightgreen', 'cyan', 'purple']
c = 0

win = Tk()
win.geometry("600x200+30+30")
win.title("Button")


def change():
    global c
    c += 1
    if c == 6:
        c = 0
    else:
        pass
    button.configure(bg=color[c])


button = Button(win,fg="red",text="Click me!", bg=f"{color[c]}", activebackground="gray", command=change)
button.place(x=100, y=150)
text = Label(win, text="<--- Click to change the color of the button", borderwidth=3, relief="ridge")
text.place(x=200, y=150)   
win.mainloop()
