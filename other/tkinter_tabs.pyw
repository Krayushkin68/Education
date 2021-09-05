from tkinter import *
from tkinter import ttk

window=Tk()
window.title('Tabs')
window.geometry('400x250')

Tabs=ttk.Notebook(window)
tab1=ttk.Frame(Tabs)
tab2=ttk.Frame(Tabs)
Tabs.add(tab1,text='First')
Tabs.add(tab2,text='Second')

lbl1=Label(tab1,text='This is tab1')
lbl1.pack()

lbl2=Label(tab2,text='This is tab2')
lbl2.pack()

Tabs.pack(expand=1,fill='both')

window.mainloop()
