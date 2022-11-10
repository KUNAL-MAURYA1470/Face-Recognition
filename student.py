from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import color
from typing_extensions import Self
from webbrowser import get
from PIL import Image,ImageTk
from numpy import place
from pyparsing import col
from tkinter import messagebox
import mysql.connector
from soupsieve import escape

class Student:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("face Recogniton System")

        #==============Variables================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()

        imgbg=Image.open(r"Image\bg.jpg")
        imgbg=imgbg.resize((1300,700),Image.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
        f_lbl=Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=0,width=1300,height=700)

        title_lbl = Label(text="Student Management System",font=("times new roman",35,"bold"),fg="green",justify="center")
        title_lbl.place(x=0,y=0,width=1300,height=60)

        main_frame = Frame(bd=2)
        main_frame.place(x=10,y=70,width=1260,height=580)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=550)

        #current course
        course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Details",font=("times new roman",12,"bold"))
        course_frame.place(x=10,y=10,width=590,height=150)

        #department
        dep_label=Label(course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course

        course_label=Label(course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","1st year","2nd year","3rd year","4th year")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year

        year_label=Label(course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #sem

        sem_label=Label(course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Sem","1st ","2nd ","3rd ","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student information

        class_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_frame.place(x=10,y=180,width=590,height=340)

        #student Id

        studentId_label=Label(class_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentId_entry=ttk.Entry(class_frame,textvariable=self.var_id,width=18,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student name

        studentName_label=Label(class_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=7,pady=10,sticky=W)

        studentName_entry=ttk.Entry(class_frame,textvariable=self.var_name,width=18,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=7,pady=10,sticky=W)

        #class divison

        classdiv_label=Label(class_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        classdiv_entry=ttk.Entry(class_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"))
        classdiv_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Roll no

        roll_label=Label(class_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=7,pady=10,sticky=W)

        roll_entry=ttk.Entry(class_frame,textvariable=self.var_rollno,width=18,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=7,pady=10,sticky=W)

        #gender

        Gender_label=Label(class_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        Gender_entry=ttk.Entry(class_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"))
        Gender_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Email

        Email_label=Label(class_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=2,column=2,padx=7,pady=10,sticky=W)

        Email_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=18,font=("times new roman",12,"bold"))
        Email_entry.grid(row=2,column=3,padx=7,pady=10,sticky=W)

        #DOB

        dOB_label=Label(class_frame,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
        dOB_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        dOB_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=18,font=("times new roman",12,"bold"))
        dOB_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Phone

        Phone_label=Label(class_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=7,pady=10,sticky=W)

        Phone_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=18,font=("times new roman",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=7,pady=10,sticky=W)


        #radio Buttons
        radionbtn1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)
        
        #bbuttons frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=580,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=250,width=580,height=35)

        take_photo_btn=Button(btn_frame2,text="Take photo sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame2,text="Update photo sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        

        




        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=600,height=550)

        #search System

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=10,width=580,height=100)

        search_label=Label(search_frame,text="Search By ",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select ","Student Id ","rollno ","phoneno ")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=1,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=1,column=1)

        showall_btn=Button(search_frame,text="Show all",width=14,font=("times new roman",11,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=1,column=2)

        #===========tableframwe=========
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=120,width=580,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","rollno","gender","email","dob","phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="StudentName")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        #================function================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="facerecognition")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_course.get(),
                                                                                                       self.var_year.get(),
                                                                                                       self.var_sem.get(),
                                                                                                       self.var_id.get(),
                                                                                                       self.var_name.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_dob.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_div.get(),
                                                                                                       self.var_rollno.get(),
                                                                                                       self.var_radio1.get()


                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                    messagebox.showerror("error",f"Due to :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="facerecognition")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
       
        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()