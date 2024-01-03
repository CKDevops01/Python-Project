import tkinter as tk
import time;
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import os

import mysql.connector

#mycursor.execute("Create table Restaurent_Data(SNo int(3),Customer_Name varchar(200),Amount double,BillNo int(6) )")



window=tk.Tk()
window.geometry("700x700")
window.title("Login System")

ik=Image.open("phebe-tan-G0H58Z5aPog-unsplash123.jpg")
BG=ImageTk.PhotoImage(ik)

ig=PhotoImage(file="logo.png")
ig2=PhotoImage(file="person logo4.png")
ig3=PhotoImage(file="username.png")
ig4=PhotoImage(file="iconfinder_icons_password_1564520.png")

lb=Label(window,image=BG).place(x=1,y=0)
label=Label(window,image=ig).place(x=60,y=180)
label8=Label(window,text="Restaurent management system",font=("algerian",45),fg="red").place(x=300,y=10)
label2=Label(window,text="Login System",font=("century",20),fg="green",bg="yellow",relief=GROOVE).place(x=750,y=150)
frame=Frame(window,bg="white").place(x=700)

label3=Label(frame,image=ig2).place(x=710,y=220)
label4=Label(frame,image=ig3,relief=GROOVE).place(x=600,y=500)
uname=StringVar()
passwd=StringVar()



label5=Label(frame,text="Username:",font=("arial bold",15),bg="white",fg="black",pady=12,relief=GROOVE).place(x=655,y=503)
entry=tk.Entry(frame,width=30,textvariable=uname,bd=10,font=("",15),relief=GROOVE).place(x=770,y=512)

