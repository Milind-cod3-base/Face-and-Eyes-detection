# importing modules
import cv2
import numpy as np

# creating a face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# creating eyes cascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# capturing using external video cam
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

# starting the loop
while True:
    ret, img = cap.read()
    # converting video into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detects objects of different sizes in the input image and draws
    # rectangles on it
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(
            img,
            pt1=(
                x,
                y),
            pt2=(
                x + w,
                y + h),
            color=(
                255,
                0,
                0),
            thickness=2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # after finding the face, look for the eyes.
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                img=roi_color,
                pt1=(
                    ex,
                    ey),
                pt2=(
                    ex + ew,
                    ey + eh),
                color=(
                    0,
                    255,
                    0),
                thickness=2)

    cv2.imshow('img', img)  # displays the image in the specified window
    # milliseconds, waits for specific time until you press any button on
    # keyword
    k = cv2.waitKey(30)

    if k == 27:  # interruption happens before 30 ms
        break

cap.release()
cv2.destroyAllWindows()
