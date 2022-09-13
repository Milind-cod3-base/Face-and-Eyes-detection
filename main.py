# importing modules
import cv2
import numpy as np

# creating a face cascade
face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# creating eyes cascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# capturing using external video cam
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)

# starting the loop
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting video into gray scale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detects objects of different sizes in the input image and draws rectangles on it


    for (x,y,w,h) in faces:
        cv2.rectangle(img, pt1=(x,y),pt2=(x+w, y+h), color=(255,0,0), thickness=2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # after finding the face, look for the eyes.