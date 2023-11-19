from tkinter import *
from PIL import Image, ImageTk


class FaceRecognitionSystem:
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
        title_lbl = Label(self.root, text="FACE RECOGNITION SYSTEM", font=("Courier New", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #Student BTN
        std_img = Image.open('images/student.png')
        std_img = std_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_std = ImageTk.PhotoImage(std_img)

        b1=Button(self.root, image= self.photoimg_std, cursor="hand2")
        b1.place(x=200, y=100, width=200, height=200 )

        b1_1=Button(self.root, text="Student Details" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=200, height=40)

        #Detect Face BTN
        df_img = Image.open('images/face.png')
        df_img = df_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_fc = ImageTk.PhotoImage(df_img)

        b1=Button(self.root, image= self.photoimg_fc, cursor="hand2")
        b1.place(x=500, y=100, width=200, height=200 )

        b1_1=Button(self.root, text="Face Detector" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=200, height=40)

        #Attendance BTN
        att_img = Image.open('images/report.png')
        att_img = att_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_att = ImageTk.PhotoImage(att_img)

        b1=Button(self.root, image= self.photoimg_att, cursor="hand2")
        b1.place(x=800, y=100, width=200, height=200 )

        b1_1=Button(self.root, text="Attendance" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=200, height=40)

        #Help BTN
        help_img = Image.open('images/help.png')
        help_img = help_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_help = ImageTk.PhotoImage(help_img)

        b1=Button(self.root, image= self.photoimg_help, cursor="hand2")
        b1.place(x=1100, y=100, width=200, height=200 )

        b1_1=Button(self.root, text="Help Desk" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=200, height=40)

        #Train BTN
        train_img = Image.open('images/train.png')
        train_img = train_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_train = ImageTk.PhotoImage(train_img)

        b1=Button(self.root, image= self.photoimg_train, cursor="hand2")
        b1.place(x=200, y=380, width=200, height=200 )

        b1_1=Button(self.root, text="Train Data" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=200, height=40)

        #Photos BTN
        upload_img = Image.open('images/upload.png')
        upload_img = upload_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_upload = ImageTk.PhotoImage(upload_img)

        b1=Button(self.root, image= self.photoimg_upload, cursor="hand2")
        b1.place(x=500, y=380, width=200, height=200 )

        b1_1=Button(self.root, text="Upload Data" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=200, height=40)

        #Developer BTN
        dev_img = Image.open('images/dev.png')
        dev_img = dev_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_dev = ImageTk.PhotoImage(dev_img)

        b1=Button(self.root, image= self.photoimg_dev, cursor="hand2")
        b1.place(x=800, y=380, width=200, height=200 )

        b1_1=Button(self.root, text="Developers" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=200, height=40)


        #Exit BTN
        ext_img = Image.open('images/exit.png')
        ext_img = ext_img.resize((200, 200), Image.LANCZOS)
        self.photoimg_ext = ImageTk.PhotoImage(ext_img)

        b1=Button(self.root, image= self.photoimg_ext, cursor="hand2")
        b1.place(x=1100, y=380, width=200, height=200 )

        b1_1=Button(self.root, text="Exit" , cursor="hand2", font=("Courier New", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=200, height=40)




if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
