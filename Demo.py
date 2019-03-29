from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Year")
l2.grid(row=1, column=0)
l3 = Label(window, text="Author")
l3.grid(row=0, column=3)
l4 = Label(window, text="ISDN")
l4.grid(row=1, column=3)

text_title = StringVar()
e1= Entry(window, textvariable = text_title, width = 10)
e1.grid(row=0, column=1)

text_year = StringVar()
e2= Entry(window, textvariable = text_year, width = 10)
e2.grid(row=1, column=1)

text_author = StringVar()
e3= Entry(window, textvariable = text_author, width = 10)
e3.grid(row=0, column=4)

text_isdn = StringVar()
e4= Entry(window, textvariable = text_isdn, width = 10)
e4.grid(row=1, column=4)

list1 = Listbox(window, height = 6, width =35)
list1.grid(row=2, column=0,rowspan = 6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row =2 , column = 2, rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View all",width = 12)
b1.grid(row= 2, column=4)

b2 = Button(window,text="Search",width = 12)
b2.grid(row= 3, column=4)

b3 = Button(window,text="Add entry",width = 12)
b3.grid(row= 4, column=4)

b4 = Button(window,text="Update",width = 12)
b4.grid(row= 5, column=4)

b5 = Button(window,text="Delete",width = 12)
b5.grid(row= 6, column=4)

b6 = Button(window,text="Close",width = 12)
b6.grid(row= 7, column=4)

window.mainloop()
