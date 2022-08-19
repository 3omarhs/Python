# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4
# resultimage = cv2.bitwise_and(imageread1, imageread2, mask = None)
# added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)


# '''
# importing the libraries
import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)

# Read logo and resize
logo = cv2.imread('image.png')
# size = 100
# logo = cv2.resize(logo, (size, size))


increase_sizex = 0
increase_sizey = 0
move_up = 100 * 100
move_right = 38

# Create a mask of logo
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    # Capture frame-by-frame

    ret, frame = cap.read()
    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier('face.xml')

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        (x, y), (x + w, y + h)
        sizex = w + increase_sizex
        sizey = h + increase_sizey
        logo = cv2.resize(logo, (sizex, sizey))
        centerX = x+(w/2)
        centerY = y+(h/2)
        # roi = frame[-sizex - 10:-10, -sizey - 10:-10]
        roi = frame[int((centerY - (move_up/h)) - (sizex/2)) : int((centerY - ( move_up/h)) + (sizex/2)), int((centerX + (w / move_right)) - (sizey/2)) : int((centerX + (w / move_right)) + (sizey/2))]
        # roi = frame[-size - 10:-10, -size - 10:-10]
        # roi[np.where(mask)] = 0
        roi += logo
        # Region of Image (ROI), where we want to insert logo
        # roi = frame[-size - 10:-10, -size - 10:-10]

        # Set an index of where the mask is
        # roi[np.where(mask)] = 0
        # roi += logo

        cv2.imshow('WebCam', frame)
        if cv2.waitKey(1) == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# '''


'''
############################################################### my edition 2:
# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4



# importing the libraries
import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)

# Read logo and resize
logo = cv2.imread('image.png')
size = 100
logo = cv2.resize(logo, (size, size))


sizex = 100
sizey = 100


# Create a mask of logo
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        (x, y), (x + w, y + h)
        sizex = w
        sizey = h
        logo = cv2.resize(logo, (sizex, sizey))
        roi = frame[-sizex - 10:-10, -sizey - 10:-10]
        x = cv2.bitwise_and(roi, logo, mask=None)
        frame[-sizex - 10:-10, -sizey - 10:-10] = x
        # roi = frame[-size - 10:-10, -size - 10:-10]
        # roi[np.where(mask)] = 0
        # roi += logo
    # Region of Image (ROI), where we want to insert logo
    # roi = frame[-size - 10:-10, -size - 10:-10]

    # Set an index of where the mask is
    # roi[np.where(mask)] = 0
    # roi += logo




    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

###############################################################
# '''

'''
# code from website:
# importing the libraries
import cv2
import numpy as np

# Setup camera
cap = cv2.VideoCapture(0)

# Read logo and resize
logo = cv2.imread('image.png')
size = 100
logo = cv2.resize(logo, (size, size))

# Create a mask of logo
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Region of Image (ROI), where we want to insert logo
    roi = frame[-size-10:-10, -size-10:-10]

    # Set an index of where the mask is
    roi[np.where(mask)] = 0
    roi += logo

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# '''