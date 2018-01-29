import os
import cv2
import numpy as np 
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def addUser(id,name,age,status):
    conn=sqlite3.connect("recDetails.db")
    verify="select * from recDetails where id=" + str(id)
    cursor=conn.execute(verify)
    exists=0
    for row in cursor:
        exists=1
    if(exists==1):
        print("sorry user with id already exists")
    else:
        query="insert into recDetails values("+ str(id) + ",'" + str(name) + "'," + str(age) + ",'" + str(status) + "')"
        conn.execute(query)
    conn.commit()
    conn.close()

print('=========== Face Recognition System =========')
print('please enter the following user details')
id=input('id :')
name=input('name :')
age=input('age :')
status=input('status :')
addUser(id,name,age,status)

objNum = 0
while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces :
        objNum = objNum + 1
        cv2.imwrite("testData/Obj."+str(id)+"."+str(objNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)

    cv2.imshow("FACE",img);
    cv2.waitKey(1)
    if(objNum>20):
        break;

cam.release();
cv2.destroyAllWindows();
               
