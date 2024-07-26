import tkinter
from tkinter import *

root=Tk()
root.title('Calculator')
root.geometry('308x450+100+200')
root.resizable(0,0)
root.configure(bg='#17161b')

equation=""

# For taking user input 
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

# For clear  section
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

# For Calculation
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="error.."
            equation=""
    label_result.config(text=result)

# To  create entry section
label_result=Label(root,width=25,height=2,font=('arial',29))
label_result.pack()

# To create button
Button(root,text='C',width=3,font=('arial',25,'bold'),bd=1,bg='#3697f5',fg='#fff',command=lambda : clear()).place(x=8,y=100)
Button(root,text='*',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("*")).place(x=83,y=100)
Button(root,text='/',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("/")).place(x=156,y=100)
Button(root,text='%',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("%")).place(x=233,y=100)

Button(root,text='7',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("7")).place(x=8,y=170)
Button(root,text='8',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("8")).place(x=83,y=170)
Button(root,text='9',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("9")).place(x=156,y=170)
Button(root,text='-',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("-")).place(x=233,y=170)

Button(root,text='4',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("4")).place(x=8,y=240)
Button(root,text='5',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("5")).place(x=83,y=240)
Button(root,text='6',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("6")).place(x=156,y=240)
Button(root,text='+',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("+")).place(x=233,y=240)

Button(root,text='1',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("1")).place(x=8,y=310)
Button(root,text='2',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("2")).place(x=83,y=310)
Button(root,text='3',width=3,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("3")).place(x=156,y=310)
Button(root,text='=',width=3,height=3,font=('arial',24,'bold'),bd=1,bg='#fe9037',fg='#fff',command=lambda : calculate()).place(x=233,y=310)

Button(root,text='0',width=6,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show("0")).place(x=8,y=380)
Button(root,text='.',width=4,font=('arial',25,'bold'),bd=1,bg='#2a2d36',fg='#fff',command=lambda : show(".")).place(x=141,y=380)

root.mainloop()