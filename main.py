from tkinter import*
from tkinter import ttk
from turtle import color
from PIL import Image,ImageTk
from numpy import place
from student import Student
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(text="Face Recognition Attendance System",font=("times new roman",35,"bold"),fg="green",justify="center")
        title_lbl.place(x=0,y=0,width=1300,height=60)
        
        #top img1
        img=Image.open(r"Image\imagelabel.jfif")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=60,width=400,height=130)

        #top img2
        img1=Image.open(r"Image\imagelabel2.jfif")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=60,width=500,height=130)

        #top img3
        img2=Image.open(r"Image\imagelabel3.jfif")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=60,width=400,height=130)

        #bg img
        imgbg=Image.open(r"Image\bg.jpg")
        imgbg=imgbg.resize((1500,1000),Image.Resampling.LANCZOS)
        self.photoimgbg=ImageTk.PhotoImage(imgbg)
        f_lbl=Label(self.root,image=self.photoimgbg)
        f_lbl.place(x=0,y=190,width=1500,height=1000)
        
        #student button
        b1=Button(cursor="hand2",text="student details",command=self.student_details)
        b1.place(x=750,y=350,width=100,height=40)

        #=============function==========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
