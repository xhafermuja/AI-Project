from tkinter import *
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================ Variables =========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        #BG IMG
        bg_img = Image.open('images/bg_attendance.jpg')
        bg_img = bg_img.resize((1530, 800), Image.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(bg_img)

        f_lbl = Label(self.root, image=self.photoimgbg)
        f_lbl.place(x=0, y=0, width=1530, height=800)

        #TITLE
        title_lbl = Label(self.root, text="ATTENDANE MANAGEMENT SYSTEM", font=("Courier New", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #MAIN FRAME
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=50, y=100, width=1430, height=650)

        #LEFT LABEL FRAME
        left_frame= LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=20,y=10,width=715,height=580)

        left_img = Image.open('images/smart_attendance.jpeg')
        left_img = left_img.resize((710, 150), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_img)

        f_lbl=Label(left_frame, image= self.photoimg_left)
        f_lbl.place(x=0, y=0, width=710, height=150)
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE ,bg="white")
        left_inside_frame.place(x=5, y=155, width=700, height=370)

        # Labeland entry

        # Attendace ID
        attendanceID_label=Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 12, "bold"),bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"),bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        atten_roll.grid(row=0,column=3, padx=10, pady=5, sticky=W)

        # NAME
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"),bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        atten_name = ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        atten_name.grid(row=1,column=1, padx=10, pady=5, sticky=W)

        # DEPARTAMENT
        depLabel = Label(left_inside_frame, text="Departament:", font=("times new roman", 12, "bold"),bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        atten_dep = ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1,column=3, padx=10, pady=5, sticky=W)


        # TIME
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        atten_time = ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        atten_time.grid(row=2,column=1, padx=10, pady=5, sticky=W)


        # DATE
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"),bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        atten_date = ttk.Entry(left_inside_frame, width=17, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        atten_date.grid(row=2,column=3, padx=10, pady=5, sticky=W)


        # ATTENDANCE
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"),bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        self.atten_status = ttk.Combobox(left_inside_frame, width=15, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"))
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)


        #BUTTONS FRAME
        btn_frame= Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x= 0, y=300, width=695, height=30)

        save_btn=Button(btn_frame, width=24, text="Import csv", command=self.importCsv, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, width=23, text="Export csv", command=self.exportCsv, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, width=23, text="Update", font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, width=23, text="Reset", command=self.reset_data, font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        reset_btn.grid(row=0, column=3)

        #RIGHT LABEL FRAME
        right_frame= LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=745,y=9,width=650,height=580)

        table_frame= Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x= 3, y=5, width=640, height=455)


        # ================= Scroll bar table ===================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id","roll","name","department","time","date","attendance"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)



        # ================ Fetch Data =================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    #  Import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #  Export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror('No Data', 'No data found to export', parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo('Success', "Your data exported to "+os.path.basename(fln) + " successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
                
            


         

if __name__ == "__main__":
        root = Tk()
        app = Attendance(root)
        root.mainloop()

