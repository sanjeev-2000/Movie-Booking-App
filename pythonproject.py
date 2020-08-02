from tkinter import *
import mysql.connector
def ty(name,time,seats,ticket):
    gui = Toplevel()
    gui.geometry("600x400")
    gui.configure(bg="light pink")
    frame1 = Frame(gui, width=600, height=500)
    img1 = PhotoImage(file='File Location Here\\qr.gif')
    label1 = Label(gui, image=img1)
    label1.place(x=0, y=50)
    label0 = Label(gui,text="THANK YOU FOR USING SHOW BOX",font="comicsansms 20 bold",fg="yellow",bg="light pink")
    label0.place(x=65,y=0)
    lab0 = Label(gui,text="SCAN THE ABOVE GIVEN QR CODE AT THE ENTRY OF THE CINEMA HALL!!!",font="comicsansms 12 bold",fg="RED",bg="light pink")
    lab0.place(x=0,y=370)
    lab1 = Label(gui, text="NAME:", font="comicsansms 15 bold", fg="blue", bg="light pink")
    lab1.place(x=280, y=70)
    lab2 = Label(gui, text="TIME:", font="comicsansms 15 bold", fg="blue", bg="light pink")
    lab2.place(x=280, y=140)
    lab3 = Label(gui, text="SEATS:", font="comicsansms 15 bold", fg="blue", bg="light pink")
    lab3.place(x=280, y=210)
    lab4 = Label(gui, text=name, font="comicsansms 15 bold", fg="red", bg="light pink")
    lab4.place(x=370, y=70)
    lab5 = Label(gui, text=time, font="comicsansms 15 bold", fg="red", bg="light pink")
    lab5.place(x=370, y=140)
    lab6 = Label(gui, text=seats, font="comicsansms 15 bold", fg="red", bg="light pink")
    lab6.place(x=370, y=210)
    lab7 = Label(gui, text="COST:", font="comicsansms 15 bold", fg="blue", bg="light pink")
    lab7.place(x=280, y=280)
    lab8 = Label(gui, text=ticket, font="comicsansms 15 bold", fg="red", bg="light pink")
    lab8.place(x=370, y=280)
    gui.mainloop()
