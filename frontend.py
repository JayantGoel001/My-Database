from tkinter import *

win = Tk()

l1 = Label(win, text='Date')
l1.grid(row=0, column=0)

l2 = Label(win, text='Earning')
l2.grid(row=0, column=2)

l3 = Label(win, text='Exercise')
l3.grid(row=1, column=0)

l4 = Label(win, text='Study')
l4.grid(row=1, column=2)

l5 = Label(win, text='Diet')
l5.grid(row=2, column=0)

l6 = Label(win, text='Python')
l6.grid(row=2, column=1)

win.mainloop()
