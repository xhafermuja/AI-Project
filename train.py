from tkinter import *
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #TITLE
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Courier New", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        #Top img
        img_top = Image.open('images/facerecognition.png')
        img_top = img_top.resize((1530, 340), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image= self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=340)

        #Train BTN
        b1_1=Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("Courier New", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=385, width=1530, height=60)

        #Bottom img
        img_bottom = Image.open('images/opencv_face_reco_more_data.jpg')
        img_bottom = img_bottom.resize((1530, 340), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root, image= self.photoimg_bottom)
        f_lbl.place(x=0, y=445, width=1530, height=340)


    def train_classifier(self):
        data_dir = ("data")
        path =[os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        #================ Train the classifier And save ===============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")        


if __name__ == "__main__":
        root = Tk()
        app = Train(root)
        root.mainloop()
