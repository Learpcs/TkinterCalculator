import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

str = ""

def refresh():
    e1.delete(0, "end")
    e1.insert(0, str)

def f(char):
    global str
    str += char
    refresh()

def calc():
    e1.delete(0, "end")
    e1.insert(0, eval(str))

e1 = ttk.Entry(width = 3)
b0 = ttk.Button(width = 3, text ="0", command=lambda : f("0"))
b1 = ttk.Button(width = 3, text ="1", command=lambda : f("1"))
b2 = ttk.Button(width = 3, text ="2", command=lambda : f("2"))
b3 = ttk.Button(width = 3, text ="3", command=lambda : f("3"))
b4 = ttk.Button(width = 3, text ="4", command=lambda : f("4"))
b5 = ttk.Button(width = 3, text ="5", command=lambda : f("5"))
b6 = ttk.Button(width = 3, text ="6", command=lambda : f("6"))
b7 = ttk.Button(width = 3, text ="7", command=lambda : f("7"))
b8 = ttk.Button(width = 3, text ="8", command=lambda : f("8"))
b9 = ttk.Button(width = 3, text ="9", command=lambda : f("9"))
b10 = ttk.Button(width = 4, text ="+", command=lambda : f("+"))
b11 = ttk.Button(width = 4, text ="-", command=lambda : f("-"))
b12 = ttk.Button(width = 4, text ="*", command=lambda : f("*"))
b13 = ttk.Button(width = 4, text ="/", command=lambda : f("/"))
b14 = ttk.Button(width = 4, text ="=", command=calc)

e1.grid(row=0, column = 0)
b0.grid(row=5, column = 1)
b1.grid(row=2, column = 0)
b2.grid(row=2, column = 1)
b3.grid(row=2, column = 2)
b4.grid(row=3, column = 0)
b5.grid(row=3, column = 1)
b6.grid(row=3, column = 2)
b7.grid(row=4, column = 0)
b8.grid(row=4, column = 1)
b9.grid(row=4, column = 2)
b10.grid(row=2, column = 3)
b11.grid(row=3, column = 3)
b12.grid(row=4, column = 3)
b13.grid(row=5, column = 3)
b14.grid(row=0, column = 3)

window.mainloop()