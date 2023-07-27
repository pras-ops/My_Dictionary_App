from tkinter import *
from src.dictionary import dictionary

def insert1(data):
    if type(data) == list:
        for item in data:
            t.insert(END, item + '\n')
    else:
        t.insert(END, data + '\n')

def search_meaning():
    word = ent_val.get()
    result = dictionary(word)
    t.delete(1.0, END)
    if type(result) == list:
        insert1(result)
    else:
        insert1(result)

def clear():
    t.delete(1.0, END)
    ent.delete(0, END)

root = Tk()
root.title("Dictionary")

head = Label(root, text="Python Dictionary", bg="red", fg="white")
head.pack(fill=X)

label1 = Label(root, text="Enter Word")
label1.pack(fill=X)

ent_val = StringVar()
ent = Entry(root, textvariable=ent_val)
ent.pack()

button = Button(root, text="Meaning", command=search_meaning, bg="orange")
button.pack()

t = Text(root)
t.pack(fill=X)

label2 = Label(root, text="Clear Screen")
label2.pack()

button2 = Button(root, text="Clear", command=clear, bg="orange")
button2.pack()

root.mainloop()
