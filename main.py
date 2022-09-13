# importing modules
import cv2
import numpy as np

# creating a face cascade
face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# creating eyes cascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
