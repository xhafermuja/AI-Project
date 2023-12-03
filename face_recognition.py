from tkinter import *
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #TITLE
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Courier New", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45)

        # #1st img
        # img_top = Image.open('images/face_detector2.jpg')
        # img_top = img_top.resize((650, 800), Image.LANCZOS)
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root, image= self.photoimg_top)
        # f_lbl.place(x=0, y=45, width=650, height=800)

        #2st img
        img_bottom = Image.open('images/face_detector.png')
        img_bottom = img_bottom.resize((1530, 800), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root, image= self.photoimg_bottom)
        f_lbl.place(x=0, y=45, width=1530, height=800)


        #Face Detector BTN
        b1_1=Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("Courier New", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=600, y=650, width=240, height=40)

    

    #=========== Attendance ============
    def mark_attendance(self, i, r, n, d):
        with open("hyrjet.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset ")
                

    
    #=========== Face Recognition ============

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn= mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor= conn.cursor()

                # Ndryshimi i kodit me pjesen e kodit poshte per shkak te 1 error
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                # n = str(n)  # Convert to string
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                # r = str(r)  # Convert to string
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                # d = str(d)  # Convert to string
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                # i = str(i)  # Convert to string
                i="+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Departament:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Face!" ,(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coord = [x,y,w,y]

            return coord
            
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        video_cap.destroy()
        cv2.destroyAllWindows()


if __name__ == "__main__":
        root = Tk()
        app = Face_Recognition(root)
        root.mainloop()