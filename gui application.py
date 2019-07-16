from tkinter import*
from tkinter import ttk
import time

root=Tk()
root.title("GUI APLLICATION")
d=Frame(root)
d.pack()
Tops=Frame(root,width=1600,height=40,bg="light blue",relief=SUNKEN)
Tops.pack(side=RIGHT,padx=120,pady=120)
#Topss=Frame(root,bg="light blue",relief=SUNKEN)
#Topss.pack(side =RIGHT)
f2=Frame(root,width=300,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=BOTTOM)
#photo=PhotoImage(file="C:\\Users\\DELL\\Pictures\\Screenshots\\o.png")
#labelp=Label(root,image=photo)
#labelp.pack()
#---------------------label----------------------------------------------------------#
label=Label(text="DELICIOUS CHINESE CORNER",fg="blue",font=("italian",40),bg="black")
root.geometry("1300x300")
label.config(width=45,height=2)
label.pack(padx=10,pady=10)
#----time
localtime=time.asctime(time.localtime(time.time()))
labeo=Label(text=localtime,fg="black",bg="light blue")
labeo.config(width=99,height=2)
labeo.pack()
#-----------------------background colour-----------------------------------------------#
root.config(background="blue");

label3=Label(text="MENU",font=("italian",20,"bold"),fg="blue",bg="red")
label3.config(width=28,height=2);
label3.pack(anchor=W);
#-----------------------------------------------menu------------------------------------------
def f():
    sel="YOU SELECTED THE CHINESE CONTENT AND YOUR OPTION IS :"+ str(var.get())
    label.config(text=sel)
var=IntVar();
w1=Radiobutton(root,text="OPTION1:SUB MENU",fg="red",bg="black",font=("calibri",29),relief="sunken",variable=var,value=1,command=f)
w1.pack(anchor=W,padx=10)
w2=Radiobutton(root,text="OPTION2:AMERICAN CHOPSE",fg="red",bg="black",font=("calibri",19),relief="sunken",variable=var,value=2,command=f)
w2.pack(anchor=W,padx=10)
w2=Radiobutton(root,text="OPTION3:ALLO PATTISE",fg="red",bg="black",font=("calibri",19),relief="sunken",variable=var,value=3,command=f)
w2.pack(anchor=W,padx=10)
w2=Radiobutton(root,text="OPTION4:CHILLI PANEER",fg="red",bg="black",font=("calibri",19),relief="sunken",variable=var,value=4,command=f)
w2.pack(anchor=W,padx=10)
w2=Radiobutton(text="OPTION5:SCHEZWAN NOODLES",fg="red",bg="black",font=("calibri",19),relief="sunken",variable=var,value=5,command=f)
w2.pack(anchor=W,padx=10)
label=Label(root)
label.pack()
#------------------------------------entry widget----------------------------------#
t1=Label(Tops,text="MANCHURIAN",fg="black",font=("calibri",19,"bold"),bg="red")
t1.grid(row=0,column=0)
t2=Entry(Tops)
t2.grid(row=0,column=1)
t3=Label(Tops,text="AMERICAN CHOPSE",fg="black",font=("calibri",19,"bold"),bg="red")
t3.grid(row=1,column=0)
t31=Entry(Tops)
t31.grid(row=1,column=1)
t1=Label(Tops,text="BURGER MEAL",fg="black",font=("calibri",19,"bold"),bg="red")
t1.grid(row=2,column=0)
t2=Entry(Tops)
t2.grid(row=2,column=1)
t1=Label(Tops,text="DELICIOUS PIZZA",fg="black",font=("calibri",19,"bold"),bg="red")
t1.grid(row=3,column=0)
t2=Entry(Tops)
t2.grid(row=3,column=1)
t1=Label(Tops,text="CHICKEN MEAL",fg="black",font=("calibri",19,"bold"),bg="red")
t1.grid(row=4,column=0)
t2=Entry(Tops)
t2.grid(row=4,column=1)
t1=Label(Tops,text="CHESSE MEAL",fg="black",font=("calibri",19,"bold"),bg="red")
t1.grid(row=5,column=0)
t2=Entry(Tops)
t2.grid(row=5,column=1)
t54=Label(Tops,text="COCKTAIL",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=6,column=0)
t24=Entry(Tops)
t24.grid(row=6,column=1)
t54=Label(Tops,text="CHILLI PANNEER",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=7,column=0)
t24=Entry(Tops)
t24.grid(row=7,column=1)
t54=Label(Tops,text="HAKKA NOODLES",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=8,column=0)
t24=Entry(Tops)
t24.grid(row=8,column=1)
t54=Label(Tops,text="SCHEZWAN NOODLES",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=9,column=0)
t24=Entry(Tops)
t24.grid(row=9,column=1)
t54=Label(Tops,text="MOMOS",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=10,column=0)
t24=Entry(Tops)
t24.grid(row=10,column=1)
t54=Label(Tops,text="SPRING ROLLS",fg="black",font=("calibri",19,"bold"),bg="red")
t54.grid(row=11,column=0)
t24=Entry(Tops)
t24.grid(row=11,column=1)

