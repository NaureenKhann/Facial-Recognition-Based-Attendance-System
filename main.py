from tkinter import*
from tkinter import ttk
import os
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from time import strftime
from datetime import datetime
from face_recognition import Face_Recogition
from developer import Developer
from attendance import Attendance
from help import HELP
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #IMAGE 1

        img1=Image.open("shade2.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # IMAGE 2

        img2=Image.open("shade2.png")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #IMAGE 3
        img3=Image.open("shade2.png")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # BACKGROUND IMAGE
        img4=Image.open("tech4.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Face Recognition based Attendence System",font=("TimesNew Roman",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def time():
          string=strftime('%H:%M:%S %p')  
          lbl.config(text=string)
          lbl.after(1000,time)
      
        lbl=Label(title_lbl,font=('times new roman','14','bold'),background='white',foreground='navyblue')
        lbl.place(x=0,y=0,width=110,height=70)
        time()
        #button 1
        img5=Image.open("studentneww.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=150,y=300,width=220,height=40)

        #button 2
        img6=Image.open("faces.jpeg")
        img6=img6.resize((230,210),Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=450,y=100,width=220,height=220)

        b2_2=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b2_2.place(x=450,y=300,width=220,height=40)

        #button 3
        img7=Image.open("atten11.png")
        img7=img7.resize((230,220),Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b3=Button(bg_img,image=self.photoimg7,command=self.attendance_data,cursor="hand2")
        b3.place(x=750,y=100,width=220,height=220)

        b3_3=Button(bg_img,text="attendance",cursor="hand2",command=self.attendance_data,font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b3_3.place(x=750,y=300,width=220,height=40)

        #button 4
        img8=Image.open("support.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b4=Button(bg_img,image=self.photoimg8,command=self.help,cursor="hand2")
        b4.place(x=1050,y=100,width=220,height=220)

        b4_4=Button(bg_img,text="Help Desk",command=self.help,cursor="hand2",font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b4_4.place(x=1050,y=300,width=220,height=40)

        #button 5
        img9=Image.open("datatrain.jpg")
        img9=img9.resize((260,260),Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=150,y=380,width=220,height=220)

        b5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b5_5.place(x=150,y=580,width=220,height=40)

        #button 6
        img10=Image.open("photo.jpeg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=450,y=380,width=220,height=220)

        b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b6_6.place(x=450,y=580,width=220,height=40)

        #button 7
        img11=Image.open("about us.jpeg")
        img11=img11.resize((230,240),Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b7=Button(bg_img,image=self.photoimg11,command=self.dev_data,cursor="hand2")
        b7.place(x=750,y=380,width=220,height=220)

        b7_7=Button(bg_img,text="developer/about us",command=self.dev_data,cursor="hand2",font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b7_7.place(x=750,y=580,width=220,height=40)
       
         #button 8
        img12=Image.open("exit.png")
        img12=img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        b8=Button(bg_img,image=self.photoimg12,command=self.exit,cursor="hand2")
        b8.place(x=1050,y=380,width=220,height=220)

        b8_8=Button(bg_img,text="exit",cursor="hand2",command=self.exit,font=("TimesNew Roman",15,"bold"),bg="white",fg="black")
        b8_8.place(x=1050,y=580,width=220,height=40)
   
    def exit(self):
      self.exit=tkinter.messagebox.askyesno("Face recognition","Are you sure you want to exit this project??",parent=self.root)
      if self.exit > 0:
        self.root.destroy()
      else:
        return       
    def  open_img(self):
        os.startfile("data")
    
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.apps=Student(self.new_window)  
      
    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.apps=Train(self.new_window)  
      
    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.apps=Face_Recogition(self.new_window)  
      
    def dev_data(self):
      self.new_window=Toplevel(self.root)
      self.apps=Developer(self.new_window) 
       
    def attendance_data(self):
      self.new_window=Toplevel(self.root)
      self.apps=Attendance(self.new_window) 
      
    def help(self):
      self.new_window=Toplevel(self.root)
      self.apps=HELP(self.new_window) 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

     #--------------function buttons---------------------
     
