# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4
# resultimage = cv2.bitwise_and(imageread1, imageread2, mask = None)
# added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)


import cv2

cap = cv2.VideoCapture(0)
haircut_image = 'image.png'

increase_sizex = 0
increase_sizey = -0.05
move_up = 3.5 #100 * 100
move_right = 50050

# img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        (x, y), (x + w, y + h)

        sizex = w + (w*increase_sizex)
        sizey = h + (h*increase_sizey)
        logo = cv2.imread(haircut_image)
        try:
            logo = cv2.resize(logo, (int(sizey), int(sizex)))
            centerX = x+(w/2)
            centerY = y+(h/2)
            roi = frame[int((centerY - (h / move_up)) - (sizex/2)) : int((centerY - (h / move_up)) + (sizex/2)),
                  int((centerX + (w / move_right)) - (sizey/2)) : int((centerX + (w / move_right)) + (sizey/2))]
            roi += logo
        except:
            try:
                logo = cv2.resize(logo, (int(sizey+1), int(sizex)))
                centerX = x + (w / 2)
                centerY = y + (h / 2)
                roi = frame[int((centerY - (h / move_up)) - (sizex / 2)): int((centerY - (h / move_up)) + (sizex / 2)),
                      int((centerX + (w / move_right)) - (sizey / 2)): int((centerX + (w / move_right)) + (sizey / 2))]
                roi += logo
            except:
                try:
                    logo = cv2.resize(logo, (int(sizey), int(sizex)+1))
                    centerX = x + (w / 2)
                    centerY = y + (h / 2)
                    roi = frame[
                          int((centerY - (h / move_up)) - (sizex / 2)): int((centerY - (h / move_up)) + (sizex / 2)),
                          int((centerX + (w / move_right)) - (sizey / 2)): int(
                              (centerX + (w / move_right)) + (sizey / 2))]
                    roi += logo
                except:1


    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





'''
# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4
# resultimage = cv2.bitwise_and(imageread1, imageread2, mask = None)
# added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)


import cv2

cap = cv2.VideoCapture(0)
logo = cv2.imread('image.png')

increase_sizex = 0
increase_sizey = 0
move_up = 12 * 10
move_right = 80

# img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('face.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        (x, y), (x + w, y + h)
        y = h + move_up
        sizex = w + increase_sizex
        sizey = h + increase_sizey
        logo = cv2.resize(logo, (sizex, sizey))
        centerX = x+(w/2)
        centerY = y+(h/2)
        roi = frame[int((centerY - (h)) - (sizex/2)) : int((centerY - (h)) + (sizex/2)),
              int((centerX + (w / move_right)) - (sizey/2)) : int((centerX + (w / move_right)) + (sizey/2))]
        roi += logo

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''