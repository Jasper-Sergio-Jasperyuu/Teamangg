from tkinter import *

class ListBoxTest:
    def __init__(self) :
        self.root = Tk()

        self.list_box_1 = Listbox(self.root, selectmode=EXTENDED)
        self.list_box_1.grid(column=0, row=0, rowspan=3)
        self.delete_button = Button(self.root, text="Delete",command=self.DeleteSelection)
        self.delete_button.grid(column=0, row=3)
        self.entry = Entry(self.root, width=15, font=("Arial", 15))
        self.entry.grid(column=1, row=2, rowspan=2)
        self.button = Button(self.root, text="Insert", command=self.Insert)
        self.button.grid(column=1, row=3)


        self.list_box_1.insert(1,"C++")
        self.list_box_1.insert(2,"Python")
        self.list_box_1.insert(3,"HTML")
        self.list_box_1.insert(4,"Java")
        self.root.geometry("300x250+10+10")
        self.root.resizable(False, False)
        self.root.mainloop()
    def DeleteSelection(self) :
        items = self.list_box_1.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.list_box_1.delete( idx,idx )
            pos = pos + 1
    def Insert(self):
        item = self.entry.get()
        if item:
            self.entry.delete(0, END)
            self.list_box_1.insert(END, item)
        else:
            pass
lbt=ListBoxTest()