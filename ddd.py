from tkinter import *
from tkinter import messagebox
import webbrowser
import random
from datetime import date
import time
pro = Tk()
u1="https://www.facebook.com/noor.kurdi.77"
u2="https://www.instagram.com/noorkurdi/"
u3="https://t.me/noorku"
def about1 () :
    messagebox.showinfo('developer' , 'Noor Kurdi')
def about2 () :
    messagebox.showinfo('About the program' , 'Pharmacy project in python')
pro.geometry('800x450+280+50')
pro.resizable(False, False)
pro.title("Pharmacy صيدلية")
pro.iconbitmap('D:\\ph.ico')
title = Label(pro, text='Pharmacy system', fg='white', bg='light blue', font=('leelawadee', 30, 'bold') )
title.pack(fill=X)
f1= Frame(pro, width=230, height=420, bg='pink')
f1.place(x=570, y=54)
title1 = Label(f1, text="Pharmacy project", bg="pink", fg="white", font=("leelawadee", 15, "bold"))
title1.place(x=20, y=16)
title2 = Label(f1, text="Noor developer",bg="pink", fg="white", font=("leelawadee", 15, "bold"))
title2.place(x=20, y=55)
title3=Label(f1, text="Communication ways",bg="pink", fg="white", font=("leelawadee", 15, "bold"))
title3.place(x=13, y=120)
def open1 () :
    webbrowser.open_new(u1)
b1=Button(f1, text="Facebook", width=20, fg="white", bg="light blue", font=("leelawadee", 12, "bold"), command = open1)
b1.place(x=10, y=160)
def open2 () :
    webbrowser.open_new(u2)
b2=Button(f1, text="Instagram", width=20, fg="white", bg="light blue", font=("leelawadee", 12, "bold"), command = open2)
b2.place(x=10, y=200)
def open3 () :
    webbrowser.open_new(3)
