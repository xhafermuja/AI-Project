from tkinter import *
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



  

        title_lbl = Label(self.root, text="DEVELOPER", font=("Courier New", 35, "bold"), bg="black", fg="blue")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #Top img
        img_top = Image.open('images/developer.jpg')
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image= self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)   

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1020, y=19, width=480, height=650)  


        f_lbl=Label(self.root, image= self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)   

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1020, y=19, width=480, height=650)  


       

        #Developer info
        dev_label=Label(main_frame, text="Xhafer Muja", font=("times new roman",25, "bold"),bg="white")
        dev_label.place(x=140, y=210)

        dev_label=Label(main_frame, text="Rreth meje", font=("times new roman",18, "bold"),bg="white")
        dev_label.place(x=20,y=270)

        dev_label1=Label(main_frame, text = 
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        , font=("times new roman", 10, "italic"), bg="white")
        dev_label1.place(x=20,y=320)

        dev_label=Label(main_frame, text="ID:210306076", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev_label.place(x=20,y=460)

        dev_label=Label(main_frame, text="Email: xhafermuja@gmail.com", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev_label.place(x=20,y=500) 

        dev_label=Label(main_frame, text="Contact: 049******", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev_label.place(x=20,y=540)

        img_top1 = Image.open('images/Xhafer.jpg')
        img_top1 = img_top1.resize((230, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame, image= self.photoimg_top1, borderwidth=1, highlightthickness=1)
        f_lbl.place(x=140, y=0, width=200, height=200)



        bg_img = Image.open('images/logo.jpg')
        bg_img = bg_img.resize((100, 100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bg_img)

        f_lbl = Label(main_frame, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=100, height=100)



        second_frame = Frame(root, bd=2, bg="white")
        second_frame.place(x=520, y=67, width=480, height=650)  # Adjust dimensions as needed

        # Contents of the second frame
        # Developer info for the second frame
        dev2_label = Label(second_frame, text="Rrezart Kallaba", font=("times new roman", 25, "bold"), bg="white")
        dev2_label.place(x=140, y=210)  # Adjust x and y positions within the second frame as needed

        dev2_label = Label(second_frame, text="Rreth meje", font=("times new roman", 18, "bold"), bg="white")
        dev2_label.place(x=20, y=270)  # Adjust x and y positions within the second frame as needed

        dev2_label = Label(second_frame, text = 
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        , font=("times new roman", 10, "italic"), bg="white")
        dev2_label.place(x=20, y=320)  # Adjust x and y positions within the second frame as needed

        bg_img2 = Image.open('images/logo.jpg')
        bg_img2 = bg_img2.resize((100, 100), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(bg_img2)

        f_lbl = Label(second_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=100, height=100)

        

        dev2_label=Label(second_frame, text="ID: 210306034", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev2_label.place(x=20,y=460)

        dev2_label=Label(second_frame, text="Email: rrezartkallaba@gmail.com", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev2_label.place(x=20,y=500)

        dev2_label=Label(second_frame, text="Contact: 049******", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev2_label.place(x=20,y=540)

        # Image for the second frame
        bg_img_second = Image.open('images/user.png')
        bg_img_second = bg_img_second.resize((230, 200), Image.LANCZOS)
        self.photoimg_second = ImageTk.PhotoImage(bg_img_second)

        # Adjust x and y positions within the second frame as needed
        f_lbl_second = Label(second_frame, image=self.photoimg_second, borderwidth=1, highlightthickness=1)
        f_lbl_second.place(x=140, y=0, width=200, height=200)

    

        third_frame = Frame(root, bd=2, bg="white")
        third_frame.place(x=20, y=67, width=480, height=650)  # Adjust dimensions as needed

        # Contents of the third frame
        # Developer info for the third frame
        dev3_label = Label(third_frame, text="Endrit Jelliqi", font=("times new roman", 25, "bold"), bg="white")
        dev3_label.place(x=140, y=210)  # Adjust x and y positions within the second frame as needed

        dev3_label = Label(third_frame, text="Rreth meje", font=("times new roman", 18, "bold"), bg="white")
        dev3_label.place(x=20, y=270)  # Adjust x and y positions within the second frame as needed


        dev3_label = Label(third_frame, text = 
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, consectetur elit\n"
        , font=("times new roman", 10, "italic"), bg="white")
        dev3_label.place(x=20, y=320)  # Adjust x and y positions within the second frame as needed

        bg_img3 = Image.open('images/logo.jpg')
        bg_img3 = bg_img3.resize((100, 100), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(bg_img3)



        f_lbl_third = Label(third_frame, image=self.photoimg3)
        f_lbl_third.place(x=0, y=0, width=100, height=100)


        dev3_label=Label(third_frame, text="ID: 210306091", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev3_label.place(x=20,y=460)

        dev3_label=Label(third_frame, text="Email: endritjelliqi@gmail.com",font=("times new roman", 18,"bold", "italic"), bg="white")
        dev3_label.place(x=20,y=500)

        dev3_label=Label(third_frame, text="Contact: 049******", font=("times new roman", 18,"bold", "italic"), bg="white")
        dev3_label.place(x=20,y=540)


        
        

        # Image for the third frame
        bg_img_third = Image.open('images/endrit.jpg')
        bg_img_third = bg_img_third.resize((230, 200), Image.LANCZOS)
        self.photoimg_third = ImageTk.PhotoImage(bg_img_third)

        f_lbl_third = Label(third_frame, image=self.photoimg_third, borderwidth=1, highlightthickness=1)
        f_lbl_third.place(x=140, y=0, width=200, height=200) # Adjust x and y positions within the third frame as needed


        
if __name__ == "__main__":
        root = Tk()
        app = Developer(root)
        root.mainloop() 