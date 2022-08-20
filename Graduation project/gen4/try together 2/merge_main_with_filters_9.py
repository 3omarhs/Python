import glob
import os
import time
import face_recognition
import argparse
import keyboard
import cv2
import numpy as np
import pygame
import filter
import random
import pickle

# current_run = 'train'
current_run = 'run'
mode_selected = 0
tolerance=0.75  #un-accuracy "error" percentage
compare_faces_accuracy = 1  # 0 - 1
camera_number = 0
wait_to_change_time = 2

oldphoto = ''
gender = ''
filter1 = ""
img2 = ''
male = ''
person_name = ''
old_img = r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen4\photos\mens\Ashton Kutcher (4).png'
saved_time = round(time.time())
encoding_images_path = '../encoded images files'
BG_photo_path = "../photos/BG.jpg"
white_photo_path = '../photos/white.png'
images_path_M = '../photos/mens/'
images_path_F = '../photos/womens/'
images_path = ''

faceProto = "../AGE-Gender-Detection-main/opencv_face_detector.pbtxt"
faceModel = "../AGE-Gender-Detection-main/opencv_face_detector_uint8.pb"

ageProto = "../AGE-Gender-Detection-main/age_deploy.prototxt"
ageModel = "../AGE-Gender-Detection-main/age_net.caffemodel"

genderProto = "../AGE-Gender-Detection-main/gender_deploy.prototxt"
genderModel = "../AGE-Gender-Detection-main/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)
video_capture = cv2.VideoCapture(camera_number)
cap = video_capture
padding = 20