#-----------------------------------------------button-------------------------------------------------
a=Button(text="Total",bg="light blue",font=("calibri",10,"bold"))
a.pack(anchor=W)
b=Button(text="Reset",bg="light blue",font=("calibri",10,"bold"))
b.pack(side=LEFT,ipadx=50,ipady=30)
c=Button(text="Quit",bg="light blue",font=("calibri",10,"bold"))
c.pack(side=LEFT,padx=80,pady=30)
c.config(width=10,height=5)
a.config(width=10,height=5)
#----------------------------------------calci----------------------------------------#
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btnClear(numbers):
    global operator
    operator=""
    text_Input.set("")
def btnEquals(numbers):
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
#ca.title("Calculator")
operator=""
text_Input=StringVar()

entry=Entry(f2,font=("arial",20,"bold"),textvariable=text_Input,bd=30,insertwidth=4,
            bg="powder blue",justify="right").grid(columnspan=4)

bt1=Button(f2,text="1",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(1),font=("arial",20,"bold")).grid(row=1,column=0)
bt1=Button(f2,text="2",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(2),font=("arial",20,"bold")).grid(row=1,column=1)
bt1=Button(f2,text="3",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(3),font=("arial",20,"bold")).grid(row=1,column=2)
bt1=Button(f2,text="+",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick("+"),font=("arial",20,"bold")).grid(row=1,column=3)

bt1=Button(f2,text="4",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(4),font=("arial",20,"bold")).grid(row=2,column=0)
bt1=Button(f2,text="5",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(5),font=("arial",20,"bold")).grid(row=2,column=1)
bt1=Button(f2,text="6",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(6),font=("arial",20,"bold")).grid(row=2,column=2)
bt1=Button(f2,text="-",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick("-"),font=("arial",20,"bold")).grid(row=2,column=3)

bt1=Button(f2,text="7",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(7),font=("arial",20,"bold")).grid(row=3,column=0)
bt1=Button(f2,text="8",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(8),font=("arial",20,"bold")).grid(row=3,column=1)
bt1=Button(f2,text="9",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(9),font=("arial",20,"bold")).grid(row=3,column=2)
bt1=Button(f2,text="*",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick("*"),font=("arial",20,"bold")).grid(row=3,column=3)

bt1=Button(f2,text="0",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick(0),font=("arial",20,"bold")).grid(row=4,column=0)
bt1=Button(f2,text="C",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClear("C"),font=("arial",20,"bold")).grid(row=4,column=1)
bt1=Button(f2,text="=",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnEquals("="),font=("arial",20,"bold")).grid(row=4,column=2)
bt1=Button(f2,text="/",padx=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClick("/"),font=("arial",20,"bold")).grid(row=4,column=3)