b3=Button(f1, text="Telegram",width=20, fg="white", bg="light blue", font=("leelawadee", 12, "bold"), command = open3)
b3.place(x=10, y=240)
b4=Button(f1, text="developer" , width=20, fg="white" , bg="light blue" , font = ("leelawadee" , 12 , "bold" ) , command =about1)
b4.place(x=10 , y=280)
b5=Button(f1, text="project", width=20, fg="white" , bg="light blue" , font = ("leelawadee" , 12 , "bold" ) , command=about2)
b5.place(x=10,y=320)
b6=Button(f1 , text = "Exit" ,  width=20, fg="white" , bg="light blue" , font = ("leelawadee" , 12 , "bold" ) , command= quit)
b6.place(x=10 , y= 360)
photo = PhotoImage(file="D:\\phph.png")
imo = Label(pro , image = photo , width = 250 , height = 240)
imo.place(x=155 , y=55)
f2 = Frame(pro , width= 570 , height= 400, bg ="pink" )
f2.place(x=0,y=300)
class Ph :
    def __init__(self , root):
        self.root=root
        self.root.geometry('1525x780+0+10')
        self.root.title('Pharmacy صيدلية')
        self.root.resizable(False,False)
        self.root.iconbitmap('D:\\ph.ico')
        title = Label(self.root , text ="Pharmacy management" , width = 25,  fg = "white" , bg="light blue" , font =("leelawadee" ,25) )
        title.pack(fill =X)
        #==========================
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.w1=IntVar()
        self.w2=IntVar()
        self.w3=IntVar()
        self.w4=IntVar()
        self.w5=IntVar()
        self.w6=IntVar()
        self.h1=IntVar()
        self.h2=IntVar()
        self.h3=IntVar()
        self.h4=IntVar()
        self.h5=IntVar()
        self.h6=IntVar()
        self.h7=IntVar()
        self.h8=IntVar()
        self.j1=IntVar()
        self.j2=IntVar()
        self.j3=IntVar()
        self.j4=IntVar()
        self.j5=IntVar()
        self.j6=IntVar()
        self.n1=IntVar()
        self.n2=IntVar()
        self.n3=IntVar()
        self.n4=IntVar()
        self.n5=IntVar()
        self.n6=IntVar()
        self.n7=IntVar()
        self.n8=IntVar()
        #==========================
        self.date=date.today()
        self.Time=time.localtime()
        self.time=time.strftime('%H:%M:%S',self.Time)
        #==========================
        self.na=StringVar()
        self.phone=StringVar()
        self.order=StringVar()
        self.bill=IntVar()
        x=random.randint(50 ,400)
        self.bill.set(x)
        #===== patient Data ========
        f1 = Frame(root , width =380 , bd=2 , height =270 , bg = "#ff91a4"  )
        f1.place(x=0 ,y=46)
        en1 = Entry(f1, font=("leelawadee" ,15 ) , justify="center" , width=17,textvariable=self.na)
        en1.place(x=160 , y=32)
        en2=Entry(f1 , font=('leelawadee' , 15), justify="center" , width=17,textvariable=self.phone)
        en2.place(x=160, y =72)
        en3=Entry(f1, font=("leelawadee" , 15) , justify="center" , width=17,textvariable=self.order)
        en3.place(x=160 , y=112)
        en4=Spinbox(f1 , from_=0,to=1000,justify="center" ,textvariable=self.bill)
        en4.place(x=160 , y=158)
        tit = Label(f1 , text ="Patient Data" , bg="#ff91a4" , fg ="#008080" , font=("leelawadee" , 15, "bold"))
        tit.place(x=130 , y=0)
        his_name= Label(f1, text="Patient Name :" , bg="#ff91a4" , fg ="white" , font=("leelawadee" , 15, "bold"))
        his_name.place(x=8,y=30)
        his_phone =Label(f1, text="Patient Phone :" , bg="#ff91a4" , fg ="white" , font=("leelawadee" , 15, "bold"))
        his_phone.place(x=8 , y=70)
        his_ord=Label(f1, text="Total :" , bg="#ff91a4" , fg ="white" , font=("leelawadee" , 15, "bold"))
        his_ord.place(x=8 , y=110)
        his_num=Label(f1, text="Bill Number :" , bg="#ff91a4" , fg ="white" , font=("leelawadee" , 15, "bold"))
        his_num.place(x=8 , y=150)
        btn_patient = Button(f1 , text = "search" , font =("leelawadee" , 12) ,width = 10 , bg="light blue")
        btn_patient.place(x=130 , y=190)
        #=======bill=========
        titdd=Label(f1,text="Bills" , font=("leelawadee" , 17 ,"bold") ,bg="#ff91a4" , fg="#008080")
        titdd.place(x=152 , y= 230)
        f3=Frame(root , bd=2 , width=380 , height = 300 ,bg= "white")
        f3.place(x=-284 ,y=315)
        scroll= Scrollbar(f3 , orient=VERTICAL)
        self.textarea = Text(f3 , yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT ,fill=Y )
        scroll.config(command = self.textarea.yview)
        self.textarea.pack(fill =BOTH , expand =1)
        #========price=========
        f4=Frame(root , bd=2 , width=380 , height=112 , bg="#ff91a4" )
        f4.place(x=0 ,y=705)
        self.hesab=Button(f4 ,text= "Total" ,width=6 , height=2 ,font="leelawadee" , bg="light blue",command=self.Total)
        self.hesab.place(x=10 , y=5)
        bill=Button(f4 ,text= "Get the bill" ,width =9 , height=2 ,font="leelawadee" , bg="light blue",command=self.welcome)
        bill.place(x=92 , y=5)
        clear = Button(f4 ,text= "Clear" ,width =6 , height=2 ,font="leelawadee" , bg="light blue",command=self.welcome1 )
        clear.place(x=207 , y=5)
        exit = Button(f4 ,text= "Exit" ,width =6 , height=2 ,font="leelawadee" , bg="light blue",command=quit)
        exit.place(x=290 , y=5)
        #========مسكنات========
        ff1=Frame(root, bd=2 ,width =318 , height =800 , bg="#ff91a4")
        ff1.place(x=1207 , y=46)
        painkillers=Label(ff1 , text="Painkillers" , font=("leelawadee" , 23 ,"bold") , bg="#ff91a4" , fg="#008080")
        painkillers.place(x=85 ,y=0)
        pk1=Label(ff1, text="ParaCetamol" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk1.place(x=5 , y=55)
        pk2=Label(ff1, text="IbuProfen" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk2.place(x=5 , y=100)
        pk3=Label(ff1,text="Banadol" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk3.place(x=5 , y=145)
        pk4=Label(ff1, text="Excedrin" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk4.place(x=5 , y=190)
        pk5=Label(ff1, text="Unadol" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk5.place(x=5 , y=235)
        pk6=Label(ff1, text="Declone" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk6.place(x=5 , y=280)
        pk7=Label(ff1, text="Tramadol" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk7.place(x=5 , y=325)
        pk8=Label(ff1, text="Acetaminophen" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk8.place(x=5 , y=370)
        pk9=Label(ff1, text="Morphine" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk9.place(x=5 , y=415)
        pk10=Label(ff1, text="Methadone" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk10.place(x=5 , y=460)
        pk11=Label(ff1, text="CetaCodeine" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk11.place(x=5 , y=505)
        pk12=Label(ff1, text="Oxycodone" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk12.place(x=5 , y=550)
        pk13=Label(ff1, text="Fentanyl" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk13.place(x=5 , y=595)
        pk14=Label(ff1, text="Oxymorphone" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk14.place(x=5 , y=640)
        pk15=Label(ff1, text="SuperGesic" , font=("leelawadee" ,16) ,bg="#ff91a4" , fg="white")
        pk15.place(x=5 , y=685)
        ene1=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q1)
        ene1.place(x=160 ,y=61)
        ene2=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q2)
        ene2.place(x=160 ,y=105)
        ene3=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q3)
        ene3.place(x=160 ,y=150)
        ene4=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q4)
        ene4.place(x=160 ,y=195)
        ene5=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q5)
        ene5.place(x=160 ,y=240)
        ene6=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q6)
        ene6.place(x=160 ,y=285)
        ene7=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q7)
        ene7.place(x=160 ,y=330)
        ene8=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q8)
        ene8.place(x=160 ,y=375)
        ene9=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q9)
        ene9.place(x=160 ,y=422)
        ene10=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q10)
        ene10.place(x=160 ,y=467)
        ene11=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q11)
        ene11.place(x=160 ,y=511)
        ene12=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q12)
        ene12.place(x=160 ,y=555)
        ene13=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q13)
        ene13.place(x=160 ,y=600)
        ene14=Spinbox(ff1, from_=0 ,to =100 , justify="center",textvariable=self.q14)
        ene14.place(x=160 ,y=647)
        ene15=Spinbox(ff1, from_=0 ,to =100, justify="center",textvariable=self.q15)
        ene15.place(x=160 ,y=691)
        #========الالتهاب=======
        f2=Frame(root, bd=2 , bg="#ff91a4" , width=400 , height=330)
        f2.place(x=805,y=46)
        anti_inflammatory=Label(f2 , text="Anti-Iflammatory" , bg="#ff91a4" , fg="#008080" , font=("leelawadee" , 23 , "bold"))
        anti_inflammatory.place(x=72,y=0)
        ai1=Label(f2 , text="Augmentin" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai1.place(x=5 ,y=55)
        ai2=Label(f2 , text="Mosapride" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai2.place(x=5 ,y=100)
        ai3=Label(f2 , text="Epicotil" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai3.place(x=5 ,y=145)
        ai4=Label(f2 , text="Amoxicillin" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai4.place(x=5 ,y=190)
        ai5=Label(f2 , text="Mucoangin" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai5.place(x=5 ,y=235)
        ai6=Label(f2 , text="Azithromycin" , bg="#ff91a4" , fg="white" , font=("leelawadee" , 16))
        ai6.place(x=5 ,y=280)
        sb1=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w1)
        sb1.place(x=160 , y=61)
        sb2=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w2)
        sb2.place(x=160 , y=105)
        sb3=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w3)
        sb3.place(x=160 , y=150)
        sb4=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w4)
        sb4.place(x=160 , y=195)
        sb5=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w5)
        sb5.place(x=160 , y=240)
        sb6=Spinbox(f2 , from_=0 , to=100 , justify="center",textvariable=self.w6)
        sb6.place(x=160 , y=285)
        #========المراهم=======
        f5=Frame(root,width=400 , height=470 ,bg="#ff91a4" , bd=2)
        f5.place(x=805 , y=378)
        O=Label(f5 , text="Ointments" , bg="#ff91a4" , fg="#008080" , font=("leelawadee" , 23 , "bold"))
        O.place(x= 120,y=0)
        o1=Label(f5 , text="Gentamicin" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o1.place(x=5 ,y=45)
        o2=Label(f5 , text="Dermatin" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o2.place(x=5 ,y=90)
        o3=Label(f5 , text="Voltaren" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o3.place(x=5 ,y=135)
        o4=Label(f5 , text="Fucidin" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o4.place(x=5 ,y=180)
        o5=Label(f5 , text="Dermovate" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o5.place(x=5 ,y=225)
        o6=Label(f5 , text="Kenacomb" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o6.place(x=5 ,y=270)
        o7=Label(f5 , text="Diprosalic" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o7.place(x=5 ,y=315)
        o8=Label(f5 , text="Fucicort" ,bg="#ff91a4" ,fg="white" ,font=("leelawadee" ,16))
        o8.place(x=5 ,y=360)
        so1=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h1)
        so1.place(x=160 , y=53)
        so2=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h2)
        so2.place(x=160 , y=98)
        so3=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h3)
        so3.place(x=160 , y=143)
        so4=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h4)
        so4.place(x=160 , y=188)
        so5=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h5)
        so5.place(x=160 , y=233)
        so6=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h6)
        so6.place(x=160 , y=278)
        so7=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h7)
        so7.place(x=160 , y=323)
        so8=Spinbox(f5 , from_=0 , to=100 , justify="center",textvariable=self.h8)
        so8.place(x=160 , y=368)
        #=======الملينات=======
        f6=Frame(root , width =420 , height=330 ,bg="#ff91a4" ,bd=2)
        f6.place(x= 383,y=46)
        La=Label(f6 ,text="Laxative" ,bg="#ff91a4" , fg='#008080' ,font=("leelawadee" ,23 , 'bold'))
        La.place(x=148 ,y=0)
        la1=Label(f6 ,text="Dulcolax" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la1.place(x=5 ,y=55)
        la2=Label(f6 ,text="Duphalac" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la2.place(x=5 ,y=100)
        la3=Label(f6 ,text="Agiolax" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la3.place(x=5 ,y=145)
        la4=Label(f6 ,text="Ezilax" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la4.place(x=5 ,y=190)
        la5=Label(f6 ,text="Movicol" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la5.place(x=5 ,y=235)
        la6=Label(f6 ,text="Normacol" ,fg='white' ,bg='#ff91a4' ,font=('leelawadee' , 16))
        la6.place(x=5 ,y=280)
        sl1=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j1)
        sl1.place(x=160 ,y=63)
        sl2=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j2)
        sl2.place(x=160 ,y=108)
        sl3=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j3)
        sl3.place(x=160 ,y=153)
        sl4=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j4)
        sl4.place(x=160 ,y=198)
        sl5=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j5)
        sl5.place(x=160 ,y=243)
        sl6=Spinbox(f6 ,from_=0 ,to=100,justify='center',textvariable=self.j6)
        sl6.place(x=160 ,y=288)
        #==============كريمات=============
        f7=Frame(root , bd=2 ,bg="#ff91a4" , width=420 ,height =470)
        f7.place(x=383 ,y=378)
        c=Label(f7 ,text="Creams" ,bg="#ff91a4" ,fg="#008080" ,font=("leelawadee",23,"bold"))
        c.place(x=150 ,y=0)
        c1=Label(f7 ,text="Dove",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c1.place(x=5,y=50)
        c2=Label(f7 ,text="Olay",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c2.place(x=5,y=95)
        c3=Label(f7 ,text="Nivea",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c3.place(x=5,y=140)
        c4=Label(f7 ,text="Vaseline",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c4.place(x=5,y=185)
        c5=Label(f7 ,text="Cetaphil",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c5.place(x=5,y=230)
        c6=Label(f7 ,text="Fair&Lovely",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c6.place(x=5,y=275)
        c7=Label(f7 ,text="Clean&Clear",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c7.place(x=5,y=320)
        c8=Label(f7 ,text="L'oreal",bg="#ff91a4",fg="white" ,font=("leelawadee",16))
        c8.place(x=5,y=365)
        sc1=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n1)
        sc1.place(x=160,y=58)
        sc2=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n2)
        sc2.place(x=160,y=103)
        sc3=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n3)
        sc3.place(x=160,y=143)
        sc4=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n4)
        sc4.place(x=160,y=193)
        sc5=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n5)
        sc5.place(x=160,y=238)
        sc6=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n6)
        sc6.place(x=160,y=283)
        sc7=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n7)
        sc7.place(x=160,y=328)
        sc8=Spinbox(f7 ,from_=0,to=100,justify='center',textvariable=self.n8)
        sc8.place(x=160,y=373)
        #==============Bill================
        self.welcome()
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"                                             Welcome to noor's pharmacy")
        self.textarea.insert(END,"\n                                   =============================================")
        self.textarea.insert(END,f"\n                                   Bill Num :{self.bill.get()}")
        self.textarea.insert(END,f"\n                                   Name :{self.na.get()}")
        self.textarea.insert(END,f"\n                                   Phone :{self.phone.get()}")
        self.textarea.insert(END,"\n                                   ==============================================")
        self.textarea.insert(END,f"                                  Price : {self.order.get()}")
        self.textarea.insert(END,f"\n                                   Date :{self.date}           Time :{self.time}")
        self.textarea.insert(END,"\n                                   ===============================================")
    def welcome1(self):
        x=random.randint(50,400)
        self.bill.set(x)
        a=""
        b=random.randint(0,0)
        c=''
        self.phone.set(a)
        self.na.set(a)
        self.order.set(c)
        self.q1.set(b)
        self.q2.set(b)
        self.q3.set(b)
        self.q4.set(b)
        self.q5.set(b)
        self.q6.set(b)
        self.q7.set(b)
        self.q8.set(b)
        self.q9.set(b)
        self.q10.set(b)
        self.q11.set(b)
        self.q12.set(b)
        self.q13.set(b)
        self.q14.set(b)
        self.q15.set(b)
        self.w1.set(b)
        self.w2.set(b)
        self.w3.set(b)
        self.w4.set(b)
        self.w5.set(b)
        self.w6.set(b)
        self.h1.set(b)
        self.h2.set(b)
        self.h3.set(b)
        self.h4.set(b)
        self.h5.set(b)
        self.h6.set(b)
        self.h7.set(b)
        self.h8.set(b)
        self.j1.set(b)
        self.j2.set(b)
        self.j3.set(b)
        self.j4.set(b)
        self.j5.set(b)
        self.j6.set(b)
        self.n1.set(b)
        self.n2.set(b)
        self.n3.set(b)
        self.n4.set(b)
        self.n5.set(b)
        self.n6.set(b)
        self.n7.set(b)
        self.n8.set(b)
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"                                             Welcome to Heba's pharmacy")
        self.textarea.insert(END,"\n                                   =============================================")
        self.textarea.insert(END,f"\n                                   Bill Num :{self.bill.get()}")
        self.textarea.insert(END,f"\n                                   Name : ")
        self.textarea.insert(END,f"\n                                   Phone :")
        self.textarea.insert(END,"\n                                   ==============================================")
        self.textarea.insert(END,f"                                  Price :                              ")
        self.textarea.insert(END,f"\n                                   Date :{self.date}           Time :{self.time}")
        self.textarea.insert(END,"\n                                   ===============================================")
        #================================
    def Total(self):
        self.pc=self.q1.get()*1.5
        self.Ip=self.q2.get()*2
        self.Ban=self.q3.get()*1
        self.ex=self.q4.get()*2
        self.un=self.q5.get()*1
        self.dec=self.q6.get()*1.5
        self.tra=self.q7.get()*4
        self.ac=self.q8.get()*1
        self.mr=self.q9.get()*1
        self.mth=self.q10.get()*1
        self.cc=self.q11.get()*1
        self.ox=self.q12.get()*1
        self.fen=self.q13.get()*1
        self.oxy=self.q14.get()*1
        self.sg=self.q15.get()*2
        self.aug=self.w1.get()*1.5
        self.mo=self.w2.get()*1.5
        self.ec=self.w3.get()*2
        self.am=self.w4.get()*1
        self.mu=self.w5.get()*1
        self.az=self.w6.get()*2
        self.gen=self.h1.get()*1.5
        self.de=self.h2.get()*1
        self.vol=self.h3.get()*2
        self.fu=self.h4.get()*1.5
        self.der=self.h5.get()*2
        self.ken=self.h6.get()*1.5
        self.dip=self.h7.get()*1
        self.fuc=self.h8.get()*1.5
        self.du=self.j1.get()*1
        self.dup=self.j2.get()*2
        self.ag=self.j3.get()*1.5
        self.ez=self.j4.get()*2
        self.mov=self.j5.get()*1
        self.no=self.j6.get()*1.5
        self.do=self.n1.get()*3
        self.ol=self.n2.get()*2
        self.niv=self.n3.get()*3
        self.vas=self.n4.get()*1.5
        self.cp=self.n5.get()*2
        self.fl=self.n6.get()*3
        self.cl=self.n7.get()*1
        self.lo=self.n8.get()*2
        self.totalieto=float(
            self.pc+
            self.Ip+
            self.Ban+
            self.sg+
            self.ox+
            self.oxy+
            self.fen+
            self.ex+
            self.ag+
            self.un+
            self.dec+
            self.tra+
            self.ac+
            self.mth+
            self.mr+
            self.cc+
            self.aug+
            self.mo+
            self.ec+
            self.am+
            self.mu+
            self.az+
            self.gen+
            self.de+
            self.vol+
            self.fu+
            self.der+
            self.ken+
            self.dip+
            self.fuc+
            self.du+
            self.dup+
            self.ez+
            self.mov+
            self.no+
            self.do+
            self.vas+
            self.cl+
            self.niv+
            self.lo+
            self.fl+
            self.ol+
            self.cp
        )
        self.order.set(str(self.totalieto)+" $")
def log() :
    user = en1.get()
    password = en2.get()
    if user == "noor" and password == "123456"  :
        messagebox.showinfo("Hello" , "Welcome Sir")
        root=Tk()
        ap=Ph(root)
        root.mainloop()
    else :
        messagebox.showerror("Error", "The username or password is not correct")
title4=Label(f2, text="Username :" ,  bg="pink" , fg="white" , font=("leelawadee" , 20 , "bold"))
title4.place(x=30 , y=25)
title5=Label(f2 , text="Password :" , bg="pink" , fg="white" , font=("leelawadee" , 20 , "bold"))
title5.place(x=30 , y=80)
en1 = Entry(f2, font=("leelawadee" , 15) , justify="center")
en1.place(x=183,y=34)
en2=Entry(f2, font=("leelawadee" , 15), justify="center" ,)
en2.place(x=183 , y= 87)
b=Button(f2, text="Log in", bg="light blue" , fg="white", font=("leelawadee" , 20 ) , width=9 , height = 0 , command = log)
b.place(x=420 , y=50)
pro.mainloop()