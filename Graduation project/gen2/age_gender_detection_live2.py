import cv2
import math
import time
import argparse


from simple_facerec import SimpleFacerec
hotoname = ''
oldphoto = ''
images_path_M = 'D:/Backup/PycharmProjects/datasets/10photos/'
images_path_F = 'D:/Backup/PycharmProjects/datasets/10photos_w/'
sfr = SimpleFacerec()
# sfr.load_encoding_images("D:/Backup/PycharmProjects/datasets/10photos/")
sfr.load_encoding_images(images_path_M)
sfr.load_encoding_images(images_path_F)


def getFaceBox(net, frame,conf_threshold = 0.75):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn,1.0,(300,300),[104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence > conf_threshold:
            x1 = int(detections[0,0,i,3]* frameWidth)
            y1 = int(detections[0,0,i,4]* frameHeight)
            x2 = int(detections[0,0,i,5]* frameWidth)
            y2 = int(detections[0,0,i,6]* frameHeight)
            bboxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn,(x1,y1),(x2,y2),(0,255,0),int(round(frameHeight/150)),8)

    return frameOpencvDnn , bboxes


# def load_encoding_images(images_path, capt, personPhoto):
def load_encoding_images(images_path, capt):
    while True:
        ret, frame = cap.read()
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            photoname = name
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Scan Your face to detect the best hair cut for you", frame)
        if(photoname != 'Unknown'):
            img = cv2.imread(f'{images_path}/{photoname}.jpg')
            cv2.imshow(photoname, img)
            if oldphoto == '' or oldphoto != photoname:
                if oldphoto != '':
                    cv2.destroyWindow(oldphoto)
                oldphoto = photoname
            cv2.waitKey(500)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



faceProto = "AGE-Gender-Detection-main/opencv_face_detector.pbtxt"
faceModel = "AGE-Gender-Detection-main/opencv_face_detector_uint8.pb"

ageProto = "AGE-Gender-Detection-main/age_deploy.prototxt"
ageModel = "AGE-Gender-Detection-main/age_net.caffemodel"

genderProto = "AGE-Gender-Detection-main/gender_deploy.prototxt"
genderModel = "AGE-Gender-Detection-main/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']


#load the network
ageNet = cv2.dnn.readNet(ageModel,ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)

cap = cv2.VideoCapture(0)
padding = 20

try:
    while cv2.waitKey(1) < 0:
        #read frame
        t = time.time()
        hasFrame , frame = cap.read()
        ret, frame1 = cap.read()

        if not hasFrame:
            cv2.waitKey()
            break
        #creating a smaller frame for better optimization
        small_frame = cv2.resize(frame,(0,0),fx = 0.5,fy = 0.5)

        frameFace ,bboxes = getFaceBox(faceNet,small_frame)
        if not bboxes:
            print("No face Detected, Checking next frame")
            continue
        for bbox in bboxes:
            face = small_frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),
                    max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender = genderList[genderPreds[0].argmax()]
            if gender == 'Male':
                images_path = images_path_M
            else:
                images_path = images_path_F
            print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            # for bbox in bboxes:
            #     face = small_frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),
            #             max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
            #     blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            #     genderNet.setInput(blob)
            #     genderPreds = genderNet.forward()
            #     gender = genderList[genderPreds[0].argmax()]
            #     print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))


                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                cv2.imshow("Age Gender Demo", frame)
                if (name != 'Unknown'):
                    img = cv2.imread(f'{images_path}/{name}.jpg')
                    cv2.imshow(name, img)
                    if oldphoto == '' or oldphoto != name:
                        if oldphoto != '':
                            cv2.destroyWindow(oldphoto)
                        oldphoto = name
                    cv2.waitKey(500)




        print("time : {:.3f}".format(time.time() - t))
        # load_encoding_images(images_path="D:/Backup/PycharmProjects/datasets/10photos/", capt=cap)


except: 1


    




        









# try:
#     load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/10photos/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_8.jpg')
#     # 1
#     # detect_face.load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/men/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_100.jpg')
# except:
#     print("Ended!")