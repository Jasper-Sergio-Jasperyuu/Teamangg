from tkinter import *
win = Tk()

def eql(): #function to evaluate/calculate written operation
    try:
        result = eval(txt1.get())
        txt1.delete(0, END)
        txt1.insert(0, result)
    except:
        txt1.delete(0, END)
        txt1.insert(0, "ERROR")

def dlt(): #function to delete the last character
    entry = txt1.get()
    modentry = entry[:-1]
    txt1.delete(0, END)
    txt1.insert(0, modentry)

txt1 = Entry(win, bd=10, relief="ridge", bg="grey11",fg="white", font=("Century Gothic", 20))
txt1.grid(row=0, column=0,columnspan=4)
# create a list of tuples that contains the button text and its position in the grid
# Format for each tuple (number/operation, row, column, columnspan)
num_btns = [('1', 5, 0, 1), ('2', 5, 1, 1), ('3', 5, 2, 1),('4', 4, 0, 1), ('5', 4, 1, 1), ('6', 4, 2, 1), 
            ('7', 3, 0, 1), ('8', 3, 1, 1), ('9', 3, 2, 1), ("(", 6, 0, 1), ('0', 6, 1, 1),(")", 6, 2, 1),
            ("+", 3, 3, 1), ('-', 4, 3, 1),('*', 5, 3, 1),('/', 6, 3, 1), ('.', 7, 0 ,1)]

# loop through the list and create each button
for btn in num_btns:
    btn_txt, row, col, span = btn
    button = Button(win, text=btn_txt, bg="darkgoldenrod1", width=6 , font=("Century Gothic", 15), command=lambda text=btn_txt: txt1.insert(END, text))
    button.grid(row=row, column=col, columnspan=span, pady=2)

exponent = Button(win, text="^", bg="darkgoldenrod1", width=6 , font=("Century Gothic", 15), command=lambda: txt1.insert(END, "**"))
exponent.grid(row=7, column=1, pady=2)

equal = Button(win, text="=", bg="grey11",fg="white", width=12 , font=("Century Gothic", 15), command=eql)
equal.grid(row=7, column=2, columnspan=2)

clear = Button(win, text="AC", width=10, font=("Century Gothic", 18), bg="grey11",fg="white", command = lambda: txt1.delete(0,END))
clear.grid(row=1, column=0, columnspan=2, pady=5)

delete = Button(win, text="del", width=10, font=("Century Gothic", 18), bg="grey11",fg="white", command =dlt)
delete.grid(row=1, column=2, columnspan=2, pady=5)

win.geometry("327x350+10+10")
win.resizable(False, False)
win.configure(bg="lightyellow")
win.title("Simple Calculator")
win.mainloop() 