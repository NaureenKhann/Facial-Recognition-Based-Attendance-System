from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
   

         #IMAGE 1

        img1=Image.open("C:/Users/naure/OneDrive/Desktop/CODING/Python Projects/attendence System/lightgreen.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # IMAGE 2

        img2=Image.open("C:/Users/naure/OneDrive/Desktop/CODING/Python Projects/attendence System/lightgreen.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #IMAGE 3
        img3=Image.open("C:/Users/naure/OneDrive/Desktop/CODING/Python Projects/attendence System/lightgreen.jpeg")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)
     
        # BACKGROUND IMAGE
        img4=Image.open("C:/Users/naure/OneDrive/Desktop/CODING/Python Projects/attendence System/lightgreen.jpeg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("TimesNew Roman",35,"bold"),bg="white",fg="lightgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=1,background="lightgreen")
        main_frame.place(x=10,y=55,width=1500,height=600)
  
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,background="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        left_frame.place(x=10,y=10,width=735,height=580)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,background="white",relief=RIDGE,text="Current Course Info",font=("Times New Roman",12,"bold"))
        current_course_frame.place(x=5,y=20,width=720,height=130)
        #DEPARTMENT
        dep_label = Label(current_course_frame,text="Department:",font=("Times New Roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        dep_combo['values'] = ['Select Department','CSE', 'IT', 'ECE', 'MECH','CIVIL', 'CHE', 'EEE','BSC-IT','PHARMACY','ARCHITECTURE']
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #Year INFO
        course_label = Label(current_course_frame,text="Current Year:",font=("Times New Roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        course_combo['values'] = ['Select Year','FE', 'SE', 'TE', 'BE']
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester INFO
        sem_label = Label(current_course_frame,text="Current Semester:",font=("Times New Roman",14,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        sem_combo['values'] = ['Current Semester','FirstHalf', 'SecondHalf']
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Class info
        class_frame=Label(left_frame,bd=2,background="white",relief=RIDGE,text="",font=("Times New Roman",12,"bold"))
        class_frame.place(x=5,y=170,width=720,height=450)
    
        #Student Id INFO
        stu_id_label = Label(class_frame,text="Student ID:",font=("Times New Roman",13,"bold"))
        stu_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        stu_id_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_id_entry.grid(row=0,column=1,padx=10,pady=10)

        #Student NAME INFO
        stu_Name_label = Label(class_frame,text="Student Name:",font=("Times New Roman",13,"bold"))
        stu_Name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        stu_Name_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_Name_entry.grid(row=1,column=1,padx=10,pady=10)
        
        #Gender
        Gen_label = Label(class_frame,text="Gender :",font=("Times New Roman",13,"bold"))
        Gen_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        Gen_combo=ttk.Combobox(class_frame,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        Gen_combo['values'] = ['Gender :','Male', 'Female']
        Gen_combo.current(0)
        Gen_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Student Email INFO
        stu_Email_label = Label(class_frame,text="Student Email:",font=("Times New Roman",13,"bold"))
        stu_Email_label.grid(row=0,column=2,padx=8,pady=10,sticky=W)

        stu_Email_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_Email_entry.grid(row=0,column=3,padx=8,pady=10)

        #Student phone INFO
        stu_phone_label = Label(class_frame,text="Student's ContactNo:",font=("Times New Roman",13,"bold"))
        stu_phone_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        stu_phone_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_phone_entry.grid(row=4,column=1,padx=10,pady=10)

        #Student par INFO
        stu_par_label = Label(class_frame,text="Parents ContactNo:",font=("Times New Roman",13,"bold"))
        stu_par_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        stu_par_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_par_entry.grid(row=4,column=3,padx=5,pady=10)
        
        #Student Address INFO
        stu_add_label = Label(class_frame,text="Current Address:",font=("Times New Roman",13,"bold"))
        stu_add_label.grid(row=6,column=0,padx=5,pady=10,sticky=W)

        stu_add_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_add_entry.grid(row=6,column=1,padx=5,pady=10)
        
        #Student DOB INFO
        stu_dob_label = Label(class_frame,text="DOB:",font=("Times New Roman",13,"bold"))
        stu_dob_label.grid(row=6,column=2,padx=5,pady=10,sticky=W)

        stu_dob_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        stu_dob_entry.grid(row=6,column=3,padx=5,pady=10)

        # DATE
        date_label = Label(class_frame,text="Current date:",font=("Times New Roman",13,"bold"))
        date_label.grid(row=7,column=0,padx=5,pady=10,sticky=W)

        date_entry=ttk.Entry(class_frame,width=15,font=("Times New Roman",14,"bold"))
        date_entry.grid(row=7,column=1,padx=5,pady=10)
        #RADIO BUTTON
        radio1=ttk.Radiobutton(class_frame,text="TAKE PHOTO",value="Yes")
        radio1.grid(row=8,column=0,padx=5,pady=10,sticky=W)

        #RADIO BUTTON
        radio2=ttk.Radiobutton(class_frame,text="NO PHOTO",value="Yes")
        radio2.grid(row=8,column=1,padx=5,pady=10,sticky=W)
        
        #BUTTON frame

        save_btn=Button(class_frame,text="Save",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        save_btn.grid(row=10,column=0,pady=10)

        Update_btn=Button(class_frame,text="Update",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        Update_btn.grid(row=10,column=1,pady=10)
   
        Delete_btn=Button(class_frame,text="Delete",width=10,font=("Times New Roman",13,"bold"),bg="red",fg="white")
        Delete_btn.grid(row=10,column=2,pady=10)
        
        photo_btn=Button(class_frame,text="Take Photo",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        photo_btn.grid(row=8,column=2,pady=10)

        upd_btn=Button(class_frame,text="Update sample",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        upd_btn.grid(row=8,column=3,pady=10)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,background="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)
         
        img_right=Image.open("C:/Users/naure/OneDrive/Desktop/CODING/Python Projects/attendence System/lightpurple.jpeg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photo_img_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photo_img_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

       #------------SEARCH SYSTEM----------
        search_frame=LabelFrame(right_frame,bd=2,background="white",relief=RIDGE,text="Search System",font=("Times New Roman",12,"bold"))
        search_frame.place(x=5,y=130,width=705,height=70)

        search_label = Label(search_frame,text="Search",font=("Times New Roman",13,"bold"),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        search_combo['values'] = ['Select :','Roll No', 'PhoneNo']
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("Times New Roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=10)

        save_btn=Button(search_frame,text="Save",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        save_btn.grid(row=0,column=3,padx=10,pady=10)

        show_btn=Button(search_frame,text="ShowAll",width=10,font=("Times New Roman",13,"bold"),bg="lightgreen",fg="white")
        show_btn.grid(row=0,column=4,padx=10,pady=10)

        #------------TABLE FRAME----------
        table_frame=Frame(right_frame,bd=2,background="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=705,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Roll No","Name","Gender","Email","PhoneNo","ParentsContactNo","DateofBirth","dep","year","Address","Current Date","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)       

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email-Id")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("ParentsContactNo",text="Parents Contact No")
        self.student_table.heading("DateofBirth",text="Date of Birth")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("Address",text="Adress")
        self.student_table.heading("Current Date",text=" Date")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Roll No",width=100)
        self.student_table.column("Name",width=150)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=150)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("ParentsContactNo",width=150)
        self.student_table.column("DateofBirth",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("Address",width=200)
        self.student_table.column("Current Date",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)






















































if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()