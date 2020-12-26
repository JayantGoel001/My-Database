from tkinter import *
import backend

selected_row = []


def getSelectedRow(event):
    global selected_row
    index = listBox.curselection()[0]
    selected_row = listBox.get(index)
    print(index)


def addCommand():
    backend.insert(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(),
                   python_text.get())
    listBox.delete(0, END)
    listBox.insert(END, (date_text.get(), earning_text.get(), exercise_text.get(),
                         study_text.get(), diet_text.get(), python_text.get()))


def viewCommand():
    listBox.delete(0, END)
    for row in backend.view():
        listBox.insert(END, row)


def searchCommand():
    listBox.delete(0, END)
    for row in backend.Search(date_text.get(), earning_text.get(), exercise_text.get(),
                              study_text.get(), diet_text.get(), python_text.get()):
        listBox.insert(END, row)


def deleteCommand():
    backend.delete(selected_row[0])


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
l6.grid(row=2, column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable=earning_text)
e2.grid(row=0, column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1, column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1, column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2, column=1)

python_text = StringVar()
e6 = Entry(win, textvariable=python_text)
e6.grid(row=2, column=3)

listBox = Listbox(win, height=8, width=35)
listBox.grid(row=3, column=0, rowspan=9, columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9)

listBox.bind('<<ListboxSelect>>', getSelectedRow)

b1 = Button(win, text='ADD', width=12, pady=5, command=addCommand)
b1.grid(row=3, column=3)

b2 = Button(win, text='SEARCH', width=12, pady=5, command=searchCommand)
b2.grid(row=4, column=3)

b3 = Button(win, text='DELETE', width=12, pady=5, command=deleteCommand)
b3.grid(row=5, column=3)

b4 = Button(win, text='VIEW ALL', width=12, pady=5, command=viewCommand)
b4.grid(row=6, column=3)

b5 = Button(win, text='CLOSE', width=12, pady=5, command=win.destroy)
b5.grid(row=7, column=3)

win.title("My Database")
win.mainloop()