label6=Label(frame,image=ig4,relief=GROOVE).place(x=600,y=600)
label7=Label(frame,text="Password:",font=("arial bold",15),bg="white",fg="black",pady=12,relief=GROOVE).place(x=655,y=603)
entry=Entry(frame,width=30,textvariable=passwd,bd=10,font=("",15),relief=GROOVE).place(x=770,y=612)
def log():
    if(uname.get()=="" or passwd.get()==""):
        messagebox.showerror("Error","All fields are required!")
    elif (uname.get()== "AJANTHA" or passwd.get()== "12345"):
        panel3 = Toplevel()
        panel3.geometry("1000x1000")
        panel3.title("Orders")
        i = Image.open("main course.jpg")
        rend = ImageTk.PhotoImage(i)
        lbb = Label(panel3, image=rend)
        lbb.image = rend
        lbb.place(x=530, y=240)
        ii = Image.open("BEVERAGES.jpg")
        ren = ImageTk.PhotoImage(ii)
        lbb1 = Label(panel3, image=ren)
        lbb1.image = ren
        lbb1.place(x=940, y=240)
        iii = Image.open("starter.jpg")
        rende = ImageTk.PhotoImage(iii)
        lbb2 = Label(panel3, image=rende)
        lbb2.image = rende
        lbb2.place(x=80, y=240)
        sum3 = 0
        var = DoubleVar()
        var1=StringVar()
        Input = IntVar()
        Input1 = IntVar()
        Input2 = IntVar()
        Input3 = IntVar()
        Input4 = IntVar()
        Input5 = IntVar()
        Input6 = IntVar()
        Input7 = IntVar()
        Input8 = IntVar()
        Input9 = IntVar()
        Input10 = IntVar()
        Input11 = IntVar()
        Input12 = IntVar()
        Input13 = IntVar()
        Input14 = IntVar()
        Input15 = IntVar()

        l = Label(panel3, text="ajantha Restaurent", font=("algerian", 30), fg="white", bd=10, relief=GROOVE,
                     bg="grey", pady=5).place(x=400, y=20)
        l1 = Label(panel3, text="Menu Card", font=("Harlow Solid Italic", 20), fg="white", bd=8, relief=GROOVE,
                      bg="sky blue", pady=5).place(x=550, y=107)
        l2 = Label(panel3, text="STARTERS", font=("Lucida Calligraphy", 15), fg="white", bd=8, relief=GROOVE,
                      bg="purple", pady=5).place(x=100, y=180)
        l3 = Label(panel3, text="MAIN COURSE", font=("Lucida Calligraphy", 15), fg="white", bd=8, relief=GROOVE,
                      bg="orange", pady=5).place(x=530, y=180)
        l4 = Label(panel3, text="BEVERAGES", font=("Lucida Calligraphy", 15), fg="white", bd=8, relief=GROOVE,
                      bg="green", pady=5).place(x=950, y=180)

        ###STARTERS##
        l5 = Label(panel3, text="MASALA PAPAD  ? 70/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                      pady=5).place(x=50, y=420)
        entry2 = Entry(panel3, textvariable=Input, bg="powder blue", relief=GROOVE, bd=7).place(x=60, y=450)
        l6 = Label(panel3, text="PANEER CRISPY  ? 170/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                      pady=5).place(x=50, y=480)
        entry3 = Entry(panel3, textvariable=Input1, bg="powder blue", relief=GROOVE, bd=7).place(x=60, y=510)
        l7 = Label(panel3, text="VEG CRISPY  ? 160/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                      pady=5).place(x=50, y=540)
        entry4 = Entry(panel3, textvariable=Input2, bg="powder blue", relief=GROOVE, bd=7).place(x=60, y=570)
        l8 = Label(panel3, text="PANEER TIKKA DRY  ? 200/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                      pady=5).place(x=230, y=420)
        entry5 = Entry(panel3, textvariable=Input3, bg="powder blue", relief=GROOVE, bd=7).place(x=250, y=450)
        l9 = Label(panel3, text="VEG 65  ? 150/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                      pady=5).place(x=260, y=480)
        entry6 = Entry(panel3, textvariable=Input4, bg="powder blue", relief=GROOVE, bd=7).place(x=250, y=510)
        l10 = Label(panel3, text="PANEER 65  ? 180/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=250, y=540)
        entry7 = Entry(panel3, textvariable=Input5, bg="powder blue", relief=GROOVE, bd=7).place(x=250, y=570)

        ### MAIN COURSE###

        l11 = Label(panel3, text="PANEER BUTTER MASALA  ? 180/-", font=("Bookman Old Style", 10), fg="black",
                       bd=3, pady=5).place(x=490, y=420)
        entry8 = Entry(panel3, textvariable=Input6, bg="orange", relief=GROOVE, bd=7).place(x=520, y=450)
        l12 = Label(panel3, text="PALAK PANEER  ? 170/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=490, y=480)
        entry9 = Entry(panel3, textvariable=Input7, bg="orange", relief=GROOVE, bd=7).place(x=520, y=510)
        l13 = Label(panel3, text="VEG KOLHAPURI  ? 200/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=490, y=540)
        entry10 = Entry(panel3, textvariable=Input8, bg="orange", relief=GROOVE, bd=7).place(x=520, y=570)
        l14 = Label(panel3, text="MIX VEG  ? 190/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=740, y=420)
        entry11 = Entry(panel3, textvariable=Input9, bg="orange", relief=GROOVE, bd=7).place(x=740, y=450)
        l15 = Label(panel3, text="DAL FRY  ? 140/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=740, y=480)
        entry12 = Entry(panel3, textvariable=Input10, bg="orange", relief=GROOVE, bd=7).place(x=740, y=510)
        l16 = Label(panel3, text="DAL TADKA ? 150/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=740, y=540)
        entry13 = Entry(panel3, textvariable=Input11, bg="orange", relief=GROOVE, bd=7).place(x=740, y=570)

        ###BEVERAGES###

        l17 = Label(panel3, text="TEA OR COFFEE  ? 50/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=950, y=420)
        entry14 = Entry(panel3, textvariable=Input12, bg="powder blue", relief=GROOVE, bd=7).place(x=970, y=450)
        l18 = Label(panel3, text="ALL FRESH JUICE ? 70/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=950, y=480)
        entry15 = Entry(panel3, textvariable=Input13, bg="powder blue", relief=GROOVE, bd=7).place(x=970, y=510)
        l19 = Label(panel3, text="ALL COLD DRINKS ? 30/-", font=("Bookman Old Style", 10), fg="black", bd=3,
                       pady=5).place(x=950, y=540)
        entry16 = Entry(panel3, textvariable=Input14, bg="powder blue", relief=GROOVE, bd=7).place(x=970, y=570)

        def bill_no():
            x = random.randint(10908, 500879)
            ref = x
            Input15.set(ref)

        def reset():
            Input.set(0)
            Input1.set(0)
            Input2.set(0)
            Input3.set(0)
            Input4.set(0)
            Input5.set(0)
            Input6.set(0)
            Input7.set(0)
            Input8.set(0)
            Input9.set(0)
            Input10.set(0)
            Input11.set(0)
            Input12.set(0)
            Input13.set(0)
            Input14.set(0)
            Input15.set(0)
            var.set(0.0)
            var1.set(" ")
        bill = Button(panel3, text="Bill No:", font=("Bookman Old Style", 10), command=bill_no, fg="black", bd=3,
                         bg="Orange", pady=5).place(x=50, y=48)
        entry19 = Entry(panel3, textvariable=Input15, bg="white", font=("arial bold", 10), relief=GROOVE,
                           bd=7).place(x=130, y=48)
        localtime = time.asctime(time.localtime(time.time()))
        labelinfo = Label(panel3, text=localtime, font=("arial bold", 20), fg="red").place(x=1000, y=48)
        res = Button(panel3, text="RESET", font=("Bookman Old Style", 10), command=reset, fg="black", bd=3,
                        bg="powder blue", pady=5).place(x=420, y=690)
        def Totl():
            sum = (Input.get()) * 70 + (Input1.get()) * 170 + (Input2.get()) * 160 + (Input3.get()) * 200 + (
                Input4.get()) * 150 + (Input5.get()) * 180 + (Input6.get()) * 180 + (Input7.get()) * 170 + (
                      Input8.get()) * 200 + (Input9.get()) * 190 + (Input10.get()) * 140 + (Input11.get()) * 150 + (
                      Input12.get()) * 50 + (Input13.get()) * 70 + (Input14.get()) * 30
            # sum=(entry2.get()*70)+(entry3.get()*170)+(entry4.get()*160)+(entry5.get()*200)+(entry6.get()*150)+(entry7.get()*180)+(entry8.get()*180)+(entry9.get()*170)+(entry10.get()*200)+(entry11.get()*190)+(entry12.get()*140)+(entry13.get()*150)+(entry14.get()*50)+(entry15.get()*70)+(entry16.get()*30)
            Servies_tax = 50
            sum2 = (sum) * (18 / 100)
            sum3 = sum2 + Servies_tax + sum
            var.set(sum3)

        btn = Button(panel3, text="TOTAL", font=("Bookman Old Style", 10), command=Totl, fg="white", relief=GROOVE,
                        bg="grey",
                        bd=8, pady=5).place(x=500, y=690)
        entry = Entry(panel3, textvariable=var, bg="white", relief=GROOVE, bd=7).place(x=580, y=690)
        gst=Label(panel3,text="GST(CGST+SGST)=18%",fg="black",font=("century",20)).place(x=500,y=600)
        tax = Label(panel3, text="Servies_tax=50Rs", fg="black", font=("century", 20)).place(x=200, y=600)
        l20 = Label(panel3, text="Customer Name:", font=("Bookman Old Style", 13), fg="black", bd=3,
                       pady=5).place(x=900, y=110)
        entry20 = Entry(panel3, textvariable=var1, bg="white", relief=GROOVE, bd=7).place(x=1080, y=110)

        def add_Data():
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Pranav@123##", database="Pranavdb")
            mycursor = mydb.cursor()
            mycursor.execute("insert into Restaurent_Data values(%s,%s,%s,%s)", (Input15.get(), var1.get(), var.get(),localtime))
            mydb.commit()
            mydb.close()

        btn2 = Button(panel3, text="ADD \n DATA", command=add_Data, font=("Bookman Old Style", 10), fg="white",
                      relief=GROOVE,
                      bg="grey",
                      bd=8, pady=5).place(x=990, y=690)
        def Bill_Generate():
            master = Toplevel()
            master.geometry("1000x1000")
            master.title("BILL")
            b_reciept=Label(master,text="BILL RECIEPT",font=("algerian",25),fg="blue").place(x=590,y=40)



            lib = Listbox(master, width=70, height=30)
            lib.insert(0, "Bill_No: " + str(Input15.get()))
            lib.insert(1,"Customer Name:"    + str(var1.get())                                           )
            lib.insert(2, "                                          AJANTHA RESTAURENT      ")
            lib.insert(3, "                                              Payment Receipt                       ")
            lib.insert(4,
                       "Itemes                                               Rate                Quantity         Amount")
            lib.insert(5, "MASALA PAPAD                                 70\t\t\t\t\t                    " + str(
                Input.get()) + "                       " + str(Input.get() * 70))
            lib.insert(6, "PANEER CRISPY                                  170\t\t\t\t\t                  " + str(
                Input1.get()) + "                       " + str(Input1.get() * 170))
            lib.insert(7, "VEG CRISPY                                         160\t\t\t\t                  " + str(
                Input2.get()) + "                       " + str(Input2.get() * 160))
            lib.insert(8, "PANEER TIKKA DRY                            200\t\t\t\t\t                  " + str(
                Input3.get()) + "                       " + str(Input3.get() * 200))
            lib.insert(9,
                       "VEG 65                                                  150\t\t\t\t\t                  " + str(
                           Input4.get()) + "                       " + str(Input4.get() * 150))
            lib.insert(10, "PANEER 65                                           180\t\t\t\t\t                  " + str(
                Input5.get()) + "                       " + str(Input5.get() * 180))
            lib.insert(11, "PANEER BUTTER MASALA                180\t\t\t\t\t                  " + str(
                Input6.get()) + "                       " + str(Input6.get() * 180))
            lib.insert(12, "PALAK PANEER                                   170\t\t\t\t\t                  " + str(
                Input7.get()) + "                       " + str(Input7.get() * 170))
            lib.insert(13, "VEG KOLHAPURI                                 200\t\t\t\t\t                  " + str(
                Input8.get()) + "                       " + str(Input8.get() * 200))
            lib.insert(14,
                       "MIX VEG                                              190\t\t\t\t\t                   " + str(
                           Input9.get()) + "                       " + str(Input9.get() * 190))
            lib.insert(15,
                       "DAL FRY                                              140\t\t\t\t\t                   " + str(
                           Input10.get()) + "                       " + str(Input10.get() * 140))
            lib.insert(16, "DAL TADAKA                                      150\t\t\t\t\t                   " + str(
                Input11.get()) + "                       " + str(Input11.get() * 150))
            lib.insert(17, "TEA OR COFFEE                                  50\t\t\t\t\t                    " + str(
                Input12.get()) + "                       " + str(Input12.get() * 50))
            lib.insert(18, "FRESH JUICE                                        70\t\t\t\t\t                    " + str(
                Input13.get()) + "                       " + str(Input13.get() * 70))
            lib.insert(19, "COLD DRINKS                                     30\t\t\t\t\t                    " + str(
                Input14.get()) + "                       " + str(Input14.get() * 30))
            lib.insert(20, "GST(CGST+SGST=18%)")
            lib.insert(21, "Servies_tax=100 ?")
            lib.insert(22,"                                                                                         Total(Rs)=" + str(var.get()))
            lib.insert(23, "                   THANKS FOR YOUR PAYMENT      ")
            lib.insert(24, "                         DO VISIT AGAIN!           ")
            lib.place(x=500, y=90)
        btn1 = Button(panel3, text="GENERATE \n BILL", command=Bill_Generate, font=("Lucida Calligraphy", 10),fg="black", bd=8,relief=GROOVE, bg="orange").place(x=800, y=700)


    else:
        messagebox.showerror("Error", "Invalid Username or Password")

btn=Button(frame,text="Login",bg="blue",command=log,fg="white",font=("arial bold",15),relief=GROOVE).place(x=800,y=700)


window.mainloop()