def ckout1(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,time,name):
    print(v1)
    l2=[]
    if v1 == 0:
        pass
    else:
        l2.append("A1")
    if v2 == 0:
        pass
    else:
        l2.append("A2")
    if v3 == 0:
        pass
    else:
        l2.append("A3")
    if v4 == 0:
        pass
    else:
        l2.append("A4")
    if v5 == 0:
        pass
    else:
        l2.append("A5")
    if v6 == 0:
        pass
    else:
        l2.append("B1")
    if v7 == 0:
        pass
    else:
        l2.append("B2")
    if v8 == 0:
        pass
    else:
        l2.append("B3")
    if v9 == 0:
        pass
    else:
        l2.append("B4")
    if v10 == 0:
        pass
    else:
        l2.append("B5")
    if v11 == 0:
        pass
    else:
        l2.append("C1")
    if v12 == 0:
        pass
    else:
        l2.append("C2")
    if v13 == 0:
        pass
    else:
        l2.append("C3")
    if v14 == 0:
        pass
    else:
        l2.append("C4")
    if v15 == 0:
        pass
    else:
        l2.append("C5")
    seats=len(l2)
    cost1 = seats*130
    con = 45
    tot = cost1+con
    print(seats)
    newg = Toplevel()
    newg.geometry("600x600")
    newg.configure(bg="light green")
    frame1 = Frame(newg, width=600, height=600)
    label1 = Label(newg, text="TICKET SUMMARY", font="comicsansms 20 bold", fg="blue", bg="light green")
    label1.place(x=250, y=0)
    lab1 = Label(newg, text="NAME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab1.place(x=250, y=70)
    lab2 = Label(newg, text="TIME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab2.place(x=250, y=140)
    lab3 = Label(newg, text="SEATS:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab3.place(x=250, y=210)
    lab4 = Label(newg, text=name, font="comicsansms 15 bold", fg="red", bg="light green")
    lab4.place(x=350, y=70)
    lab5 = Label(newg, text=time, font="comicsansms 15 bold", fg="red", bg="light green")
    lab5.place(x=350, y=140)
    lab6 = Label(newg, text=l2, font="comicsansms 15 bold", fg="red", bg="light green")
    lab6.place(x=350, y=210)
    lab7 = Label(newg, text="COST PER TICKET:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab7.place(x=250, y=280)
    lab8 = Label(newg, text="130", font="comicsansms 15 bold", fg="red", bg="light green")
    lab8.place(x=450, y=280)
    lab9 = Label(newg, text="Cost Of tickets:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab9.place(x=100, y=400)
    lab12 = Label(newg, text=cost1, font="comicsansms 15 bold", fg="red", bg="light green")
    lab12.place(x=300, y=400)
    lab10 = Label(newg, text="Convenience Fee:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab10.place(x=100, y=440)
    lab13 = Label(newg, text=con, font="comicsansms 15 bold", fg="red", bg="light green")
    lab13.place(x=300, y=440)
    if(seats>2):
        dis = tot*20/100
        tot = tot-dis
        lab11 = Label(newg, text="Discount:", font="comicsansms 15 bold", fg="blue", bg="light green")
        lab11.place(x=100, y=480)
        lab16 = Label(newg, text=dis,font="comicsansms 15 bold", fg="red", bg="light green")
        lab16.place(x=300, y=480)
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=520)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=520)
    else:
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=480)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=480)
    img2 = PhotoImage(file='File Location Here\\capn.gif')
    label0 = Label(newg,image=img2)
    label0.place(x=0, y=0)
    btn1 = Button(newg, text="CONFIRM", font="comicsansms 15 bold", fg="red", bg="blue",command=lambda:[ty(name,time,l2,tot),newg.destroy()])
    btn1.place(x=450,y=550)
    button5 = Button(newg, text="BACK", command=newg.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=330, y=550, height=50, width=100)
    newg.mainloop()
def ckout2(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,time,name):
    l2=[]
    if v1 == 0:
        pass
    else:
        l2.append("A1")
    if v2 == 0:
        pass
    else:
        l2.append("A2")
    if v3 == 0:
        pass
    else:
        l2.append("A3")
    if v4 == 0:
        pass
    else:
        l2.append("A4")
    if v5 == 0:
        pass
    else:
        l2.append("A5")
    if v6 == 0:
        pass
    else:
        l2.append("B1")
    if v7 == 0:
        pass
    else:
        l2.append("B2")
    if v8 == 0:
        pass
    else:
        l2.append("B3")
    if v9 == 0:
        pass
    else:
        l2.append("B4")
    if v10 == 0:
        pass
    else:
        l2.append("B5")
    if v11 == 0:
        pass
    else:
        l2.append("C1")
    if v12 == 0:
        pass
    else:
        l2.append("C2")
    if v13 == 0:
        pass
    else:
        l2.append("C3")
    if v14 == 0:
        pass
    else:
        l2.append("C4")
    if v15 == 0:
        pass
    else:
        l2.append("C5")
    seats=len(l2)
    cost1 = seats*130
    con = 45
    tot = cost1+con
    print(seats)
    newg = Toplevel()
    newg.geometry("600x600")
    newg.configure(bg="light green")
    frame1 = Frame(newg, width=600, height=600)
    label1 = Label(newg, text="TICKET SUMMARY", font="comicsansms 20 bold", fg="blue", bg="light green")
    label1.place(x=250, y=0)
    lab1 = Label(newg, text="NAME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab1.place(x=250, y=70)
    lab2 = Label(newg, text="TIME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab2.place(x=250, y=140)
    lab3 = Label(newg, text="SEATS:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab3.place(x=250, y=210)
    lab4 = Label(newg, text=name, font="comicsansms 15 bold", fg="red", bg="light green")
    lab4.place(x=350, y=70)
    lab5 = Label(newg, text=time, font="comicsansms 15 bold", fg="red", bg="light green")
    lab5.place(x=350, y=140)
    lab6 = Label(newg, text=l2, font="comicsansms 15 bold", fg="red", bg="light green")
    lab6.place(x=350, y=210)
    lab7 = Label(newg, text="COST PER TICKET:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab7.place(x=250, y=280)
    lab8 = Label(newg, text="130", font="comicsansms 15 bold", fg="red", bg="light green")
    lab8.place(x=450, y=280)
    lab9 = Label(newg, text="Cost Of tickets:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab9.place(x=100, y=400)
    lab12 = Label(newg, text=cost1, font="comicsansms 15 bold", fg="red", bg="light green")
    lab12.place(x=300, y=400)
    lab10 = Label(newg, text="Convenience Fee:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab10.place(x=100, y=440)
    lab13 = Label(newg, text=con, font="comicsansms 15 bold", fg="red", bg="light green")
    lab13.place(x=300, y=440)
    if(seats>2):
        dis = tot*20/100
        tot = tot-dis
        lab11 = Label(newg, text="Discount:", font="comicsansms 15 bold", fg="blue", bg="light green")
        lab11.place(x=100, y=480)
        lab16 = Label(newg, text=dis,font="comicsansms 15 bold", fg="red", bg="light green")
        lab16.place(x=300, y=480)
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=520)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=520)
    else:
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=480)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=480)
    img2 = PhotoImage(file='File Location Here\\ave.gif')
    label0 = Label(newg,image=img2)
    label0.place(x=0, y=0)
    btn1 = Button(newg, text="CONFIRM", font="comicsansms 15 bold", fg="red", bg="blue",command=lambda:ty(name,time,l2,tot))
    btn1.place(x=450,y=550)
    button5 = Button(newg, text="BACK", command=newg.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=330, y=550, height=50, width=100)
    newg.mainloop()
def ckout3(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,time,name):
    l2=[]
    if v1 == 0:
        pass
    else:
        l2.append("A1")
    if v2 == 0:
        pass
    else:
        l2.append("A2")
    if v3 == 0:
        pass
    else:
        l2.append("A3")
    if v4 == 0:
        pass
    else:
        l2.append("A4")
    if v5 == 0:
        pass
    else:
        l2.append("A5")
    if v6 == 0:
        pass
    else:
        l2.append("B1")
    if v7 == 0:
        pass
    else:
        l2.append("B2")
    if v8 == 0:
        pass
    else:
        l2.append("B3")
    if v9 == 0:
        pass
    else:
        l2.append("B4")
    if v10 == 0:
        pass
    else:
        l2.append("B5")
    if v11 == 0:
        pass
    else:
        l2.append("C1")
    if v12 == 0:
        pass
    else:
        l2.append("C2")
    if v13 == 0:
        pass
    else:
        l2.append("C3")
    if v14 == 0:
        pass
    else:
        l2.append("C4")
    if v15 == 0:
        pass
    else:
        l2.append("C5")
    seats=len(l2)
    cost1 = seats*150
    con = 42
    tot = cost1+con
    print(seats)
    newg = Toplevel()
    newg.geometry("600x600")
    newg.configure(bg="light green")
    frame1 = Frame(newg, width=600, height=600)
    label1 = Label(newg, text="TICKET SUMMARY", font="comicsansms 20 bold", fg="blue", bg="light green")
    label1.place(x=250, y=0)
    lab1 = Label(newg, text="NAME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab1.place(x=250, y=70)
    lab2 = Label(newg, text="TIME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab2.place(x=250, y=140)
    lab3 = Label(newg, text="SEATS:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab3.place(x=250, y=210)
    lab4 = Label(newg, text=name, font="comicsansms 15 bold", fg="red", bg="light green")
    lab4.place(x=350, y=70)
    lab5 = Label(newg, text=time, font="comicsansms 15 bold", fg="red", bg="light green")
    lab5.place(x=350, y=140)
    lab6 = Label(newg, text=l2, font="comicsansms 15 bold", fg="red", bg="light green")
    lab6.place(x=350, y=210)
    lab7 = Label(newg, text="COST PER TICKET:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab7.place(x=250, y=280)
    lab8 = Label(newg, text="150", font="comicsansms 15 bold", fg="red", bg="light green")
    lab8.place(x=450, y=280)
    lab9 = Label(newg, text="Cost Of tickets:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab9.place(x=100, y=400)
    lab12 = Label(newg, text=cost1, font="comicsansms 15 bold", fg="red", bg="light green")
    lab12.place(x=300, y=400)
    lab10 = Label(newg, text="Convenience Fee:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab10.place(x=100, y=440)
    lab13 = Label(newg, text=con, font="comicsansms 15 bold", fg="red", bg="light green")
    lab13.place(x=300, y=440)
    if(seats>2):
        dis = tot*20/100
        tot = tot-dis
        lab11 = Label(newg, text="Discount:", font="comicsansms 15 bold", fg="blue", bg="light green")
        lab11.place(x=100, y=480)
        lab16 = Label(newg, text=dis,font="comicsansms 15 bold", fg="red", bg="light green")
        lab16.place(x=300, y=480)
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=520)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=520)
    else:
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=480)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=480)
    img2 = PhotoImage(file='File Location Here\\gb1.gif')
    label0 = Label(newg,image=img2)
    label0.place(x=0, y=0)
    btn1 = Button(newg, text="CONFIRM", font="comicsansms 15 bold", fg="red", bg="blue",command=lambda:ty(name,time,l2,tot))
    btn1.place(x=450,y=550)
    button5 = Button(newg, text="BACK", command=newg.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=330, y=550, height=50, width=100)
    newg.mainloop()
def ckout4(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,time,name):
    l2=[]
    if v1 == 0:
        pass
    else:
        l2.append("A1")
    if v2 == 0:
        pass
    else:
        l2.append("A2")
    if v3 == 0:
        pass
    else:
        l2.append("A3")
    if v4 == 0:
        pass
    else:
        l2.append("A4")
    if v5 == 0:
        pass
    else:
        l2.append("A5")
    if v6 == 0:
        pass
    else:
        l2.append("B1")
    if v7 == 0:
        pass
    else:
        l2.append("B2")
    if v8 == 0:
        pass
    else:
        l2.append("B3")
    if v9 == 0:
        pass
    else:
        l2.append("B4")
    if v10 == 0:
        pass
    else:
        l2.append("B5")
    if v11 == 0:
        pass
    else:
        l2.append("C1")
    if v12 == 0:
        pass
    else:
        l2.append("C2")
    if v13 == 0:
        pass
    else:
        l2.append("C3")
    if v14 == 0:
        pass
    else:
        l2.append("C4")
    if v15 == 0:
        pass
    else:
        l2.append("C5")
    seats=len(l2)
    cost1 = seats*150
    con = 42
    tot = cost1+con
    print(seats)
    newg = Toplevel()
    newg.geometry("600x600")
    newg.configure(bg="light green")
    frame1 = Frame(newg, width=600, height=600)
    label1 = Label(newg, text="TICKET SUMMARY", font="comicsansms 20 bold", fg="blue", bg="light green")
    label1.place(x=250, y=0)
    lab1 = Label(newg, text="NAME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab1.place(x=250, y=70)
    lab2 = Label(newg, text="TIME:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab2.place(x=250, y=140)
    lab3 = Label(newg, text="SEATS:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab3.place(x=250, y=210)
    lab4 = Label(newg, text=name, font="comicsansms 15 bold", fg="red", bg="light green")
    lab4.place(x=350, y=70)
    lab5 = Label(newg, text=time, font="comicsansms 15 bold", fg="red", bg="light green")
    lab5.place(x=350, y=140)
    lab6 = Label(newg, text=l2, font="comicsansms 15 bold", fg="red", bg="light green")
    lab6.place(x=350, y=210)
    lab7 = Label(newg, text="COST PER TICKET:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab7.place(x=250, y=280)
    lab8 = Label(newg, text="150", font="comicsansms 15 bold", fg="red", bg="light green")
    lab8.place(x=450, y=280)
    lab9 = Label(newg, text="Cost Of tickets:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab9.place(x=100, y=400)
    lab12 = Label(newg, text=cost1, font="comicsansms 15 bold", fg="red", bg="light green")
    lab12.place(x=300, y=400)
    lab10 = Label(newg, text="Convenience Fee:", font="comicsansms 15 bold", fg="blue", bg="light green")
    lab10.place(x=100, y=440)
    lab13 = Label(newg, text=con, font="comicsansms 15 bold", fg="red", bg="light green")
    lab13.place(x=300, y=440)
    if(seats>2):
        dis = tot*20/100
        tot = tot-dis
        lab11 = Label(newg, text="Discount:", font="comicsansms 15 bold", fg="blue", bg="light green")
        lab11.place(x=100, y=480)
        lab16 = Label(newg, text=dis,font="comicsansms 15 bold", fg="red", bg="light green")
        lab16.place(x=300, y=480)
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=520)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=520)
    else:
        lab14 = Label(newg, text="TOTAL COST:", font="comicsansms 15 bold", fg="red", bg="light green")
        lab14.place(x=100, y=480)
        lab15 = Label(newg, text=tot, font="comicsansms 15 bold", fg="red", bg="light green")
        lab15.place(x=300, y=480)
    img2 = PhotoImage(file='File Location Here\\hb1.gif')
    label0 = Label(newg,image=img2)
    label0.place(x=0, y=0)
    btn1 = Button(newg, text="CONFIRM", font="comicsansms 15 bold", fg="red", bg="blue",command=lambda:ty(name,time,l2,tot))
    btn1.place(x=450,y=550)
    button5 = Button(newg, text="BACK", command=newg.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=330, y=550, height=50, width=100)
    newg.mainloop()
def seats4(time,name):
    new = Toplevel()
    new.geometry("600x600")
    new.configure(bg="sky blue")
    frame1 = Frame(new,width=600,height=600)
    label1 = Label(new,text="SELECT SEATS",font="comicsansms 20 bold",fg="red",bg="sky blue")
    label1.place(x=200,y=0)
    label2 = Label(new,text="_____________________________________________________",bg="sky blue")
    label3 = Label(new,text="**********SCREEN THIS SIDE**********",bg="sky blue")
    label2.place(x=280,y=400)
    label3.place(x=305,y=420)
    lab4 = Label(new,text="*discount applicable for selection of 3 or more seats*",font="comicsansms 10 bold",bg="sky blue",fg="red")
    lab4.place(x=2,y=580)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    Checkbutton(new, text="A1",  variable=var1,bg="sky blue",font="comicsansms 15 bold") .place(x=0, y=100)
    Checkbutton(new, text="A2",  variable=var2, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=130)
    Checkbutton(new, text="A3",  variable=var3, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=160)
    Checkbutton(new, text="A4",  variable=var4, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=190)
    Checkbutton(new, text="A5",  variable=var5, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=220)
    Checkbutton(new, text="B1",  variable=var6, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=250)
    Checkbutton(new, text="B2",  variable=var7, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=280)
    Checkbutton(new, text="B3",  variable=var8, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=310)
    Checkbutton(new, text="B4",  variable=var9, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=340)
    Checkbutton(new, text="B5", variable=var10, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=370)
    Checkbutton(new, text="C1", variable=var11, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=400)
    Checkbutton(new, text="C2", variable=var12, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=430)
    Checkbutton(new, text="C3", variable=var13, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=460)
    Checkbutton(new, text="C4", variable=var14, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=490)
    Checkbutton(new, text="C5", variable=var15, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=520)
    btn1 = Button(new, text="A1",font="comicsansms 10 bold")
    btn2 = Button(new, text="A2",font="comicsansms 10 bold")
    btn3 = Button(new, text="A3",font="comicsansms 10 bold")
    btn4 = Button(new, text="A4",font="comicsansms 10 bold")
    btn5 = Button(new, text="A5", font="comicsansms 10 bold")
    #new row
    btn6 = Button(new, text="B1", font="comicsansms 10 bold")
    btn7 = Button(new, text="B2", font="comicsansms 10 bold")
    btn8 = Button(new, text="B3", font="comicsansms 10 bold")
    btn9 = Button(new, text="B4", font="comicsansms 10 bold")
    btn10 = Button(new, text="B5", font="comicsansms 10 bold")
    #new row
    btn11 = Button(new, text="C1", font="comicsansms 10 bold")
    btn12 = Button(new, text="C2", font="comicsansms 10 bold")
    btn13 = Button(new, text="C3", font="comicsansms 10 bold")
    btn14 = Button(new, text="C4", font="comicsansms 10 bold")
    btn15 = Button(new, text="C5", font="comicsansms 10 bold")
    btn1.place(x=300, y=100)
    btn2.place(x=350, y=100)
    btn3.place(x=400, y=100)
    btn4.place(x=450, y=100)
    btn5.place(x=500, y=100)
    #new row
    btn6.place(x=300, y=200)
    btn7.place(x=350, y=200)
    btn8.place(x=400, y=200)
    btn9.place(x=450, y=200)
    btn10.place(x=500, y=200)
    #new row
    btn11.place(x=300, y=300)
    btn12.place(x=350, y=300)
    btn13.place(x=400, y=300)
    btn14.place(x=450, y=300)
    btn15.place(x=500, y=300)
    button1 = Button(new, text="CONTINUE", font="comicsansms 15 bold", fg="red", bg="light green",command=lambda:ckout4(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),time,name))
    button1.place(x=300, y=500)
    button5 = Button(new, text="BACK", command=new.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=470, y=565, height=30, width=100)
    button6 = Button(new, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=360, y=565, height=30, width=100)
    print(time,name)
    new.mainloop()
def seats3(time,name):
    new = Toplevel()
    new.geometry("600x600")
    new.configure(bg="sky blue")
    frame1 = Frame(new,width=600,height=600)
    label1 = Label(new,text="SELECT SEATS",font="comicsansms 20 bold",fg="red",bg="sky blue")
    label1.place(x=200,y=0)
    label2 = Label(new,text="_____________________________________________________",bg="sky blue")
    label3 = Label(new,text="**********SCREEN THIS SIDE**********",bg="sky blue")
    label2.place(x=280,y=400)
    label3.place(x=305,y=420)
    lab4 = Label(new,text="*discount applicable for selection of 3 or more seats*",font="comicsansms 10 bold",bg="sky blue",fg="red")
    lab4.place(x=2,y=580)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    Checkbutton(new, text="A1",  variable=var1,bg="sky blue",font="comicsansms 15 bold") .place(x=0, y=100)
    Checkbutton(new, text="A2",  variable=var2, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=130)
    Checkbutton(new, text="A3",  variable=var3, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=160)
    Checkbutton(new, text="A4",  variable=var4, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=190)
    Checkbutton(new, text="A5",  variable=var5, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=220)
    Checkbutton(new, text="B1",  variable=var6, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=250)
    Checkbutton(new, text="B2",  variable=var7, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=280)
    Checkbutton(new, text="B3",  variable=var8, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=310)
    Checkbutton(new, text="B4",  variable=var9, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=340)
    Checkbutton(new, text="B5", variable=var10, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=370)
    Checkbutton(new, text="C1", variable=var11, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=400)
    Checkbutton(new, text="C2", variable=var12, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=430)
    Checkbutton(new, text="C3", variable=var13, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=460)
    Checkbutton(new, text="C4", variable=var14, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=490)
    Checkbutton(new, text="C5", variable=var15, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=520)
    btn1 = Button(new, text="A1",font="comicsansms 10 bold")
    btn2 = Button(new, text="A2",font="comicsansms 10 bold")
    btn3 = Button(new, text="A3",font="comicsansms 10 bold")
    btn4 = Button(new, text="A4",font="comicsansms 10 bold")
    btn5 = Button(new, text="A5", font="comicsansms 10 bold")
    #new row
    btn6 = Button(new, text="B1", font="comicsansms 10 bold")
    btn7 = Button(new, text="B2", font="comicsansms 10 bold")
    btn8 = Button(new, text="B3", font="comicsansms 10 bold")
    btn9 = Button(new, text="B4", font="comicsansms 10 bold")
    btn10 = Button(new, text="B5", font="comicsansms 10 bold")
    #new row
    btn11 = Button(new, text="C1", font="comicsansms 10 bold")
    btn12 = Button(new, text="C2", font="comicsansms 10 bold")
    btn13 = Button(new, text="C3", font="comicsansms 10 bold")
    btn14 = Button(new, text="C4", font="comicsansms 10 bold")
    btn15 = Button(new, text="C5", font="comicsansms 10 bold")
    btn1.place(x=300, y=100)
    btn2.place(x=350, y=100)
    btn3.place(x=400, y=100)
    btn4.place(x=450, y=100)
    btn5.place(x=500, y=100)
    #new row
    btn6.place(x=300, y=200)
    btn7.place(x=350, y=200)
    btn8.place(x=400, y=200)
    btn9.place(x=450, y=200)
    btn10.place(x=500, y=200)
    #new row
    btn11.place(x=300, y=300)
    btn12.place(x=350, y=300)
    btn13.place(x=400, y=300)
    btn14.place(x=450, y=300)
    btn15.place(x=500, y=300)
    button1 = Button(new, text="CONTINUE", font="comicsansms 15 bold", fg="red", bg="light green",command=lambda:ckout3(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),time,name))
    button1.place(x=300, y=500)
    print(time,name)
    button5 = Button(new, text="BACK", command=new.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=470, y=565, height=30, width=100)
    button6 = Button(new, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=360, y=565, height=30, width=100)
    new.mainloop()
def seats2(time,name):
    new = Toplevel()
    new.geometry("600x600")
    new.configure(bg="sky blue")
    label1 = Label(new,text="SELECT SEATS",font="comicsansms 20 bold",fg="red",bg="sky blue")
    label1.place(x=200,y=0)
    label2 = Label(new,text="_____________________________________________________",bg="sky blue")
    label3 = Label(new,text="**********SCREEN THIS SIDE**********",bg="sky blue")
    label2.place(x=280,y=400)
    label3.place(x=305,y=420)
    lab4 = Label(new,text="*discount applicable for selection of 3 or more seats*",font="comicsansms 10 bold",bg="sky blue",fg="red")
    lab4.place(x=2,y=580)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    Checkbutton(new, text="A1",  variable=var1,bg="sky blue",font="comicsansms 15 bold") .place(x=0, y=100)
    Checkbutton(new, text="A2",  variable=var2, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=130)
    Checkbutton(new, text="A3",  variable=var3, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=160)
    Checkbutton(new, text="A4",  variable=var4, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=190)
    Checkbutton(new, text="A5",  variable=var5, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=220)
    Checkbutton(new, text="B1",  variable=var6, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=250)
    Checkbutton(new, text="B2",  variable=var7, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=280)
    Checkbutton(new, text="B3",  variable=var8, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=310)
    Checkbutton(new, text="B4",  variable=var9, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=340)
    Checkbutton(new, text="B5", variable=var10, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=370)
    Checkbutton(new, text="C1", variable=var11, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=400)
    Checkbutton(new, text="C2", variable=var12, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=430)
    Checkbutton(new, text="C3", variable=var13, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=460)
    Checkbutton(new, text="C4", variable=var14, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=490)
    Checkbutton(new, text="C5", variable=var15, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=520)
    btn1 = Button(new, text="A1",font="comicsansms 10 bold")
    btn2 = Button(new, text="A2",font="comicsansms 10 bold")
    btn3 = Button(new, text="A3",font="comicsansms 10 bold")
    btn4 = Button(new, text="A4",font="comicsansms 10 bold")
    btn5 = Button(new, text="A5", font="comicsansms 10 bold")
    #new row
    btn6 = Button(new, text="B1", font="comicsansms 10 bold")
    btn7 = Button(new, text="B2", font="comicsansms 10 bold")
    btn8 = Button(new, text="B3", font="comicsansms 10 bold")
    btn9 = Button(new, text="B4", font="comicsansms 10 bold")
    btn10 = Button(new, text="B5", font="comicsansms 10 bold")
    #new row
    btn11 = Button(new, text="C1", font="comicsansms 10 bold")
    btn12 = Button(new, text="C2", font="comicsansms 10 bold")
    btn13 = Button(new, text="C3", font="comicsansms 10 bold")
    btn14 = Button(new, text="C4", font="comicsansms 10 bold")
    btn15 = Button(new, text="C5", font="comicsansms 10 bold")
    btn1.place(x=300, y=100)
    btn2.place(x=350, y=100)
    btn3.place(x=400, y=100)
    btn4.place(x=450, y=100)
    btn5.place(x=500, y=100)
    #new row
    btn6.place(x=300, y=200)
    btn7.place(x=350, y=200)
    btn8.place(x=400, y=200)
    btn9.place(x=450, y=200)
    btn10.place(x=500, y=200)
    #new row
    btn11.place(x=300, y=300)
    btn12.place(x=350, y=300)
    btn13.place(x=400, y=300)
    btn14.place(x=450, y=300)
    btn15.place(x=500, y=300)
    button1 = Button(new, text="CONTINUE", font="comicsansms 15 bold", fg="red", bg="light green",command=lambda:ckout2(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),time,name))
    button1.place(x=300, y=500)
    print(time,name)
    button5 = Button(new, text="BACK", command=new.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=470, y=565, height=30, width=100)
    button6 = Button(new, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=360, y=565, height=30, width=100)
    new.mainloop()
def seats1(time,name):
    new = Toplevel()
    new.geometry("600x600")
    new.configure(bg="sky blue")
    frame1 = Frame(new,width=600,height=600)
    label1 = Label(new,text="SELECT SEATS",font="comicsansms 20 bold",fg="red",bg="sky blue")
    label1.place(x=200,y=0)
    label2 = Label(new,text="_____________________________________________________",bg="sky blue")
    label3 = Label(new,text="**********SCREEN THIS SIDE**********",bg="sky blue")
    label2.place(x=280,y=400)
    label3.place(x=305,y=420)
    lab4 = Label(new,text="*discount applicable for selection of 3 or more seats*",font="comicsansms 10 bold",bg="sky blue",fg="red")
    lab4.place(x=2,y=580)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    Checkbutton(new, text="A1",  variable=var1,bg="sky blue",font="comicsansms 15 bold") .place(x=0, y=100)
    Checkbutton(new, text="A2",  variable=var2, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=130)
    Checkbutton(new, text="A3",  variable=var3, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=160)
    Checkbutton(new, text="A4",  variable=var4, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=190)
    Checkbutton(new, text="A5",  variable=var5, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=220)
    Checkbutton(new, text="B1",  variable=var6, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=250)
    Checkbutton(new, text="B2",  variable=var7, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=280)
    Checkbutton(new, text="B3",  variable=var8, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=310)
    Checkbutton(new, text="B4",  variable=var9, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=340)
    Checkbutton(new, text="B5", variable=var10, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=370)
    Checkbutton(new, text="C1", variable=var11, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=400)
    Checkbutton(new, text="C2", variable=var12, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=430)
    Checkbutton(new, text="C3", variable=var13, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=460)
    Checkbutton(new, text="C4", variable=var14, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=490)
    Checkbutton(new, text="C5", variable=var15, bg="sky blue",font="comicsansms 15 bold").place(x=0, y=520)
    btn1 = Button(new, text="A1",font="comicsansms 10 bold")
    btn2 = Button(new, text="A2",font="comicsansms 10 bold")
    btn3 = Button(new, text="A3",font="comicsansms 10 bold")
    btn4 = Button(new, text="A4",font="comicsansms 10 bold")
    btn5 = Button(new, text="A5", font="comicsansms 10 bold")
    #new row
    btn6 = Button(new, text="B1", font="comicsansms 10 bold")
    btn7 = Button(new, text="B2", font="comicsansms 10 bold")
    btn8 = Button(new, text="B3", font="comicsansms 10 bold")
    btn9 = Button(new, text="B4", font="comicsansms 10 bold")
    btn10 = Button(new, text="B5", font="comicsansms 10 bold")
    #new row
    btn11 = Button(new, text="C1", font="comicsansms 10 bold")
    btn12 = Button(new, text="C2", font="comicsansms 10 bold")
    btn13 = Button(new, text="C3", font="comicsansms 10 bold")
    btn14 = Button(new, text="C4", font="comicsansms 10 bold")
    btn15 = Button(new, text="C5", font="comicsansms 10 bold")
    btn1.place(x=300, y=100)
    btn2.place(x=350, y=100)
    btn3.place(x=400, y=100)
    btn4.place(x=450, y=100)
    btn5.place(x=500, y=100)
    #new row
    btn6.place(x=300, y=200)
    btn7.place(x=350, y=200)
    btn8.place(x=400, y=200)
    btn9.place(x=450, y=200)
    btn10.place(x=500, y=200)
    #new row
    btn11.place(x=300, y=300)
    btn12.place(x=350, y=300)
    btn13.place(x=400, y=300)
    btn14.place(x=450, y=300)
    btn15.place(x=500, y=300)
    button1 = Button(new, text="CONTINUE", font="comicsansms 15 bold", fg="red", bg="light green",command=lambda:ckout1(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),time,name))
    button1.place(x=300, y=500)
    button5 = Button(new, text="BACK", command=new.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=470, y=565, height=30, width=100)
    button6 = Button(new, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=360, y=565, height=30, width=100)
    print(time,name)
    new.mainloop()
def cap():
    top = Toplevel()
    top.geometry("600x500")
    top.configure(bg="yellow")
    frame2 = Frame(top, width=400, height=400)
    img1 = PhotoImage(file='File Location Here\\capin.gif')
    label1 = Label(top, image=img1)
    label2 = Label(top, text="CAPTAIN MARVEL", font="comicsansms 15 bold",fg="red",bg="yellow")
    label3 = Label(top, text="REVIEWS:", font="comicsansms 8 bold", fg="blue",bg="yellow")
    label4 = Label(top, text="SHOW TIMINGS:", font="comicsansms 12 bold", fg="red",bg="yellow")
    label5 = Label(top, text="RATING: 8/10", font="comicsansms 15 bold", fg="blue",bg="yellow")
    btn1 = Button(top, text="10 am",fg="blue",command=lambda: seats1("10 am","CAPTAIN MARVEL"))
    btn2 = Button(top, text="1 pm", fg="blue",command=lambda: seats1("1 pm","CAPTAIN MARVEL"))
    btn3 = Button(top, text="5 pm", fg="blue",command=lambda: seats1("5 pm","CAPTAIN MARVEL"))
    btn4 = Button(top, text="9 pm", fg="blue",command=lambda: seats1("p pm","CAPTAIN MARVEL"))
    label1.place(x=0 , y=0)
    label4.place(x=0, y=350)
    label0 = Label(top, text="MOVIE DESCRIPTION:", font="comicsansms 8 bold",fg="blue",bg="yellow")
    l2 = Label(top,text="Captain Marvel is a 2019 American superhero film",bg="yellow")
    l3 = Label(top,text="based on the Marvel Comics character Carol Danvers.",bg="yellow")
    l4 = Label(top, text="Produced by Marvel Studios and distributed by Walt",bg="yellow")
    l5 = Label(top,text="Disney Studios Motion Pictures, it is the twenty-first",bg="yellow")
    l6 = Label(top,text="film in the Marvel Cinematic Universe (MCU).",bg="yellow")
    la2 = Label(top, text="The expectations are at an all-time high with Marvel’s",bg="yellow")
    la3 = Label(top, text= " very first female superhero movie. Captain Marvel has ",bg="yellow")
    la4 = Label(top, text="Brie Larson playing the lead role of the half-human, ",bg="yellow")
    la5 = Label(top, text="half-Kree warrior hero.Also Samuel L Jackson was as",bg="yellow")
    la6 = Label(top, text=" always...Awesome",bg="yellow")
    label2.place(x=275,y=0)
    label0.place(x=275,y=30)
    label3.place(x=275,y=160)
    label5.place(x=10,y=300)
    l2.place(x=275,y=50)
    l3.place(x=275, y=65)
    l4.place(x=275, y=80)
    l5.place(x=275, y=95)
    l6.place(x=275, y=110)
    la2.place(x=275, y=180)
    la3.place(x=275, y=200)
    la4.place(x=275, y=220)
    la5.place(x=275, y=240)
    la6.place(x=275, y=260)
    btn1.place(x=50, y=400)
    btn2.place(x=150, y=400)
    btn3.place(x=250, y=400)
    btn4.place(x=350, y=400)
    button5 = Button(top, text="BACK", command=top.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=460, y=450, height=30, width=100)
    button6 = Button(top, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=350, y=450, height=30, width=100)
    top.mainloop()
def endgame():
    top = Toplevel()
    top.geometry("600x600")
    top.configure(bg="yellow")
    frame2 = Frame(top, width=600, height=600)
    img1 = PhotoImage(file='File Location Here\\1.gif')
    label1 = Label(top, image=img1)
    label2 = Label(top, text="AVENGERS:END GAME", font="comicsansms 15 bold", fg="red", bg="yellow")
    label3 = Label(top, text="REVIEWS:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    label4 = Label(top, text="SHOW TIMINGS:", font="comicsansms 12 bold", fg="red", bg="yellow")
    label5 = Label(top, text="RATING:--", font="comicsansms 15 bold", fg="blue", bg="yellow")
    btn1 = Button(top, text="10 am", fg="blue",command=lambda: seats2("10 am","AVENGERS:END GAME"))
    btn2 = Button(top, text="1 pm", fg="blue",command=lambda: seats2("1 pm","AVENGERS:END GAME"))
    btn3 = Button(top, text="5 pm", fg="blue",command=lambda: seats2("5 pm","AVENGERS:END GAME"))
    btn4 = Button(top, text="9 pm", fg="blue",command=lambda: seats2("9 pm","AVENGERS:END GAME"))
    label1.place(x=0, y=0)
    label4.place(x=0, y=450)
    label0 = Label(top, text="MOVIE DESCRIPTION:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    l2 = Label(top, text="Avengers Endgame is an upcoming American superhero",bg="yellow")
    l3 = Label(top, text="film based on the Marvel Comics superhero team the", bg="yellow")
    l4 = Label(top, text="Avengers produced by Marvel Studios and set for", bg="yellow")
    l5 = Label(top, text="distribution by Walt Disney Studios Motion", bg="yellow")
    l6 = Label(top, text="Pictures. It is a direct sequel to avengers", bg="yellow")
    l7 = Label(top, text="Infinity war released in 2018", bg="yellow")
    la2 = Label(top, text="No Reviews available:(", bg="yellow")
    label2.place(x=295, y=0)
    label0.place(x=295, y=30)
    label3.place(x=295, y=160)
    label5.place(x=0, y=375)
    l2.place(x=295, y=50)
    l3.place(x=295, y=65)
    l4.place(x=295, y=80)
    l5.place(x=295, y=95)
    l6.place(x=295, y=110)
    l7.place(x=295, y=125)
    la2.place(x=295, y=180)
    btn1.place(x=50, y=500)
    btn2.place(x=150, y=500)
    btn3.place(x=250, y=500)
    btn4.place(x=350, y=500)
    button5 = Button(top, text="BACK", command=top.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=460, y=550, height=30, width=100)
    button6 = Button(top, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=350, y=550, height=30, width=100)
    top.mainloop()
def Gb():
    top = Toplevel()
    top.geometry("600x500")
    top.configure(bg="yellow")
    frame2 = Frame(top, width=400, height=400)
    img1 = PhotoImage(file='File Location Here\\gully.gif')
    label1 = Label(top, image=img1)
    label2 = Label(top, text="GULLY BOY", font="comicsansms 15 bold", fg="red", bg="yellow")
    label3 = Label(top, text="REVIEWS:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    label4 = Label(top, text="SHOW TIMINGS:", font="comicsansms 12 bold", fg="red", bg="yellow")
    label5 = Label(top, text="RATING: 9/10", font="comicsansms 15 bold", fg="blue", bg="yellow")
    btn1 = Button(top, text="10 am", fg="blue",command=lambda: seats3("10 am","GULLY BOY"))
    btn2 = Button(top, text="1 pm", fg="blue",command=lambda: seats3("1 pm","GULLY BOY"))
    btn3 = Button(top, text="5 pm", fg="blue",command=lambda: seats3("5 pm","GULLY BOY"))
    btn4 = Button(top, text="9 pm", fg="blue",command=lambda: seats3("9 pm","GULLY BOY"))
    label1.place(x=0, y=0)
    label4.place(x=0, y=350)
    label0 = Label(top, text="MOVIE DESCRIPTION:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    l2 = Label(top, text="Gully Boy is a 2019 Indian Hindi-language musical drama film It stars.",bg="yellow")
    l3 = Label(top, text="Ranveer Singh and Alia Bhatt, and features Kalki Koechlin, Siddhant",bg="yellow")
    l4 = Label(top, text="Chaturvedi and Vijay Raaz in supporting roles. Inspired by the", bg="yellow")
    l5 = Label(top, text="lives of Indian street rappers Divine and Naezy,the film is story  ", bg="yellow")
    l6 = Label(top, text="about an aspiring street rapper from the Dharavi slums of Mumbai.", bg="yellow")
    la2 = Label(top, text="An entertaining and engaging look at the world of Indian rappers.",bg="yellow")
    la3 = Label(top, text="Ranveer’s restrained performance as Murad and as a man who has", bg="yellow")
    la4 = Label(top, text="found his freedom as Gully Boy is moving. The film has a soul", bg="yellow")
    la5 = Label(top, text="with a satisfying story arch.", bg="yellow")
    la6 = Label(top, text="In mumbai ki boli....Picture bohot hard hai bantai.", bg="yellow")
    label2.place(x=275, y=0)
    label0.place(x=230, y=30)
    label3.place(x=230, y=160)
    label5.place(x=0, y=300)
    l2.place(x=230, y=50)
    l3.place(x=230, y=65)
    l4.place(x=230, y=80)
    l5.place(x=230, y=95)
    l6.place(x=230, y=110)
    la2.place(x=230, y=180)
    la3.place(x=230, y=200)
    la4.place(x=230, y=220)
    la5.place(x=230, y=240)
    la6.place(x=230, y=260)
    btn1.place(x=50, y=400)
    btn2.place(x=150, y=400)
    btn3.place(x=250, y=400)
    btn4.place(x=350, y=400)
    button5 = Button(top, text="BACK", command=top.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=460, y=450, height=30, width=100)
    button6 = Button(top, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=350, y=450, height=30, width=100)
    top.mainloop()
def Hb():
    top = Toplevel()
    top.geometry("600x500")
    top.configure(bg="yellow")
    frame2 = Frame(top, width=400, height=400)
    img1 = PhotoImage(file='File Location Here\\hell.gif')
    label1 = Label(top, image=img1)
    label2 = Label(top, text="HELL BOY ", font="comicsansms 15 bold", fg="red", bg="yellow")
    label3 = Label(top, text="REVIEWS:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    label4 = Label(top, text="SHOW TIMINGS:", font="comicsansms 12 bold", fg="red", bg="yellow")
    label5 = Label(top, text="RATING:-", font="comicsansms 15 bold", fg="blue", bg="yellow")
    btn1 = Button(top, text="10 am", fg="blue",command=lambda: seats4("10 am","HELL BOY"))
    btn2 = Button(top, text="1 pm", fg="blue",command=lambda: seats4("1 pm","HELL BOY"))
    btn3 = Button(top, text="5 pm", fg="blue",command=lambda: seats4("5 pm","HELL BOY"))
    btn4 = Button(top, text="9 pm", fg="blue",command=lambda: seats4("9 pm","HELL BOY"))
    label1.place(x=0, y=0)
    label4.place(x=0, y=350)
    label0 = Label(top, text="MOVIE DESCRIPTION:", font="comicsansms 8 bold", fg="blue", bg="yellow")
    l2 = Label(top, text="Hellboy is an upcoming American supernatural superhero film based", bg="yellow")
    l3 = Label(top, text=" on the Dark Horse Comics character Hellboy.", bg="yellow")
    l4 = Label(top, text="The film is directed by Neil Marshall and stars David Harbour in the", bg="yellow")
    l5 = Label(top, text="title role.The film also features Milla Jovovich, Ian McShane.", bg="yellow")
    la2 = Label(top, text="No reviews are available", bg="yellow")
    label2.place(x=230, y=0)
    label0.place(x=230, y=30)
    label3.place(x=230, y=160)
    label5.place(x=10, y=300)
    l2.place(x=230, y=50)
    l3.place(x=230, y=67)
    l4.place(x=230, y=83)
    l5.place(x=230, y=100)
    la2.place(x=230, y=180)
    btn1.place(x=50, y=400)
    btn2.place(x=150, y=400)
    btn3.place(x=250, y=400)
    btn4.place(x=350, y=400)
    button5 = Button(top, text="BACK", command=top.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button5.place(x=460, y=450, height=30, width=100)
    button6 = Button(top, text="EXIT", command=root.destroy, font="comicsansms 12 bold", bg="red", fg="white")
    button6.place(x=350, y=450, height=30, width=100)
    top.mainloop()
def mtdb(name,type,des):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="password1",database="newmovie")
    my_cursor = mydb.cursor()
    print(mydb)
    sqlstuff = "insert into movieinfo (name, type, description) values(%s, %s, %s)"
    rec = (name, type, des)
    my_cursor.execute(sqlstuff,rec)
    mydb.commit()
    print("values inserted!")
    new = Toplevel()
    new.geometry("350x200")
    new.configure(bg="light green")
    lab1 = Label(new,text="MOVIE ADDED SUCCESSFULLY!!!",bg="light green",fg="red",font="comicsansms 12 bold")
    lab1.place(x=20,y=50)
    btn2 = Button(new, text="OK", bg="yellow", fg="red", font="comicsansms 12 bold",command=new.destroy)
    btn2.place(x=100, y=100)
    new.mainloop()
def newmovie(id,password):
    if((id=="123")&(password=="123")):


        nm = Toplevel()
        nm.geometry("600x400")
        nm.configure(bg="light green")
        lab1 = Label(nm, text="ADD A NEW MOVIE AS UPCOMING MOVIES!!", font="comicsansms 12 bold", bg="light green", fg="red")
        lab1.place(x=0, y=5)
        lab2 = Label(nm, text="ENTER MOVIE NAME:", bg="light green", fg="dark blue", font="comicsansms 12 bold")
        lab3 = Label(nm, text="ENTER MOVIE TYPE:", bg="light green", fg="dark blue", font="comicsansms 12 bold")
        lab2.place(x=50, y=50)
        lab3.place(x=50, y=100)
        lab4 = Label(nm, text=" MOVIE CAST:", bg="light green", fg="dark blue", font="comicsansms 12 bold")
        lab4.place(x=50, y=160)
        e1 = Entry(nm, bg="white", fg="blue")
        e1.place(x=350, y=52)
        e2 = Entry(nm, bg="white", fg="blue")
        e2.place(x=250, y=162,width=300)
        e4 = Entry(nm, bg="white", fg="blue")
        e4.place(x=350, y=100)
        btn1 = Button(nm, text="ADD MOVIE", bg="yellow", fg="black", font="comicsansms 12 bold",command=lambda:mtdb(e1.get(),e4.get(),e2.get()))
        btn1.place(x=150, y=300,height=50,width=150)
        btn2 = Button(nm, text="BACK", bg="red", fg="white", font="comicsansms 12 bold",command=nm.destroy)
        btn2.place(x=320, y=300, height=50, width=150)
        nm.mainloop()
    else:
        new = Toplevel()
        new.geometry("350x200")
        new.configure(bg="light green")
        lab1 = Label(new, text="INCORRECT ID OR PASSWORD!!!", bg="light green", fg="red", font="comicsansms 12 bold")
        lab1.place(x=20, y=50)
        btn2 = Button(new, text="OK", bg="yellow", fg="red", font="comicsansms 12 bold", command=new.destroy)
        btn2.place(x=100, y=100)
        new.mainloop()
def login():
    new = Toplevel()
    new.geometry("500x200")
    new.configure(bg="light blue")
    lab2 = Label(new, text="ENTER ID:", bg="light blue", fg="green", font="comicsansms 12 bold")
    lab3 = Label(new, text="ENTER PASSWORD:", bg="light blue", fg="green", font="comicsansms 12 bold")
    lab2.place(x=50, y=50)
    lab3.place(x=50, y=100)
    e1 = Entry(new, bg="white", fg="red")
    e1.place(x=200, y=52)
    e2 = Entry(new, bg="white", fg="red")
    e2.place(x=250, y=102)
    btn1 = Button(new, text="LOGIN", bg="orange", fg="blue", font="comicsansms 8 bold", command=lambda:newmovie(e1.get(),e2.get()))
    btn1.place(x=150, y=150)
    btn2 = Button(new, text="BACK", bg="orange", fg="blue", font="comicsansms 8 bold",command=new.destroy)
    btn2.place(x=200, y=150)
    new.mainloop()
def upcoming():
    mov_det={}
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="password1", database="newmovie")
    my_cursor = mydb.cursor()
    print(mydb)
    my_cursor.execute("select * from movieinfo")
    for i in my_cursor:
        mov_det.update({i[0]:[i[1], i[2]]})
    #print(mov_det)
    new = Toplevel()
    new.geometry("800x800")
    new.configure(bg="light green")
    label1 = Label(new, text="UPCOMING MOVIES!!!", font="comicsansms 12 bold", fg="red", bg='light green')
    label1.place(x=0, y=0)
    label2 = Label(new, text="MOVIE NAME", font="comicsansms 12 bold", fg="red", bg='light green')
    label2.place(x=0, y=50)
    label3 = Label(new, text="MOVIE TYPE", font="comicsansms 12 bold", fg="red", bg='light green')
    label3.place(x=200, y=50)
    label4 = Label(new, text="CAST", font="comicsansms 12 bold", fg="red", bg='light green')
    label4.place(x=500, y=50)


    n=100
    for i in mov_det.keys():
        Label(new,text=i,bg="light green",fg="dark blue",font="comicsansms 12 bold").place(x=0,y=n)
        Label(new, text="______________________________________________________________________________________________________________________________", bg="light green",fg="blue", font="comicsansms 12 bold").place(x=0, y=n + 25)
        n=n+50
    a=100
    for j in mov_det.values():
        Label(new,text=j[0],bg="light green",fg="dark blue",font="comicsansms 12 bold").place(x=200,y=a)
        Label(new, text=j[1], bg="light green", fg="dark blue", font="comicsansms 12 bold").place(x=500, y=a)
        a = a + 50
    btn1 = Button(new, text="QUIT", bg="orange", fg="blue", font="comicsansms 12 bold",command=root.destroy)
    btn1.place(x=600, y=600)
    btn2 = Button(new, text="BACK", bg="orange", fg="blue", font="comicsansms 12 bold", command=new.destroy)
    btn2.place(x=700, y=600)
    new.mainloop()
root = Tk()
root.geometry("520x640")
root.title("SHOW BOX!!")
root.configure(bg="light blue")
label1 = Label(root,text="NOW STREAMING!!!",font="comicsansms 20 bold",fg="red",bg='light blue')
img1 = PhotoImage(file='File Location Here\\endgame.gif')
img2 = PhotoImage(file='File Location Here\\ncap.gif')
img3 = PhotoImage(file='File Location Here\\Gb.gif')
img4 = PhotoImage(file=’File Location Here\\nhb.gif')
# file location example: C:\\Users\\USERNAME\\Documents\\gully.gif
button1 = Button(root,image=img1,command=endgame)
button2 = Button(root,image=img2,command=cap)
button3 = Button(root,image=img3,command=Gb)
button4 = Button(root,image=img4,command=Hb)
lab1 = Label(root,text="AVENGERS:ENDGAME",font="comicsansms 12 bold",bg="light blue",fg="green")
lab1.place(x=0,y=325)
lab2 = Label(root,text="CAPTAIN MARVEL",font="comicsansms 12 bold",bg="light blue",fg="green")
lab2.place(x=300,y=315)
lab3 = Label(root,text="GULLY BOY",font="comicsansms 12 bold",bg="light blue",fg="green")
lab3.place(x=0,y=580)
lab4 = Label(root,text="HELL BOY",font="comicsansms 12 bold",bg="light blue",fg="green")
lab4.place(x=250,y=590)
button1.place(x=0,y=35,height=290,width=270)
button2.place(x=300,y=50)
button3.place(x=1,y=350,height=230,width=230)
button4.place(x=250,y=360,height=230,width=250)
button5 = Button(root,text="QUIT",command=root.destroy,font="comicsansms 12 bold",bg="red",fg="white")
button5.place(x=410,y=610,height=30,width=100)
button6 = Button(root,text="ADD A MOVIE!!",command=login,font="comicsansms 12 bold",bg="black",fg="yellow")
button6.place(x=0,y=610,height=30,width=150)
button7 = Button(root,text="UPCOMING MOVIES",command=upcoming,font="comicsansms 12 bold",bg="dark blue",fg="yellow")
button7.place(x=170,y=610,height=30,width=200)
label1.place(x=0,y=0)
root.mainloop()