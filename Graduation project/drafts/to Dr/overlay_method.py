# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4
# resultimage = cv2.bitwise_and(imageread1, imageread2, mask = None)
# added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)


import cv2


def process_image(frame=None, increase_sizex=0, increase_sizey=-0.05, move_right=-0.0, move_up=3.5, image_path=None):
    while True:
        move_right += 0.00000000000000000000000000001
        face_cascade = cv2.CascadeClassifier('face.xml')
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            (x, y), (x + w, y + h)

            sizex = w + (w*increase_sizex)
            sizey = h + (h*increase_sizey)
            logo = cv2.imread(image_path)
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
                          int((centerX + (move_right)) - (sizey / 2)): int((centerX + (move_right)) + (sizey / 2))]
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
        return frame


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = process_image(frame=frame, increase_sizex=0, increase_sizey=-0.05, move_right=-0.0, move_up=3.5, image_path='hair5.png')
    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
