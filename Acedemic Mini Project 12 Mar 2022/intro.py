from email import message
import math,random
from posixpath import split
from tkinter import messagebox
from cgitb import text
from textwrap import fill
from tkinter import*
import tkinter as tk
from tkinter import font
from turtle import bgcolor, color, onclick, onkeypress, width
import os

from setuptools import Command


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x712+0+0")
        self.root.title("Cafe Severney Billing Portal")
        bg_color = "#074463"
        title = Label(self.root, text="Cafe Severney", bd=12, fg="white", relief=GROOVE, bg=bg_color, font=(
            "Times new roman", 30, "bold"), pady=3).pack(fill=X)

        #================================Variable==================================================#
        #================================Beverages Variables==================================================#
        self.tea=IntVar()
        self.coffee=IntVar()
        self.espresso=IntVar()
        self.softdrink=IntVar()
        self.smoothie=IntVar()
        self.water=IntVar()
        #================================Meal Variable==================================================#
        self.sandwich=IntVar()
        self.burger=IntVar()
        self.soup=IntVar()
        self.noodles=IntVar()
        self.momos=IntVar()
        self.fries=IntVar()
        #================================Desert Variable==================================================#
        self.brownie=IntVar()
        self.chocolate=IntVar()
        self.puddings=IntVar()
        self.waffle=IntVar()
        self.roll=IntVar()
        self.applepie=IntVar()
        #================================Total Prices and Taxes===========================================#
        self.beverages_cost=StringVar()
        self.meal_cost=StringVar()
        self.desert_cost=StringVar()

        self.tax=IntVar()
        self.service_tax=IntVar()
        self.discount=IntVar()
        
        #================================Customer Variables=====================================#
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(100,999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #================================Customer Detail Frame=====================================#
        F1=LabelFrame(self.root,border=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,textvariable=self.c_name,width=22,font=("arial",15),bd=4,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,textvariable=self.c_phone,width=18,font=("arial",15),bd=4,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        cbill_lbl=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,textvariable=self.search_bill,width=15,font=("arial",15),bd=4,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        billbtn=Button(F1,text="Search",command=self.find_bill,width=10,border=7,font="Arial 12 bold").grid(row=0,column=6,pady=12,padx=35)

        #================================Beverages=====================================#
        F2=LabelFrame(self.root,border=10,relief=GROOVE,text="Beverages",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=6,y=188,width=325,height=380)

        tea_lbl=Label(F2,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F2,textvariable=self.tea,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        coffee_lbl=Label(F2,text="Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffee_txt=Entry(F2,textvariable=self.coffee,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        espresso_lbl=Label(F2,text="Espresso",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        espresso_txt=Entry(F2,textvariable=self.espresso,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        softdrink_lbl=Label(F2,text="Softdrink",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        softdrink_txt=Entry(F2,textvariable=self.softdrink,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        smoothie_lbl=Label(F2,text="Smoothie",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        smoothie_txt=Entry(F2,textvariable=self.smoothie,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        water_lbl=Label(F2,text="Water",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        water_txt=Entry(F2,textvariable=self.water,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================================Meal=====================================#
        F3=LabelFrame(self.root,border=10,relief=GROOVE,text="Meal",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=341,y=188,width=325,height=380)

        sandwich_lbl=Label(F3,text="Sandwich",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sandwich_txt=Entry(F3,textvariable=self.sandwich,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        burger_lbl=Label(F3,text="Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        burger_txt=Entry(F3,textvariable=self.burger,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        soup_lbl=Label(F3,text="Soup",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        soup_txt=Entry(F3,textvariable=self.soup,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        noodles_lbl=Label(F3,text="Noodles",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        noodles_txt=Entry(F3,textvariable=self.noodles,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        momos_lbl=Label(F3,text="Momos",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        momos_txt=Entry(F3,textvariable=self.momos,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fries_lbl=Label(F3,text="Fries",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fries_txt=Entry(F3,textvariable=self.fries,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #================================Desert=====================================#
        F4=LabelFrame(self.root,border=10,relief=GROOVE,text="Desert",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=188,width=325,height=380)

        brownie_lbl=Label(F4,text="Brownie",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        brownie_txt=Entry(F4,textvariable=self.brownie,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        chocolate_lbl=Label(F4,text="Chocolate",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        chocolate_txt=Entry(F4,textvariable=self.chocolate,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        puddings_lbl=Label(F4,text="Puddings",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        puddings_txt=Entry(F4,textvariable=self.puddings,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        waffle_lbl=Label(F4,text="Waffle",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        waffle_txt=Entry(F4,textvariable=self.waffle,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        roll_lbl=Label(F4,text="Swiss Roll",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        roll_txt=Entry(F4,textvariable=self.roll,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        applepie_lbl=Label(F4,text="Apple Pie",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        applepie_txt=Entry(F4,textvariable=self.applepie,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==================================BIll AREA===========================================#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place (x=1008,y=188,width=335,height=380)
        bill_title = Label(F5,text="Billing Area",font ="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH)

        #====================================Buttom Frame================================#
        F6=LabelFrame(self.root,border=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=574,relwidth=1,height=138)

        m1_lbl=Label(F6,text="Total Beverages Cost",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_txt=Entry(F6,textvariable=self.beverages_cost,width=18,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=0,column=1, padx=10,pady=1)  

        m2_lbl=Label(F6,text="Total Meal Cost",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=2,sticky="w")
        m2_txt=Entry(F6,textvariable=self.meal_cost,width=18,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=1,column=1, padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Desert Cost",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=2,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.desert_cost,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=2,column=1, padx=10,pady=1)

        

        c1_lbl=Label(F6,text="Tax @ 12",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=2,sticky="w")
        c1_txt=Entry(F6,textvariable=self.tax,width=18,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=0,column=3, padx=10,pady=1)  

        c2_lbl=Label(F6,text="Service Tax @ 6",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=2,sticky="w")
        c2_txt=Entry(F6,textvariable=self.service_tax,width=18,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=1,column=3, padx=10,pady=1)

        c3_lbl=Label(F6,text="Discount @ 10",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=2,sticky="w")
        c3_txt=Entry(F6,textvariable=self.discount,width=18,font="arial 10 bold",border=3,relief=SUNKEN).grid(row=2,column=3, padx=10,pady=1)


        btn_F=Frame(F6,bd=3,relief=GROOVE)
        btn_F.place(x=758,width=560,height=97)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="black",pady=5,padx=10,width=14,bd=3,height=3,font="arial 12 bold").grid(row=0,column=0,padx=7,pady=5)
        total_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="black",pady=5,padx=10,width=14,bd=3,height=3,font="arial 12 bold").grid(row=0,column=1,padx=7,pady=5)
        total_btn=Button(btn_F,text="Save/Print",command=self.save_bill,bg="cadetblue",fg="black",pady=5,width=14,padx=10,bd=3,height=3,font="arial 12 bold").grid(row=0,column=2,padx=7,pady=5)
        self.welcome_bill()
        
    def total(self):
        self.total_beverages_price=float(
                                    (self.tea.get()*15)+
                                    (self.coffee.get()*25)+
                                    (self.espresso.get()*35)+
                                    (self.softdrink.get()*30)+
                                    (self.smoothie.get()*45)+
                                    (self.water.get()*10)
                                    )
        self.beverages_cost.set("Rs. "+str(self.total_beverages_price))

        self.total_meal_price=float(
                                    (self.sandwich.get()*35)+
                                    (self.burger.get()*40)+
                                    (self.soup.get()*60)+
                                    (self.noodles.get()*70)+
                                    (self.momos.get()*7)+
                                    (self.fries.get()*40)
                                    )
        self.meal_cost.set("Rs. "+str(self.total_meal_price))

        self.total_desert_price=float(
                                    (self.brownie.get()*40)+
                                    (self.chocolate.get()*50)+
                                    (self.puddings.get()*35)+
                                    (self.waffle.get()*30)+
                                    (self.roll.get()*45)+
                                    (self.applepie.get()*60)
                                    )
        self.desert_cost.set("Rs. "+str(self.total_desert_price))
        self.z=(self.total_beverages_price+self.total_desert_price+self.total_meal_price)*.12
        self.y=(self.total_beverages_price+self.total_desert_price+self.total_meal_price)*.06
    
        self.tax.set("Rs. "+str(round(self.z,2)))
        self.service_tax.set("Rs. "+str(round(self.y,2)))
        self.dis=((self.z+self.y+self.total_beverages_price+self.total_desert_price+self.total_meal_price)*.1)
        self.discount.set("Rs. "+str(round(self.dis,2)))
        

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f"             Cafe Severney\n              Tax Invoice\n------------------------------------\nBill Number:              {self.bill_no.get()}\nCustomer Name:   {self.c_name.get()}\nPhone Number:        {self.c_phone.get()}\n------------------------------------\n            Bill Description\n====================================\nArticle          QTY           Price\n====================================\n")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="" :
            messagebox.showerror("Error","Customer Details are Missing")
        else:
            self.welcome_bill()
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"Tea               {self.tea.get()}            {self.tea.get()*15}\n")

            if self.coffee.get()!=0:
                self.txtarea.insert(END,f"Coffee            {self.coffee.get()}            {self.coffee.get()*25}\n")

            if self.espresso.get()!=0:
                self.txtarea.insert(END,f"Espresso          {self.espresso.get()}            {self.espresso.get()*35}\n")

            if self.softdrink.get()!=0:
                self.txtarea.insert(END,f"Softdrink         {self.softdrink.get()}            {self.softdrink.get()*30}\n")

            if self.smoothie.get()!=0:
                self.txtarea.insert(END,f"Smoothie          {self.smoothie.get()}            {self.smoothie.get()*45}\n")

            if self.water.get()!=0:
                self.txtarea.insert(END,f"Water             {self.water.get()}            {self.water.get()*10}\n")

            if self.sandwich.get()!=0:
                self.txtarea.insert(END,f"Sanwich           {self.sandwich.get()}            {self.sandwich.get()*35}\n")

            if self.burger.get()!=0:
                self.txtarea.insert(END,f"Burger            {self.burger.get()}          {self.burger.get()*70}\n")

            if self.soup.get()!=0:
                self.txtarea.insert(END,f"Soup              {self.soup.get()}           {self.soup.get()*60}\n")

            if self.noodles.get()!=0:
                self.txtarea.insert(END,f"Noodles           {self.noodles.get()}            {self.noodles.get()*70}\n")

            if self.momos.get()!=0:
                self.txtarea.insert(END,f"Momo              {self.momos.get()}            {self.momos.get()*7}\n")

            if self.fries.get()!=0:
                self.txtarea.insert(END,f"Fries             {self.fries.get()}            {self.fries.get()*40}\n")

            if self.brownie.get()!=0:
                self.txtarea.insert(END,f"Brownie           {self.brownie.get()}            {self.brownie.get()*40}\n")

            if self.chocolate.get()!=0:
                self.txtarea.insert(END,f"Chocolate         {self.chocolate.get()}            {self.chocolate.get()*50}\n")

            if self.puddings.get()!=0:
                self.txtarea.insert(END,f"Puddings          {self.puddings.get()}            {self.puddings.get()*35}\n")

            if self.waffle.get()!=0:
                self.txtarea.insert(END,f"Waffle            {self.waffle.get()}            {self.waffle.get()*30}\n")

            if self.roll.get()!=0:
                self.txtarea.insert(END,f"Swiss Roll        {self.roll.get()}            {self.roll.get()*45}\n")

            if self.applepie.get()!=0:
                self.txtarea.insert(END,f"Apple Pie         {self.applepie.get()}            {self.applepie.get()*60}\n")
            self.txtarea.insert(END,"====================================\n")
            self.txtarea.insert(END,f"Number of Bevereges:            {self.tea.get()+self.coffee.get()+self.espresso.get()+self.softdrink.get()+self.smoothie.get()+self.water.get()}\n")
            self.txtarea.insert(END,f"Number of Meals:                {(self.sandwich.get())+(self.burger.get())+(self.soup.get())+(self.noodles.get()*70)+(self.momos.get())+(self.fries.get())}\n")
            self.txtarea.insert(END,f"Number of Deserts:              {(self.brownie.get())+(self.chocolate.get())+(self.puddings.get())+(self.waffle.get())+(self.roll.get())+(self.applepie.get()*60)}\n")


            self.txtarea.insert(END,f"\nTotal Quantity:                 {self.tea.get()+self.coffee.get()+self.espresso.get()+self.softdrink.get()+self.smoothie.get()+self.water.get()+(self.sandwich.get())+(self.burger.get())+(self.soup.get())+(self.noodles.get()*70)+(self.momos.get())+(self.fries.get())+(self.brownie.get())+(self.chocolate.get())+(self.puddings.get())+(self.waffle.get())+(self.roll.get())+(self.applepie.get()*60)}\n")
            self.txtarea.insert(END,"------------------------------------\n")
            self.txtarea.insert(END,f"Taxable Value:       Rs. {round(((self.z*100)/12),2)}\n")
            self.txtarea.insert(END,f"Tax:                     {round((self.z),2)}\n")
            self.txtarea.insert(END,f"Service Tax:             {round((self.y),2)}\n")
            self.txtarea.insert(END,f"Discount:                {round((self.dis),2)}\n")
            self.txtarea.insert(END,"====================================\n")
            
            self.total_bill=(((self.z*100)/12)+self.y+self.z)-self.dis
            self.txtarea.insert(END,f"Total Bill:          Rs. {round((self.total_bill),2)}\n")
            
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bill/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill Number : {self.bill_no.get()} saved successfully!")
        else:
            return
    def find_bill(self):
        present ="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bill/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

root = tk.Tk()
obj = Bill_App(root)

root.iconphoto(False, tk.PhotoImage(file='severney.png'))
root.mainloop()