CASCADE_DIR = "data/cascades/"


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings_m = []
        self.known_face_names_m = []
        self.known_face_encodings_f = []
        self.known_face_names_f = []
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path, category):
        if current_run == 'train':
            images_path = glob.glob(os.path.join(images_path, "*.*"))
            print("{} encoding images found.".format(len(images_path)))
            for img_path in images_path:
                img = cv2.imread(img_path)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)
                try:
                    img_encoding = face_recognition.face_encodings(rgb_img)[
                        0]  ##########################################################################
                except:
                    1
                if category == 'Male':
                    self.known_face_encodings_m.append(img_encoding)
                    self.known_face_names_m.append(filename)
                else:
                    self.known_face_encodings_f.append(img_encoding)
                    self.known_face_names_f.append(filename)
            print("Encoding images loaded")

            with open(f'{encoding_images_path}/{category}_encoding.txt', "wb") as fp:  # Pickling
                if category == 'Male':
                    pickle.dump(self.known_face_encodings_m, fp)
                else:
                    pickle.dump(self.known_face_encodings_f, fp)

            with open(f'{encoding_images_path}/{category}_names.txt', "wb") as fp:  # Pickling
                if category == 'Male':
                    pickle.dump(self.known_face_names_m, fp)
                else:
                    pickle.dump(self.known_face_names_f, fp)

            if category == 'Male':
                self.known_face_encodings_m = []
                self.known_face_names_m = []
                with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                    self.known_face_encodings_m = pickle.load(fp)
                with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                    self.known_face_names_m = pickle.load(fp)
            else:
                self.known_face_encodings_f = []
                self.known_face_names_f = []
                with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                    self.known_face_encodings_f = pickle.load(fp)
                with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                    self.known_face_names_f = pickle.load(fp)


            print("Encoding images loaded")




        else:
            # def load_encoding_images(self, images_path, category):
            if category == 'Male':
                with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                    self.known_face_encodings_m = pickle.load(fp)
                with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                    self.known_face_names_m = pickle.load(fp)
            else:
                with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                    self.known_face_encodings_f = pickle.load(fp)
                with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                    self.known_face_names_f = pickle.load(fp)
            print("Encoding images loaded")

    def detect_known_faces(self, frame, category):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
            if category == 'Male':
                matches = face_recognition.compare_faces(self.known_face_encodings_m, face_encoding, tolerance=tolerance)
            else:
                matches = face_recognition.compare_faces(self.known_face_encodings_f, face_encoding, tolerance=tolerance)
            name = "Unknown"

            if category == 'Male':
                face_distances = face_recognition.face_distance(self.known_face_encodings_m, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names_m[best_match_index]
                else:
                    print('unknown detected!!')
                    # name = self.known_face_names_m[random.randint(0, int(len(matches)))]
                if len(face_names) < 2:
                    face_names.append(name)
            else:
                face_distances = face_recognition.face_distance(self.known_face_encodings_f, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names_f[best_match_index]
                else:
                    print('unknown detected!!')
                    # name = self.known_face_names_f[random.randint(0, int(len(matches)))]
                if len(face_names) < 2:
                    face_names.append(name)
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names


def getFaceBox(net, frame, conf_threshold=0.75):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)     # function returns a blob which is our input image after mean subtraction, normalizing, and channel swapping.
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


def main_GUI():
    hasFrame, frame = cap.read()
    imgBG = cv2.imread(BG_photo_path)
    imgBG[170:650, 725:1365] = frame
    cv2.putText(imgBG, f'Finding Best Haircut For You`r Face..', (70, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),6)

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    frameFace, bboxes = getFaceBox(faceNet, small_frame)

    global images_path
    global gender

    for bbox in bboxes:
        face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
               max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
        try:
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)     # function returns a blob which is our input image after mean subtraction, normalizing, and channel swapping.
            genderNet.setInput(blob)
        except:1
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        if gender == 'Male':
            images_path = images_path_M
        else:
            images_path = images_path_F
        print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
    face_locations, face_names = sfr.detect_known_faces(frame, gender)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        try:
            cv2.putText(frame, (name + ',' + gender), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        except:
            1
        global person_name
        cv2.putText(imgBG, f'The best Haircut For You ', (20, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        cv2.putText(imgBG, f' Is Like: {person_name}', (50, 230), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)
        imgBG[170:650,
        725:1365] = frame  # all image height = 700-50=650 & - video height"480"        all image width = 1375-10=1365 & - video width"640"


        if (name != 'Unknown'):
            dim = (276, 276)
            personBG = cv2.imread(white_photo_path, cv2.IMREAD_UNCHANGED)
            personBG = cv2.resize(personBG, dim)
            imgBG = overlayPNG(imgBG, personBG, (50, 250))
            global old_img
            image = old_img

            # '''
            global saved_time
            if round(time.time()) > saved_time:
                person_name = name

                saved_time = round(time.time())
                saved_time += wait_to_change_time     # 3
                print('count sec. passed, changing person`s photo   ')
                old_img = f'{images_path}{name}.png'
            # '''




            try:
                img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
                img2 = cv2.resize(img, dim)
                # print(img.shape)
                imgBG = overlayPNG(imgBG, img2, (50, 250))  # (x, y)
            except:
                1
    cv2.waitKey(1)
    cv2.imshow("Detection..", imgBG)


def main_filter(mode_selected):
    def show_boundaries(rects, color):
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)

    def detect_multi_scale(cascade, min_neighbors, min_size):
        return cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=min_neighbors,
            minSize=min_size,
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    # try:
    if __name__ == "__main__":
        ap = argparse.ArgumentParser()
        ap.add_argument("-f", "--filter", nargs='+', required=False, help="filters to use")
        ap.add_argument("-p", "--package", required=False, help="filter package (optional)")
        ap.add_argument("-b", "--boundaries", required=False, action='store_true',
                        help="show boundaries of detected areas (optional)")
        ap.add_argument("-ce", "--cascade_eye", required=False, help="haar cascade for eye detection (optional)")
        ap.add_argument("-cf", "--cascade_face", required=False, help="haar cascade for face detection (optional)")
        args = vars(ap.parse_args())

        #  Creating a face cascade
        face_cascade_path = CASCADE_DIR + (args["cascade_face"] if args["cascade_face"] else "face.xml")
        eye_cascade_path = CASCADE_DIR + (args["cascade_eye"] if args["cascade_eye"] else "eye.xml")

        face_cascade = cv2.CascadeClassifier(face_cascade_path)
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

        pygame.init()
        pygame.display.set_caption("haircut filter")
        screen = pygame.display.set_mode([640, 480])

        ###*********************************************************************************************************
        while True:
            global name


            # ret, frame = cap.read()
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #
            # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            # for (x, y, w, h) in faces:
            #     img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #     roi_gray = gray[y:y + h, x:x + w]
            #     roi_color = img[y:y + h, x:x + w]
            #     eyes = eye_cascade.detectMultiScale(roi_gray)


            _, my_frame = video_capture.read()
            frame = my_frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            eyes = detect_multi_scale(eye_cascade, 50, (10, 10))
            faces = detect_multi_scale(face_cascade, 50, (30, 30))
            if args["boundaries"]:
                show_boundaries(eyes, (255, 0, 0))
                show_boundaries(faces, (0, 255, 0))
            screen.fill([0, 0, 0])
            frame = np.rot90(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0, 0))
            frame = my_frame
            #
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            # eyes = detect_multi_scale(eye_cascade, 50, (10, 10))
            # faces = detect_multi_scale(face_cascade, 50, (30, 30))
            # if args["boundaries"]:
            #     show_boundaries(eyes, (255, 0, 0))
            #     show_boundaries(faces, (0, 255, 0))
            # screen.fill([0, 0, 0])
            # frame1 = np.rot90(frame1)
            # frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGRA2RGB)
            # frame1 = pygame.surfarray.make_surface(frame1)
            # screen.blit(frame1, (0, 0))
            global gender
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            frameFace, bboxes = getFaceBox(faceNet, small_frame)
            for bbox in bboxes:
                face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
                       max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)     # function returns a blob which is our input image after mean subtraction, normalizing, and channel swapping.
                genderNet.setInput(blob)
                genderPreds = genderNet.forward()
                gender = genderList[genderPreds[0].argmax()]
                print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
            face_locations, face_names = sfr.detect_known_faces(frame, gender)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)

                print(f'you look like: {name}')

                if gender == 'Male':
                    filter1 = name
                ############################################################################################################

            # for bbox in bboxes:
            #     face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
            #            max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
            #     blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            #     genderNet.setInput(blob)
            #     genderPreds = genderNet.forward()
            #     gender = genderList[genderPreds[0].argmax()]
            #     print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
            try:
                filter.show_filter(filter1, eyes, faces, screen)

            except:
                1
            pygame.display.update()
            ###*********************************************************************************************************
            if keyboard.is_pressed('q') or keyboard.is_pressed(' '):
                pygame.quit()
                return 0
            elif keyboard.is_pressed('esc'):
                pygame.quit()
                return -1
            else:
                return 1
        video_capture.release()
        cv2.destroyAllWindows()
        pygame.quit()
    # except:1


sfr = SimpleFacerec()
print('Male Images Encoding:')
sfr.load_encoding_images(images_path_M, 'Male')
print('Female Images Encoding:')
sfr.load_encoding_images(images_path_F, 'Female')

while True:
    if mode_selected == 0:
        # try:
        while mode_selected == 0:
            main_GUI()
            if keyboard.is_pressed('q') or keyboard.is_pressed(' '):
                cv2.destroyAllWindows()
                mode_selected = 1

            elif keyboard.is_pressed('esc'):
                cv2.destroyAllWindows()
                mode_selected = -1
                break
        # except Exception as e:
        #     print(e)
    elif mode_selected == 1:
        mode_selected = main_filter(mode_selected)
    else:
        exit()
