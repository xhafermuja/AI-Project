from tkinter import *
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=======================VARIABLES==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



        #BG IMG
        bg_img = Image.open('images/ai.jpeg')
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bg_img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        #TITLE
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Courier New", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #MAIN FRAME
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=50, y=100, width=1430, height=650)

        #LEFT LABEL FRAME
        left_frame= LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=20,y=10,width=715,height=580)

        left_img = Image.open('images/Logo_UPZ_Final.jpg')
        left_img = left_img.resize((710, 150), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        f_lbl=Label(left_frame, image= self.photoimg_left)
        f_lbl.place(x=0, y=0, width=710, height=150)

        #CURRENT COURSE
        current_course_frame= LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5,y=115,width=700,height=150)

        #DEPARTMENT
        dep_label=Label(current_course_frame, text="Departament", font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo= ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"]=("Select Department", "Fakulteti i Shkencave Kompjuterike", "Fakulteti i Filologjisë", "Fakulteti Ekonomik", "Fakulteti i Shkencave të Jetës dhe Mjedisit", "Fakulteti i Edukimit", "Fakulteti Juridik")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        #COURSE
        course_label=Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo= ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"]=("Select Program", "FSHK-SD", "FSHK-TIT", "FIL-Shq", "FIL-Ang", "FIL-Gje", "FE-AB", "FE-MN", "FJ-JP")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        #YEAR
        year_label=Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo= ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"]=("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        #SEMESTER
        semester_label=Label(current_course_frame,  text="Semester", font=("times new roman", 12, "bold"),bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo= ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"]=("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

        #CLASS STUDENT
        class_student_frame= LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5,y=270,width=700,height=280)

        #STUDENT ID
        studentID_label=Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"),bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=17, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)

        #STUDENT NAME
        studentName_label=Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=17, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)

        #CLASS DIVISION
        class_div_label=Label(class_student_frame, text="Student Division:", font=("times new roman", 12, "bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo= ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"),width=15, state="readonly")
        div_combo["values"]=("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1, padx=10, pady=5, sticky=W)

        #ROLL NO
        roll_no_label=Label(class_student_frame, text="Student No:", font=("times new roman", 12, "bold"),bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame, textvariable=self.var_roll, width=17, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1,column=3, padx=10, pady=5, sticky=W)

        #GENDER
        gender_label=Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo= ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=15, state="readonly")
        gender_combo["values"]=("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1, padx=10, pady=5, sticky=W)

        #DOB
        dob_label=Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob, width=17, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2,column=3, padx=10, pady=5, sticky=W)

        #EMAIL
        email_label=Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry=ttk.Entry(class_student_frame, textvariable=self.var_email, width=17, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3,column=1, padx=10, pady=5, sticky=W)

        #PHONE NO
        phone_label=Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry=ttk.Entry(class_student_frame, textvariable=self.var_phone, width=17, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3,column=3, padx=10, pady=5, sticky=W)

        #ADDRESS
        address_label=Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry=ttk.Entry(class_student_frame, textvariable=self.var_address, width=17, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4,column=1, padx=10, pady=5, sticky=W)

        #TEACHER NAME
        teacher_label=Label(class_student_frame, text="Teacher Name :", font=("times new roman", 12, "bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry=ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=17, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3, padx=10, pady=5, sticky=W)


        #RADION BUTTONS
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #BUTTONS FRAME
        btn_frame= Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x= 0, y=200, width=695, height=30)

        save_btn=Button(btn_frame, width=24, text="Save",command=self.add_data, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, width=23, text="Update",command=self.update_data, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, width=23, text="Delete", command=self.delete_data, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, width=23, text="Reset", command=self.reset_data, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        reset_btn.grid(row=0, column=3)

        #BUTTONS FRAME2
        btn_frame2= Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x= 0, y=227, width=695, height=30)

        take_photo_btn=Button(btn_frame2,command=self.generate_dataset, width=48, text="Take Photo Sample", font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn=Button(btn_frame2, width=48, text="Update Photo Sample", font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        update_photo_btn.grid(row=0, column=1)



        #RIGHT LABEL FRAME
        right_frame= LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=745,y=9,width=650,height=580)

        right_img = Image.open('images/listStd.jpg')
        right_img = right_img.resize((700, 115), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(right_img)

        f_lbl=Label(right_frame, image= self.photoimg_right)
        f_lbl.place(x=0, y=0, width=645, height=115)




        #============== SEARCH SYSTEM ============
        search_frame= LabelFrame(right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5,y=115,width=640,height=70)

        search_label=Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"),bg="darkred", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo= ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame, width=17, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0,column=2, padx=10, pady=5, sticky=W)

        search_btn=Button(search_frame, width=12, text="Search", font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn=Button(search_frame, width=12, text="Show All", font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)


        #=============TABLE FRAME============
        table_frame= Frame(right_frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=190,width=640,height=360)

        scroll_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient= VERTICAL)

        self.student_table= ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name","div" ,"roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course",  width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem",  width=100)
        self.student_table.column("id",  width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email",  width=100)
        self.student_table.column("phone",  width=100)
        self.student_table.column("address",  width=100)
        self.student_table.column("teacher",  width=100)
        self.student_table.column("photo",  width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #=======================FUNCTION DECLARATION=================

    def add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()


                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent= self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



    #=====================Fetch Data==================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()

        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #==================Get Cursor====================

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content= self.student_table.item(cursor_focus)
        data= content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #==================Update Function=================
    def update_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()


                                                                                                 ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


    #===============Delete Function==============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delelte this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)




    #================Reset Function==============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")





    #======================Generate DataSet or Take Photo Samples=================
    def generate_dataset(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult= my_cursor.fetchall()
                id= int(self.var_std_id.get())
                for x in myresult:
                    id
                my_cursor.execute(
                    "update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #==============Load predefined data on face frontals from opencv==========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5)
                    #Scaling factor=1.3
                    #Minimum Neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face= cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = r"C:\Users\xhafe\Desktop\FSHKHulumtuesit\data\user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)



if __name__ == "__main__":
        root = Tk()
        app = Student(root)
        root.mainloop()
