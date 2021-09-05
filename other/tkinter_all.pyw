from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.ttk import Style          #???
from tkinter import filedialog
from os import path
from tkinter import Menu

def clfun():
    res='Hello {}'.format(txt.get())
    lbl.configure(text=res)
    #messagebox.showinfo('123','456')
    ans=messagebox.askokcancel('123',spin.get())

    #MainWindow    
window=Tk()
window.geometry('600x400')
window.title('Tkinter Tutorial')

    #Label
lbl=Label(window,text='Hello',font=('Arial',25))
#lbl.grid(column=0,row=0)

    #TextEdit
txt=Entry(window,width=10)
#txt.grid(column=0,row=1)
txt.focus()

    #ComboBox
combo=Combobox(window)
#combo.grid(column=1,row=1)
combo['values']=(1,2,3,4,5,'aabcd')
combo.current(1)

    #CheckButton
chk_state=BooleanVar()
chk_state.set(False)
chk=Checkbutton(window,text='Choise', var=chk_state)
#chk.grid(column=2,row=1)

rad1=Radiobutton(window,text='First',value=1)  #selected.get()
rad2=Radiobutton(window,text='Second',value=2)
rad3=Radiobutton(window,text='Third',value=3)
#rad1.grid(column=3,row=1)
#rad2.grid(column=3,row=2)
#rad3.grid(column=3,row=3)

    #ScrolledText
scr=scrolledtext.ScrolledText(window, width=40,height=10)
scr.insert(INSERT,'This is text')
#scr.grid(column=1, row=3)

    #Button
btn=Button(window,text='Button', command=clfun, bg='Yellow',fg='Black',padx=5,pady=5)
#btn.grid(column=0,row=2)

    #SpinBox
var=IntVar()
var.set(17)
spin=Spinbox(window,from_=0, to=100, width=6, textvariable=var)

    #ProgressBar
bar=Progressbar(window, length=200)
bar['value']=70

    #OpenDialog
#file=filedialog.askopenfilename(filetypes=(('Text','*.txt'),('all','*.*')))
#files=filedialog.askopenfilenames()
#dir=filedialog.askdirectory(initialdir=path.dirname(__file__))

    #Menu
menu=Menu(window)
#menu.add_command(label='File')
new=Menu(menu, tearoff=0)
new.add_command(label='New', command=clfun)
new.add_separator()
new.add_command(label='Edit')
menu.add_cascade(label='File', menu=new)
window.config(menu=menu)

    #Design
lbl.pack(expand=1, fill='both')
txt.pack(expand=1, fill='both')
combo.pack(expand=1, fill='both')
chk.pack(expand=1, fill='both')
rad1.pack(expand=1, fill='both')
rad2.pack(expand=1, fill='both')
rad3.pack(expand=1, fill='both')
scr.pack(expand=1, fill='both')
btn.pack(expand=1, fill='both')
spin.pack(expand=1, fill='both')
bar.pack(expand=1, fill='both')

window.mainloop()
