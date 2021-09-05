from tkinter import *

def Nakopl():
    if txt_NSum.get() is not '':
        NSum=int(txt_NSum.get())
    else:
        NSum=0

    if txt_MSum.get() is not '':
        MSum=int(txt_MSum.get())
    else:
        MSum=0

    if txt_Sr.get() is not '':
        Sr=int(txt_Sr.get())
    else:
        Sr=0

    if txt_Pr.get() is not '':
        Pr=int(txt_Pr.get())
    else:
        Pr=0

    res=NSum

    for i in range(int(Sr)*12):
        res=res+MSum+(res+MSum)*(Pr/1200)
        print(f'месяц: {i} сумма: {res:.2f}')
    lbl_Rez.configure(text=int(res))
    lbl_Mes.configure(text=int((res*(4.5/100))/12))

def clear(event):
    caller = event.widget
    caller.delete("0", "end")

    #MainWindow
window=Tk()
##window.geometry('600x400')
window.title('Расчет накоплений')

lbl_NSum=Label(window,text='Начальная сумма:',font=('Arial',14))
lbl_MSum=Label(window,text='Ежемесячные взносы:',font=('Arial',14))
lbl_Sr=Label(window,text='Срок вложения:',font=('Arial',14))
lbl_Pr=Label(window,text='Процентная ставка:',font=('Arial',14))
lbl_Nak=Label(window,text='Накопленная сумма:',font=('Arial',14))
lbl_Rez=Label(window,text='',font=('Arial Bold',18))
lbl_MesLab=Label(window,text='Ежемесячно:',font=('Arial',14))
lbl_Mes=Label(window,text='',font=('Arial Bold',18))


txt_NSum=Entry(window,width=20)
txt_MSum=Entry(window,width=20)
txt_Sr=Entry(window,width=20)
txt_Pr=Entry(window,width=20)


btn=Button(window,text='РАСЧЕТ', command=Nakopl, bg='Black',fg='White',pady=10)

txt_NSum.bind("<FocusIn>", clear)
txt_MSum.bind("<FocusIn>", clear)
txt_Sr.bind("<FocusIn>", clear)
txt_Pr.bind("<FocusIn>", clear)

lbl_NSum.pack()
txt_NSum.pack()
txt_NSum.focus()
lbl_MSum.pack()
txt_MSum.pack()
lbl_Sr.pack()
txt_Sr.pack()
lbl_Pr.pack()
txt_Pr.pack()
btn.pack(expand=1, fill='both')
lbl_Nak.pack(expand=1, fill='both')
lbl_Rez.pack(expand=1, fill='both')
lbl_MesLab.pack(expand=1, fill='both')
lbl_Mes.pack(expand=1, fill='both')


window.mainloop()
