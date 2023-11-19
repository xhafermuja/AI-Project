from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


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
        current_course_frame.place(x=5,y=115,width=700,height=200)

        dep_label=Label(current_course_frame, text="Departament", font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo= ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"]=("Select Department", "Fakulteti i Shkencave Kompjuterike", "Fakulteti i Filologjisë", "Fakulteti Ekonomik", "Fakulteti i Shkencave të Jetës dhe Mjedisit", "Fakulteti i Edukimit", "Fakulteti Juridik")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10)


        #RIGHT LABEL FRAME
        right_frame= LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=745,y=10,width=660,height=580)





if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
