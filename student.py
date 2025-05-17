#STUDENT CODE
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import mediapipe as mp
import numpy as np
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        
        #------------------variables--------------
        self.var_roll=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_par=StringVar()
        self.var_dob=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_address=StringVar()
        self.var_date=StringVar()
        self.var_radio1=StringVar()
       
         #IMAGE 1

        img1=Image.open("back3.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # IMAGE 2

        img2=Image.open("back3.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #IMAGE 3
        img3=Image.open("back3.jpg")
        img3=img3.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)
     
        # BACKGROUND IMAGE
        img4=Image.open("back3.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("TimesNew Roman",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=1,background="lightblue")
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

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        dep_combo['values'] = ['Select Department','CSE', 'IT', 'ECE', 'MECH','CIVIL', 'CHE', 'EEE','BSC-IT','PHARMACY','ARCHITECTURE']
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #Year INFO
        course_label = Label(current_course_frame,text="Current Year:",font=("Times New Roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        course_combo['values'] = ['Select Year','FE', 'SE', 'TE', 'BE']
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester INFO
        sem_label = Label(current_course_frame,text="Current Semester:",font=("Times New Roman",14,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        sem_combo['values'] = ['Current Semester','FirstHalf', 'SecondHalf']
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Class info
        class_frame=Label(left_frame,bd=2,background="white",relief=RIDGE,text="",font=("Times New Roman",12,"bold"))
        class_frame.place(x=5,y=170,width=720,height=450)
    
        #Student Id INFO
        stu_id_label = Label(class_frame,text="Student ID:",font=("Times New Roman",13,"bold"))
        stu_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        stu_id_entry=ttk.Entry(class_frame,textvariable=self.var_roll,width=15,font=("Times New Roman",14,"bold"))
        stu_id_entry.grid(row=0,column=1,padx=10,pady=10)

        #Student NAME INFO
        stu_Name_label = Label(class_frame,text="Student Name:",font=("Times New Roman",13,"bold"))
        stu_Name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        stu_Name_entry=ttk.Entry(class_frame,textvariable=self.var_std_name,width=15,font=("Times New Roman",14,"bold"))
        stu_Name_entry.grid(row=1,column=1,padx=10,pady=10)
        
        #Gender
        Gen_label = Label(class_frame,text="Gender :",font=("Times New Roman",13,"bold"))
        Gen_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        Gen_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=("Times New Roman",12,"bold"),width=17,state="readonly")
        Gen_combo['values'] = ('Gender :','Male', 'Female')
        Gen_combo.current(0)
        Gen_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Student Email INFO
        stu_Email_label = Label(class_frame,text="Student Email:",font=("Times New Roman",13,"bold"))
        stu_Email_label.grid(row=0,column=2,padx=8,pady=10,sticky=W)

        stu_Email_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=15,font=("Times New Roman",14,"bold"))
        stu_Email_entry.grid(row=0,column=3,padx=8,pady=10)

        #Student phone INFO
        stu_phone_label = Label(class_frame,text="Student's ContactNo:",font=("Times New Roman",13,"bold"))
        stu_phone_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        stu_phone_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=15,font=("Times New Roman",14,"bold"))
        stu_phone_entry.grid(row=4,column=1,padx=10,pady=10)

        #Student par INFO
        stu_par_label = Label(class_frame,text="Parents ContactNo:",font=("Times New Roman",13,"bold"))
        stu_par_label.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        stu_par_entry=ttk.Entry(class_frame,textvariable=self.var_par,width=15,font=("Times New Roman",14,"bold"))
        stu_par_entry.grid(row=4,column=3,padx=5,pady=10)
        
        #Student Address INFO
        stu_add_label = Label(class_frame,text="Current Address:",font=("Times New Roman",13,"bold"))
        stu_add_label.grid(row=6,column=0,padx=5,pady=10,sticky=W)

        stu_add_entry=ttk.Entry(class_frame,textvariable=self.var_address,width=15,font=("Times New Roman",14,"bold"))
        stu_add_entry.grid(row=6,column=1,padx=5,pady=10)
        
        #Student DOB INFO
        stu_dob_label = Label(class_frame,text="DOB:",font=("Times New Roman",13,"bold"))
        stu_dob_label.grid(row=6,column=2,padx=5,pady=10,sticky=W)

        stu_dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=15,font=("Times New Roman",14,"bold"))
        stu_dob_entry.grid(row=6,column=3,padx=5,pady=10)

        # DATE
        date_label = Label(class_frame,text="Current date:",font=("Times New Roman",13,"bold"))
        date_label.grid(row=7,column=0,padx=5,pady=10,sticky=W)

        date_entry=ttk.Entry(class_frame,textvariable=self.var_date,width=15,font=("Times New Roman",14,"bold"))
        date_entry.grid(row=7,column=1,padx=5,pady=10)

        #RADIO BUTTON
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="TAKE PHOTO",value="Yes")
        radio1.grid(row=8,column=0,padx=5,pady=10,sticky=W)

        #RADIO BUTTON
        self.var_radio2=StringVar()
        radio2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="NO PHOTO",value="No")
        radio2.grid(row=8,column=1,padx=5,pady=10,sticky=W)
        
        #BUTTON frame
 
        save_btn=Button(class_frame,command=self.add_data,text="Save",width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        save_btn.grid(row=10,column=0,pady=10)

        Update_btn=Button(class_frame,text="Update",command=self.update_data,width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        Update_btn.grid(row=10,column=1,pady=10)
   
        Delete_btn=Button(class_frame,text="Delete",command=self.del_data,width=10,font=("Times New Roman",13,"bold"),bg="red",fg="white")
        Delete_btn.grid(row=10,column=2,pady=10)
        
        photo_btn=Button(class_frame,text="Take Photo",command=self.generate_dataset,width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        photo_btn.grid(row=8,column=2,pady=10)

        upd_btn=Button(class_frame,text="Update sample",width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        upd_btn.grid(row=8,column=3,pady=10)

        reset_btn=Button(class_frame,text="Reset",command=self.reset_data,width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        reset_btn.grid(row=10,column=3,pady=10)
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,background="white",relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)
         
        img_right=Image.open("detail.png")
        img_right=img_right.resize((650,120),Image.Resampling.LANCZOS)
        self.photo_img_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photo_img_right)
        f_lbl.place(x=5,y=0,width=650,height=120)

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

        save_btn=Button(search_frame,text="Search",width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        save_btn.grid(row=0,column=3,padx=10,pady=10)

        show_btn=Button(search_frame,text="ShowAll",width=10,font=("Times New Roman",13,"bold"),bg="navyblue",fg="lightblue")
        show_btn.grid(row=0,column=4,padx=10,pady=10)

        #------------TABLE FRAME----------
        table_frame=Frame(right_frame,bd=2,background="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=705,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("RollNo","Name","Gender","EmailId","PhoneNo","ParentsContactNo","DateofBirth","Dep","Year","Semester","Address","Date","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)       

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("RollNo",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("EmailId",text="Email-Id")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("ParentsContactNo",text="Parents Contact No")
        self.student_table.heading("DateofBirth",text="Date of Birth")
        self.student_table.heading("Dep",text="Dep")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Date",text=" Date")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("RollNo",width=100)
        self.student_table.column("Name",width=150)
        self.student_table.column("Gender",width=100)
        self.student_table.column("EmailId",width=150)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("ParentsContactNo",width=150)
        self.student_table.column("DateofBirth",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Address",width=200)
        self.student_table.column("Date",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #-----------------------function declaration---------------------------

    def add_data(self):
       if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_roll.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
       else:
        try:
             # Establish database connection
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Naur@100",
                database="face_recog"
            )
            mycursor = conn.cursor()  # ✅ Create a cursor before executing queries

            # Correcting the SQL insert statement
            mycursor.execute("""
                INSERT INTO student (
                    RollNo,Name,Gender,EmailId,PhoneNo,ParentsContactNo,DateofBirth,Dep,Year,Semester,Address,Date,Photo
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_roll.get(),
                self.var_std_name.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_par.get(),
                self.var_dob.get(),
                self.var_dep.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_address.get(),
                self.var_date.get(),
                self.var_radio1.get()      
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Successful", "Student details have been added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

 #-------------------------FETCH DATA-------------------------------
           

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Naur@100",database="face_recog")           
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        

   #=========================get cursor=======================
    def get_cursor(self,event=""):
      cursor_focus = self.student_table.focus()
      content = self.student_table.item(cursor_focus)
      data = content["values"]
        # Ensure row is not empty
      self.var_roll.set(data[0]),  # ✅ Roll Number
      self.var_std_name.set(data[1]),  # ✅ Name
      self.var_gender.set(data[2]) , # ✅ Gender
      self.var_email.set(data[3]) , # ✅ Email
      self.var_phone.set(data[4]) , # ✅ Phone Number
      self.var_par.set(data[5]),  # ✅ Parent's Contact
      self.var_dob.set(data[6]),  # ✅ DOB
      self.var_dep.set(data[7]) , # ✅ Department
      self.var_year.set(data[8]) ,
      self.var_semester.set(data[9]) , # ✅ Semester# ✅ Year
      self.var_address.set(data[10]),  # ✅ Address
      self.var_date.set(data[11]) , # ✅ Date
      self.var_radio1.set(data[12]) , # ✅ Photo status
        
        

#update
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_roll.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Naur@100",
                        database="face_recog")           
                    mycursor=conn.cursor()
                    mycursor.execute("UPDATE student SET Name=%s,Gender=%s,EmailId=%s,PhoneNo=%s,ParentsContactNo=%s,DateofBirth=%s,Dep=%s,Year=%s,Semester=%s,Address=%s,Date=%s,Photo=%s WHERE RollNo=%s",(
                            
                                                                                    self.var_std_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_par.get(),
                                                                                    self.var_dob.get(),  
                                                                                    self.var_dep.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_date.get(),
                                                                                    self.var_radio1.get(),
                                                                                    self.var_roll.get() # Corrected roll number reference
                             ))
                    messagebox.showinfo("Sucess","Student details sucessfully updates!",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                   if not update:
                        return  
                   
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

    #   ---------delete function
    def del_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Naur@100",database="face_recog")           
                    mycursor=conn.cursor()
                    sql="DELETE FROM student WHERE RollNo=%s"
                    val=(self.var_roll.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete :
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
    def reset_data(self):
  
                        self.var_roll.set("")
                        self.var_std_name.set("")
                        self.var_gender.set("Male")
                        self.var_email.set("")
                        self.var_phone.set("")
                        self.var_par.set("")
                        self.var_dob.set("") 
                        self.var_dep.set("Select Department")
                        self.var_year.set("Select year")
                        self.var_semester.set("Select Semester")   
                        self.var_address.set("")
                        self.var_date.set("")
                        self.var_radio1.set("") 
                                         
        # GENERATE DATA SET AND TAKE PHOTO SAMPLES
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_roll.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Update student data in database
                id = self.var_roll.get()
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Naur@100",
                    database="face_recog"
                )
                mycursor = conn.cursor()
                
                mycursor.execute("""
                    UPDATE student SET 
                        Name=%s, Gender=%s, EmailId=%s, PhoneNo=%s, 
                        ParentsContactNo=%s, DateofBirth=%s, Dep=%s, 
                        Year=%s, Semester=%s, Address=%s, Date=%s, Photo=%s 
                    WHERE RollNo=%s
                    """, (
                        self.var_std_name.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_par.get(),
                        self.var_dob.get(),  
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_address.get(),
                        self.var_date.get(),
                        self.var_radio1.get(),
                        self.var_roll.get()
                    ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Initialize MediaPipe Face Mesh
                mp_face_mesh = mp.solutions.face_mesh
                face_mesh = mp_face_mesh.FaceMesh(
                    max_num_faces=1,
                    refine_landmarks=True,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5
                )

                # Define eye landmark indices (MediaPipe)
                LEFT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
                RIGHT_EYE_INDICES = [33, 160, 158, 133, 153, 144]

                def is_eye_open(landmarks, eye_indices):
                    """Check if eye is open using EAR (Eye Aspect Ratio)"""
                    # Get eye landmarks
                    eye_points = [(landmarks[i].x, landmarks[i].y) for i in eye_indices]
                    
                    # Calculate EAR
                    # Horizontal eye distance
                    ear_horizontal = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))
                    # Vertical eye distances
                    ear_vertical1 = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))
                    ear_vertical2 = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))
                    
                    ear = (ear_vertical1 + ear_vertical2) / (2.0 * ear_horizontal)
                    
                    # Threshold for open eye (adjust as needed)
                    return ear > 0.25

                def get_face_roi(frame, landmarks):
                    """Get face region of interest from landmarks"""
                    h, w = frame.shape[:2]
                    landmark_points = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks.landmark]
                    x_coords = [p[0] for p in landmark_points]
                    y_coords = [p[1] for p in landmark_points]
                    
                    x_min, x_max = min(x_coords), max(x_coords)
                    y_min, y_max = min(y_coords), max(y_coords)
                    
                    # Add some padding
                    padding = 20
                    x_min = max(0, x_min - padding)
                    y_min = max(0, y_min - padding)
                    x_max = min(w, x_max + padding)
                    y_max = min(h, y_max + padding)
                    
                    return frame[y_min:y_max, x_min:x_max]

                # Start capturing images
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Could not access the camera", parent=self.root)
                    return

                img_id = 0
                sample_count = 0
                required_samples = 50  # Number of samples to collect

                while sample_count < required_samples:
                    ret, frame = cap.read()
                    if not ret:
                        continue

                    # Convert to RGB for MediaPipe
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = face_mesh.process(frame_rgb)

                    if results.multi_face_landmarks:
                        for face_landmarks in results.multi_face_landmarks:
                            # Check if both eyes are open
                            left_eye_open = is_eye_open(face_landmarks.landmark, LEFT_EYE_INDICES)
                            right_eye_open = is_eye_open(face_landmarks.landmark, RIGHT_EYE_INDICES)

                            if left_eye_open and right_eye_open:
                                # Get face ROI
                                face_roi = get_face_roi(frame, face_landmarks)
                                
                                if face_roi.size > 0:
                                    # Resize and convert to grayscale
                                    face_roi = cv2.resize(face_roi, (550, 550))
                                    gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                                    
                                    # Save the image
                                    img_id += 1
                                    file_name_path = f"data/user.{id}.{img_id}.jpg"
                                    cv2.imwrite(file_name_path, gray_face)
                                    
                                    # Display the captured face
                                    cv2.putText(frame, f"Samples: {img_id}/{required_samples}", 
                                            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                    
                                    # Draw face landmarks for visualization
                                    mp.solutions.drawing_utils.draw_landmarks(
                                        image=frame,
                                        landmark_list=face_landmarks,
                                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                                        landmark_drawing_spec=None,
                                        connection_drawing_spec=mp.solutions.drawing_styles
                                        .get_default_face_mesh_contours_style()
                                    )
                                    
                                    sample_count += 1

                    # Display the frame
                    cv2.imshow("Capturing Face Dataset - Press ESC to exit", frame)
                    
                    # Check for exit key (ESC) or when we have enough samples
                    if cv2.waitKey(1) == 27 or sample_count >= required_samples:
                        break

                # Clean up
                cap.release()
                cv2.destroyAllWindows()
                face_mesh.close()
                
                messagebox.showinfo("Success", f"Successfully captured {sample_count} face samples", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            # def generate_dataset(self):
        #     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_roll.get()=="":
        #     messagebox.showerror("Error","All Fields are required",parent=self.root)
        #     else:
        #         try:
        #             id=self.var_roll.get()
        #             conn=mysql.connector.connect(host="localhost",username="root",password="Naur@100",database="face_recog")           
        #             mycursor=conn.cursor()
                
        #             mycursor.execute("UPDATE student SET Name=%s,Gender=%s,EmailId=%s,PhoneNo=%s,ParentsContactNo=%s,DateofBirth=%s,Dep=%s,Year=%s,Semester=%s,Address=%s,Date=%s,Photo=%s where RollNo=%s",(
                        
        #                     self.var_std_name.get(),
        #                     self.var_gender.get(),
        #                     self.var_email.get(),
        #                     self.var_phone.get(),
        #                     self.var_par.get(),
        #                     self.var_dob.get(),  
        #                     self.var_dep.get(),
        #                     self.var_year.get(),
        #                     self.var_semester.get(),
        #                     self.var_address.get(),
        #                     self.var_date.get(),
        #                     self.var_radio1.get(),
        #                     self.var_roll.get()
        #                     ))
        #             conn.commit()
        #             self.fetch_data()
        #             self.reset_data()
        #             conn.close()
        #             # --------------------LOAD PREDEFINED DATA ON FACE----------------
        #             face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #             def face_cropped(img):
        #                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #                 faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        
        #                 cropped_faces = []
        #                 for (x,y,w,h) in faces:
        #                     face_roi = img[y:y+h, x:x+w]
        #                     gray_roi = gray[y:y+h, x:x+w]
                            
        #                     # Detect eyes within the face region
        #                     eyes = eye_classifier.detectMultiScale(gray_roi, 1.1, 5)
                            
        #                     # Only accept faces with at least 2 detected eyes
        #                     if len(eyes) >= 2:
        #                         # Draw rectangle around eyes (for visualization)
        #                         for (ex,ey,ew,eh) in eyes:
        #                             cv2.rectangle(face_roi, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
                                
        #                         cropped_faces.append(face_roi)
        #                         return face_roi
        #                 return None
                        
        #             cap = cv2.VideoCapture(0)
        #             if not cap.isOpened():
        #                 print("Error: Could not access the camera")
        #                 return
                        
        #             img_id = 0
        #             while True:
        #                 ret, my_frame = cap.read()
        #                 if not ret:
        #                     break
                            
        #                 cropped_face = face_cropped(my_frame)
        #                 if cropped_face is not None:
        #                     img_id += 1
        #                     face = cv2.resize(cropped_face, (550,550))
        #                     face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        #                     file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
        #                     cv2.imwrite(file_name_path, face)
        #                     cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
        #                     cv2.imshow("Cropped Face with Eyes", face)

        #                 if cv2.waitKey(1) == 13 or int(img_id) == 50:
        #                     break
                            
        #             cap.release()
        #             cv2.destroyAllWindows()
        #             messagebox.showinfo("Result","Generating data sets completed!")
                
        #         except Exception as es:
        #             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    def is_eye_closed(self, landmarks, eye_indices):
        """Check if eye is closed using EAR (Eye Aspect Ratio)"""
        # Get eye landmarks
        eye_points = [(landmarks[i].x, landmarks[i].y) for i in eye_indices]
        
        # Calculate EAR
        # Horizontal eye distance
        ear_horizontal = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))
        # Vertical eye distances
        ear_vertical1 = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))
        ear_vertical2 = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))
        
        ear = (ear_vertical1 + ear_vertical2) / (2.0 * ear_horizontal)
        
        # Threshold for closed eye (adjust as needed)
        return ear < 0.2
                #     def face_cropped(img):
            #         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #         faces=face_classifier.detectMultiScale(gray,1.3,5)
            #         cropped_faces = []
            #         for (x,y,w,h) in faces:
            #             face_cropped=img[y:y+h,x:x+w]
            #             cropped_faces.append(face_cropped)
            #             return face_cropped
            #     cap=cv2.VideoCapture(0)
            #     if not cap.isOpened():
            #        print("Error: Could not access the camera")
            #        return
            #     img_id=0
            #     while True:
            #         ret,my_frame=cap.read()
            #         cropped_face = face_cropped(my_frame)
            #         if face_cropped(my_frame) is not None:
            #             img_id+=1
            #             face=cv2.resize(face_cropped(my_frame),(550,550))
            #             face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            #             file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
            #             cv2.imwrite(file_name_path,face)
            #             cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
            #             cv2.imshow("Cropped Face",face)

            #         if cv2.waitKey(1)==13 or int(img_id)==50:
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()
            #     messagebox.showinfo("Result","Generating data sets completed!")
            # except Exception as es:
            #     messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()








































if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
