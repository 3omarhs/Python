import cv2
import cvzone
import serial

from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8)
cap=cv2.VideoCapture(0)   #0 or 1 is the webCamera number to use

serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 1

while True:
    success,img =cap.read()
    img=cv2.resize(img,(550, 430))
    img = detector.findHands(img)
    I,box = detector.findPosition(img,draw=False)

    cv2.rectangle(img,(0,50),(170,100),(255,255,255),cv2. FILLED)
    cv2.putText(img,"LED-ON",(30,85),cv2. FONT_HERSHEY_PLAIN,2,(0,0,0),3)

    cv2.rectangle(img,(370,50),(560,100),(255,255,255), cv2.FILLED)
    cv2.putText(img,"LED-Off",(380,85),cv2. FONT_HERSHEY_PLAIN,2,(0,0,0),3)



    if I:
        if 20 < I[8][0] < 190:
            cv2.rectangle(img, (20, 50), (170, 100), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "LED-ON", (30, 85), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
            e = '\n'
            serialcomm.write(e.encode())
            serialcomm.write(str(1).encode())
        if 370 < I[8][0] < 540:
            cv2.rectangle(img, (370, 50), (530, 100), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, "LED-Off", (380, 85), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
            e = '\n'
            serialcomm.write(e.encode())
            serialcomm.write(str(0).encode())
    cv2.imshow("Image", img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
