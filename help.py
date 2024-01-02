from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



  

        title_lbl = Label(self.root, text="HELP DESK", font=("Courier New", 35, "bold"), bg="black", fg="blue")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #Top img
        img_top = Image.open('images/helpp.jpg')
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image= self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=720) 

        dev_label = Label(f_lbl, text="Email:endritjelliqi@gmail.com", font=("times new roman", 30, "bold"), bg="white", anchor=W)
        dev_label.place(x=510, y=240, width=600)

        dev_label = Label(f_lbl, text="Email:xhafer.muja@gmail.com", font=("times new roman", 30, "bold"), bg="white", anchor=W)
        dev_label.place(x=510, y=300, width=600)

        dev_label = Label(f_lbl, text="Email:rrezartkallaba@gmail.com", font=("times new roman", 30, "bold"), bg="white", anchor=W)
        dev_label.place(x=510, y=360, width=600)





if __name__ == "__main__":
        root = Tk()
        app = Help(root)
        root.mainloop() 