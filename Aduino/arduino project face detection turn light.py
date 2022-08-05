from cvzone.FaceDetectionModule import FaceDetector
import cv2
# import time
import serial

serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 1

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        e = '\n'
        serialcomm.write(e.encode())
        serialcomm.write(str(1).encode())
    else:
        e = '\n'
        serialcomm.write(e.encode())
        serialcomm.write(str(0).encode())

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





'''
##Arduino code##


const int led = 13; 
String arrivingdatabyte; 

void setup() { 
  Serial.begin(9600); 
  pinMode(led, OUTPUT);
}

void loop() { 
  if(Serial.available( ) > 0) { 
    arrivingdatabyte = Serial.readStringUntil('\n'); 
    if(arrivingdatabyte=="1") { 
      digitalWrite(led,HIGH); 
      }
     else if(arrivingdatabyte=="0") { 
      digitalWrite(led,LOW); 
      }
     }
    }



'''