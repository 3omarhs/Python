# 3omar.hs edition

# must be edited:
# 1) multi photos for every character in the dataset.
# 2) find the gender detection model maker code.
# 3) find the best fit image properities for viewing without errors in the project.
# 4) reformat the code.
# 5) find AI algorithm used in gender   > Jalookh.
#                                       > downloaded folders.



# https://github.com/Pavankunchala/AGE-Gender-Detection
# other gender detection projects:
# https://www.youtube.com/watch?v=WOuAI5DhHyU


import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            try:
                img_encoding = face_recognition.face_encodings(rgb_img)[0]    ##########################################################################
            except:1

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names



hotoname = ''
oldphoto = ''
gender = ''
mode_selected = 0
# images_path_M = 'D:/Backup/PycharmProjects/datasets/10photos0/'
images_path_M = 'photos/10photos/'

# images_path_M = r'C:/Users/Omar Hassan/Desktop/rr/'

# images_path_M = 'D:/Backup/PycharmProjects/datasets/10photos/'
# images_path_M = fr'C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen2\photos\10photos0'

# images_path_F = 'D:/Backup/PycharmProjects/datasets/10photos_w/'
images_path_F = 'photos/10photos_w/'
sfr = SimpleFacerec()

print('Male Images Encoding:')
sfr.load_encoding_images(images_path_M)

print('Female Images Encoding:')
sfr.load_encoding_images(images_path_F)


def getFaceBox(net, frame, conf_threshold=0.75):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)

    return frameOpencvDnn, bboxes

def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    try:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    except:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGR)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)

    return imgBack



faceProto = "AGE-Gender-Detection-main/opencv_face_detector.pbtxt"
faceModel = "AGE-Gender-Detection-main/opencv_face_detector_uint8.pb"

ageProto = "AGE-Gender-Detection-main/age_deploy.prototxt"
ageModel = "AGE-Gender-Detection-main/age_net.caffemodel"

genderProto = "AGE-Gender-Detection-main/gender_deploy.prototxt"
genderModel = "AGE-Gender-Detection-main/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# load the network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)

cap = cv2.VideoCapture(0)
padding = 20

def main_GUI():
    while True:
        hasFrame, frame = cap.read()
        imgBG = cv2.imread("photos/BG.jpg")
        imgBG[170:650, 725:1365] = frame
        cv2.putText(imgBG, f'Finding Best Haircut For You`r Face..', (70, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

        # if not hasFrame:
        #     cv2.waitKey()
        #     break

        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        frameFace, bboxes = getFaceBox(faceNet, small_frame)

        # if not bboxes:
        #     print("No face Detected, Checking next frame")
        #     continue

        for bbox in bboxes:
            face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
                   max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
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

            cv2.putText(frame, (name+','+gender), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.putText(imgBG, f'The best Haircut For You ', (20, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
            cv2.putText(imgBG, f' Is Like: {name}', (50, 230), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255, 255), 3)
            # cv2.putText(frame, (name), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)
            imgBG[170:650, 725:1365] = frame  # all image height = 700-50=650 & - video height"480"        all image width = 1375-10=1365 & - video width"640"

            if (name != 'Unknown'):
                # img = cv2.imread(r"C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen2\photos\10photos\Aaron_Pena_0001.png", cv2.IMREAD_UNCHANGED)
                dim = (276, 276)
                personBG = cv2.imread('photos/white.png', cv2.IMREAD_UNCHANGED)
                personBG = cv2.resize(personBG, dim)
                imgBG = overlayPNG(imgBG, personBG, (50, 250))

                # img = cv2.imread(r"C:\Users\Omar Hassan\Desktop\rr\Abdullah_Gul (4).png", cv2.IMREAD_UNCHANGED)
                try:
                    img = cv2.imread(f'{images_path}{name}.png', cv2.IMREAD_UNCHANGED)
                    img2 = cv2.resize(img, dim)
                    # print(img.shape)
                    imgBG = overlayPNG(imgBG, img2, (50, 250))   #(x, y)
                except:1
            # except:1
        cv2.waitKey(1)
        cv2.imshow("Detection..", imgBG)


# except Exception as e: print(e)
# except:1


while True:

    if mode_selected == 1:
        try:
            main_GUI()
        except Exception as e:
            print(e)

    else:
        try:
            # main_filter()
            1
        except Exception as e:
            print(e)
#     # traceback.print_exc()
#     pygame.quit()