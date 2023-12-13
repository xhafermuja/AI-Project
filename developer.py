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


        img_top1 = Image.open('images/Xhafer.jpg')
        img_top1 = img_top1.resize((280, 220), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame, image= self.photoimg_top1)
        f_lbl.place(x=230, y=-5, width=240, height=240)

        #Developer info
        dev_label=Label(main_frame, text="Xhafer Muja", font=("times new roman",30, "bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame, text="Rreth meje", font=("times new roman",20, "bold"),bg="white")
        dev_label.place(x=0,y=120)

        dev_label1=Label(main_frame, text = 
        "Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit,\n "
        "sed do eiusmod tempor incididunt \n  ut labore et dolore magna aliqua.\n "
        "Ut enim ad minim veniam \n, quis nostrud \n  exercitation ullamco laboris nisi \n "
        "ut aliquip ex ea commodo \n consequat. Duis \n  aute irure dolor in reprehenderit \n "
        "in voluptate velit \n esse cillum dolore \n  eu fugiat nulla pariatur. Excepteur \n "
        "sint occaecat \n cupidatat non proident,\n  sunt in culpa qui officia deserunt \n "
        "mollit anim id est laborum. \n"
        , font=("times new roman",10, "bold"),bg="white")
        dev_label1.place(x=0,y=170)

        dev_label=Label(main_frame, text="ID:2103060??", font=("times new roman",20, "bold"),bg="white")
        dev_label.place(x=0,y=460)

        dev_label=Label(main_frame, text="Email:Xhafer.muja@gmail.com", font=("times new roman",20, "bold"),bg="white")
        dev_label.place(x=0,y=500)

        dev_label=Label(main_frame, text="Contact:045823959", font=("times new roman",20, "bold"),bg="white")
        dev_label.place(x=0,y=540)




        bg_img = Image.open('images/logo.jpg')
        bg_img = bg_img.resize((200, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bg_img)



        f_lbl = Label(main_frame, image=self.photoimg)
        f_lbl.place(x=240, y=230, width=200, height=200)

        second_frame = Frame(root, bd=2, bg="white")
        second_frame.place(x=520, y=67, width=480, height=650)  # Adjust dimensions as needed

        # Contents of the second frame
        # Developer info for the second frame
        dev2_label = Label(second_frame, text="Rrezart \nKallaba", font=("times new roman", 30, "bold"), bg="white")
        dev2_label.place(x=10, y=5)  # Adjust x and y positions within the second frame as needed

        dev2_label = Label(second_frame, text="Rreth meje", font=("times new roman", 20, "bold"), bg="white")
        dev2_label.place(x=10, y=135)  # Adjust x and y positions within the second frame as needed

        dev2_label = Label(second_frame, text="Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit,\n "
        "sed do eiusmod tempor incididunt \n  ut labore et dolore magna aliqua.\n "
        "Ut enim ad minim veniam \n, quis nostrud \n  exercitation ullamco laboris nisi \n "
        "ut aliquip ex ea commodo \n consequat. Duis \n  aute irure dolor in reprehenderit \n "
        "in voluptate velit \n esse cillum dolore \n  eu fugiat nulla pariatur. Excepteur \n "
        "sint occaecat \n cupidatat non proident,\n  sunt in culpa qui officia deserunt \n "
        "mollit anim id est laborum. \n", font=("times new roman", 10, "bold"), bg="white")

        bg_img2 = Image.open('images/logo.jpg')
        bg_img2 = bg_img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(bg_img)



        f_lbl = Label(second_frame, image=self.photoimg)
        f_lbl.place(x=240, y=240, width=200, height=200)

        dev2_label.place(x=10, y=175)  # Adjust x and y positions within the second frame as needed

        dev2_label=Label(second_frame, text="ID:2103060??", font=("times new roman",20, "bold"),bg="white")
        dev2_label.place(x=0,y=460)

        dev2_label=Label(second_frame, text="Email:Xhafer.muja@gmail.com", font=("times new roman",20, "bold"),bg="white")
        dev2_label.place(x=0,y=500)

        dev2_label=Label(second_frame, text="Contact:045823959", font=("times new roman",20, "bold"),bg="white")
        dev2_label.place(x=0,y=540)


        

        
        
        

        

        # Image for the second frame
        bg_img_second = Image.open('images/Xhafer.jpg')
        bg_img_second = bg_img_second.resize((260, 230), Image.LANCZOS)
        self.photoimg_second = ImageTk.PhotoImage(bg_img_second)

        f_lbl_second = Label(second_frame, image=self.photoimg_second)
        f_lbl_second.place(x=240, y=-5, width=240, height=240)  # Adjust x and y positions within the second frame as needed

        



        third_frame = Frame(root, bd=2, bg="white")
        third_frame.place(x=20, y=67, width=480, height=650)  # Adjust dimensions as needed

        # Contents of the third frame
        # Developer info for the third frame
        dev3_label = Label(third_frame, text="Endrit \nJelliqi", font=("times new roman", 30, "bold"), bg="white")
        dev3_label.place(x=10, y=5)  # Adjust x and y positions within the second frame as needed

        dev3_label = Label(third_frame, text="Rreth meje", font=("times new roman", 20, "bold"), bg="white")
        dev3_label.place(x=10, y=135)  # Adjust x and y positions within the second frame as needed


        dev3_label = Label(third_frame, text="Lorem ipsum dolor sit amet,\n  consectetur adipiscing elit,\n "
        "sed do eiusmod tempor incididunt \n  ut labore et dolore magna aliqua.\n "
        "Ut enim ad minim veniam \n, quis nostrud \n  exercitation ullamco laboris nisi \n "
        "ut aliquip ex ea commodo \n consequat. Duis \n  aute irure dolor in reprehenderit \n "
        "in voluptate velit \n esse cillum dolore \n  eu fugiat nulla pariatur. Excepteur \n "
        "sint occaecat \n cupidatat non proident,\n  sunt in culpa qui officia deserunt \n "
        "mollit anim id est laborum. \n", font=("times new roman", 10, "bold"), bg="white")
        dev3_label.place(x=10, y=185)  # Adjust x and y positions within the second frame as needed

        bg_img3 = Image.open('images/logo.jpg')
        bg_img3 = bg_img3.resize((200, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(bg_img)



        f_lbl_third = Label(third_frame, image=self.photoimg)
        f_lbl_third.place(x=240, y=250, width=200, height=200)


        dev3_label=Label(third_frame, text="ID:2103060??", font=("times new roman",20, "bold"),bg="white")
        dev3_label.place(x=0,y=460)

        dev3_label=Label(third_frame, text="Email:Xhafer.muja@gmail.com", font=("times new roman",20, "bold"),bg="white")
        dev3_label.place(x=0,y=500)

        dev3_label=Label(third_frame, text="Contact:045823959", font=("times new roman",20, "bold"),bg="white")
        dev3_label.place(x=0,y=540)


        
        

        # Image for the third frame
        bg_img_third = Image.open('images/endrit.jpg')
        bg_img_third = bg_img_third.resize((270, 280), Image.LANCZOS)
        self.photoimg_third = ImageTk.PhotoImage(bg_img_third)

        f_lbl_third = Label(third_frame, image=self.photoimg_third)
        f_lbl_third.place(x=210, y=0, width=280, height=240)  # Adjust x and y positions within the third frame as needed



        



        




   

        
if __name__ == "__main__":
        root = Tk()
        app = Developer(root)
        root.mainloop() 