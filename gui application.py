from tkinter import*
root=Tk()

label=Label(text="RESTAURANT MANAGEMENT SYSTEMS",fg="blue",font=("italian",60),bg="black")
root.geometry("1300x1300")
root.config(background="blue");
label2=Label(text="Tue July 19 11:20:14 2019",font=("calibri",19))
label.pack()
label2.pack(ipadx=10,ipady=10)

w1=Label(text="MANCHRIAN",fg="red",bg="black",font=("calibri",19))
w1.pack(anchor=W,padx=10)

a=Button(text="Total",bg="light blue",font=("calibri",10,"bold"))
a.pack(side=LEFT,padx=30,pady=10)
b=Button(text="Reset",bg="light blue",font=("calibri",10,"bold"))
b.pack(side=LEFT,ipadx=50,ipady=30)
c=Button(text="Quit",bg="light blue",font=("calibri",10,"bold"))
c.pack(side=LEFT,padx=80,pady=30)
c.config(width=10,height=5)
a.config(width=10,height=5)

