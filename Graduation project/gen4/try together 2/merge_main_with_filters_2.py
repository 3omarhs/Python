# other filters project to see: https://github.com/shyaa23/Snapchat-like-Filters-Using-Computer-Vision-Techniques
# opencv change images using buttons: https://www.youtube.com/watch?v=7Uhw2nrkqa8
# use tkinter with pygame: https://python-forum.io/thread-17965.html

# this project link:
# https://github.com/OlaPietka/Snapchat-Filters

# alternative gender detectiqqon CNN project: https://sefiks.com/2020/09/07/age-and-gender-prediction-with-deep-learning-in-opencv/



import face_recognition
import os
import glob
import argparse
import sys
import keyboard
import cv2
import numpy as np
import pygame
import filter0
import random
import pickle



camera_number = 0
oldphoto = ''
gender = ''
filter1 = ""
img2 = ''
mode_selected = 0
compare_faces_accuracy = 1  # 0 - 1
encoding_images_path = '../encoded images files'
BG_photo_path = "../photos/BG.jpg"
white_photo_path = '../photos/white.png'

# images_path_M = 'C:/Users/Omar Hassan/Desktop/New folder/'
images_path_M = '../photos/mens/'

# images_path_F = 'D:/Backup/PycharmProjects/datasets/10photos_w/'
images_path_F = '../photos/10photos_w/'








faceProto = "../AGE-Gender-Detection-main/opencv_face_detector.pbtxt"
faceModel = "../AGE-Gender-Detection-main/opencv_face_detector_uint8.pb"

ageProto = "../AGE-Gender-Detection-main/age_deploy.prototxt"
ageModel = "../AGE-Gender-Detection-main/age_net.caffemodel"

genderProto = "../AGE-Gender-Detection-main/gender_deploy.prototxt"
genderModel = "../AGE-Gender-Detection-main/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']
# load the network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)
# cap = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture(camera_number)
cap = video_capture
padding = 20

#  Directory paths
CASCADE_DIR = "data/cascades/"





class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    # def load_encoding_images(self, images_path, category):
    #     """
    #     Load encoding images from path
    #     :param images_path:
    #     :return:
    #     """
    #     # Load Images
    #     images_path = glob.glob(os.path.join(images_path, "*.*"))
    #
    #     print("{} encoding images found.".format(len(images_path)))
    #
    #     # Store image encoding and names
    #     for img_path in images_path:
    #         img = cv2.imread(img_path)
    #         rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #
    #         # Get the filename only from the initial file path.
    #         basename = os.path.basename(img_path)
    #         (filename, ext) = os.path.splitext(basename)
    #         # Get encoding
    #         try:
    #             img_encoding = face_recognition.face_encodings(rgb_img)[0]    ##########################################################################
    #         except:1
    #
    #         # Store file name and file encoding
    #         self.known_face_encodings.append(img_encoding)
    #         self.known_face_names.append(filename)
    #     print("Encoding images loaded")
    #     # with open(f'encoded images files/{category}_encoding.txt', 'w') as f:
    #     #     f.write(str(self.known_face_encodings))
    #
    #     with open(f'{encoding_images_path}/{category}_encoding.txt', "wb") as fp:  # Pickling
    #         pickle.dump(self.known_face_encodings, fp)
    #     # with open(f'encoded images files/{category}_encoding.txt', 'w') as f:
    #     #     for s in self.known_face_encodings:
    #     #         f.write(str(s) + '*#*')
    #
    #     with open(f'{encoding_images_path}/{category}_names.txt', "wb") as fp:  # Pickling
    #         pickle.dump(self.known_face_names, fp)
    #     # with open(f'encoded images files/{category}_names.txt', 'w') as f:
    #     #     for s in self.known_face_names:
    #     #         f.write(str(s) + '*#*')
    #
    #     # with open(f'encoded images files/{category}_names.txt', 'w') as f:
    #     #     f.write(str(self.known_face_names))


    def load_encoding_images(self, images_path, category):
        # with open(f'encoded images files/{category}_encoding.txt', 'r') as f:
        #     try: self.known_face_encodings = [float(line.rstrip('*#*')) for line in f]
        #     except: self.known_face_encodings = [line.rstrip('*#*') for line in f]
        with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
            self.known_face_encodings = pickle.load(fp)

        # with open(f'encoded images files/{category}_names.txt', 'r') as f:
        #     self.known_face_names = [line.rstrip('*#*') for line in f]
        with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
            self.known_face_names = pickle.load(fp)
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
            else:
                name = self.known_face_names[random.randint(0, len(self.known_face_names))]
                print(f'randomly selected {name}')
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names



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



def main_GUI():
    hasFrame, frame = cap.read()
    imgBG = cv2.imread(BG_photo_path)
    imgBG[170:650, 725:1365] = frame
    cv2.putText(imgBG, f'Finding Best Haircut For You`r Face..', (70, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),
                6)

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

        cv2.putText(frame, (name + ',' + gender), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.putText(imgBG, f'The best Haircut For You ', (20, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        cv2.putText(imgBG, f' Is Like: {name}', (50, 230), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        # cv2.putText(frame, (name), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)
        imgBG[170:650,
        725:1365] = frame  # all image height = 700-50=650 & - video height"480"        all image width = 1375-10=1365 & - video width"640"

        if (name != 'Unknown'):
            # img = cv2.imread(r"C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen2\photos\10photos\Aaron_Pena_0001.png", cv2.IMREAD_UNCHANGED)
            dim = (276, 276)
            personBG = cv2.imread(white_photo_path, cv2.IMREAD_UNCHANGED)
            personBG = cv2.resize(personBG, dim)
            imgBG = overlayPNG(imgBG, personBG, (50, 250))

            try:
                # img = cv2.imread(r"C:\Users\Omar Hassan\Desktop\New folder (5)\Adam Levine\Adam Levine (9).png", cv2.IMREAD_UNCHANGED)
                img = cv2.imread(f'{images_path}{name}.png', cv2.IMREAD_UNCHANGED)
                img2 = cv2.resize(img, dim)
                # print(img.shape)
                imgBG = overlayPNG(imgBG, img2, (50, 250))  # (x, y)
            except:
                1
        # except:1
    cv2.waitKey(1)
    cv2.imshow("Detection..", imgBG)





def main_filter():

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

    try:
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

            #  Init display
            pygame.init()
            pygame.display.set_caption("haircut filter")
            screen = pygame.display.set_mode([640, 480])

            #  Sets the video source to the default webcam
            video_capture = cv2.VideoCapture(camera_number)

            ###*********************************************************************************************************
            while True:
                #  Read one frame from the video source (webcam)
                _, my_frame = video_capture.read()
                frame = my_frame

                #  Converted our webcam feed
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

                #  Detect eyes and feces in our frame.
                eyes = detect_multi_scale(eye_cascade, 50, (10, 10))
                faces = detect_multi_scale(face_cascade, 50, (30, 30))

                # Show boundaries
                if args["boundaries"]:
                    show_boundaries(eyes, (255, 0, 0))
                    show_boundaries(faces, (0, 255, 0))

                #  Mange screen
                screen.fill([0, 0, 0])
                frame = np.rot90(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
                frame = pygame.surfarray.make_surface(frame)
                screen.blit(frame, (0, 0))

                # Loop over the list of filters
                # if args["filter"]:
                #     for filter_name in args["filter"]:
                #         filter.show_filter(filter_name, eyes, faces, screen)
                # elif args["package"]:
                #     filter.show_filter_package(args["package"], eyes, faces, screen)

                ############################################################################################################

                # hasFrame, frame = video_capture.read()
                frame = my_frame

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                eyes = detect_multi_scale(eye_cascade, 50, (10, 10))
                faces = detect_multi_scale(face_cascade, 50, (30, 30))
                # Show boundaries
                if args["boundaries"]:
                    show_boundaries(eyes, (255, 0, 0))
                    show_boundaries(faces, (0, 255, 0))
                screen.fill([0, 0, 0])
                frame1 = np.rot90(frame1)
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGRA2RGB)
                frame1 = pygame.surfarray.make_surface(frame1)
                screen.blit(frame1, (0, 0))

                small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                frameFace, bboxes = getFaceBox(faceNet, small_frame)
                for bbox in bboxes:
                    face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
                           max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
                    blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                    genderNet.setInput(blob)
                    genderPreds = genderNet.forward()
                    gender = genderList[genderPreds[0].argmax()]
                    # if gender == 'Male':
                    #     images_path = images_path_M
                    # else:
                    #     images_path = images_path_F
                    print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
                face_locations, face_names = sfr.detect_known_faces(frame)
                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)

                    print(f'you look like: {name}')

                    if gender == 'Male':
                        # if '01' in name:
                        #     filter1 = 'hair1'
                        # el
                        if name == 'Dev Patel (6)':
                            filter1 = 'hair3'
                        elif name == 'tom holland (3)':
                            filter1 = 'hair5'
                        elif name == 'Unknown':
                            filter1 = 'hair6'

                        # else:
                        #     filter1 = ''
                        else:
                            filter1 = 'hair9'

                    # if (name != 'Unknown'):
                    #     # img = cv2.imread(r"C:\Users\Omar Hassan\PycharmProjects\Graduation project\gen2\photos\10photos\Aaron_Pena_0001.png", cv2.IMREAD_UNCHANGED)
                    #     dim = (276, 276)
                    #     # img = cv2.imread(f'photos/10photos0/{name}.png', cv2.IMREAD_UNCHANGED)
                    #     img = cv2.imread(f'{images_path_M}{name}.png', cv2.IMREAD_UNCHANGED)
                    #     # img = cv2.imread(f'{images_path_M}{name}.jpg', cv2.IMREAD_UNCHANGED)
                    #     img2 = cv2.resize(img, dim)
                    #     # img = cv2.resize(img, (350, 350), interpolation= cv2.INTER_AREA)  # cv2.INTER_CUBIC)cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                    #     imgBG = overlayPNG(imgBG, img2, (50, 250))  # (x, y)
                    # except:1
                    ############################################################################################################

                    # try:  # used try so that if user pressed other than the given key error will not be shown
                    if keyboard.is_pressed('q'):  # if key 'q' is pressed
                        filter1 = "hair1"
                        print('You choose santabeard filter!')
                    elif keyboard.is_pressed('w'):  # if key 'q' is pressed
                        filter1 = "hair2"
                        print('You choose santahat filter!')
                    elif keyboard.is_pressed('e'):  # if key 'q' is pressed
                        filter1 = "hair3"
                        print('You choose clownhair filter!')
                    elif keyboard.is_pressed('r'):  # if key 'q' is pressed
                        filter1 = "hair4"
                        print('You choose clownnose filter!')
                    elif keyboard.is_pressed('t'):  # if key 'q' is pressed
                        filter1 = "hair5"
                        print('You choose mustache filter!')
                    elif keyboard.is_pressed('y'):  # if key 'q' is pressed
                        filter1 = "hair6"
                        print('You choose hat filter!')
                    elif keyboard.is_pressed('u'):  # if key 'q' is pressed
                        filter1 = "hair7"
                        print('You choose glasses filter!')
                    elif keyboard.is_pressed('i'):  # if key 'q' is pressed
                        filter1 = "hair8"
                        print('You choose ballmask filter!')
                    elif keyboard.is_pressed('o'):  # if key 'q' is pressed
                        filter1 = "hair9"
                        print('You choose eyeballs filter!')
                    # else:
                    #     filter1 = "mask"
                    #     print('You didn`t choose a filter!!')
                # except:1

                try:
                    # filter.show_filter(filter1, eyes, faces, screen)
                    # print(f'filter1{filter1}')
                    filter0.show_filter(filter1, eyes, faces, screen)
                    # filter.show_filter("santahat", eyes, faces, screen)

                except:
                    1

                #  Display the resulting frame
                pygame.display.update()

                for event in pygame.event.get(): 1
                # if event.type == pygame.KEYDOWN:
                #     sys.exit(0)
            ###*********************************************************************************************************
                if keyboard.is_pressed('q'):
                    mode_selected = 0
                    video_capture.release()
                    cv2.destroyAllWindows()
                    pygame.quit()
                    break
            # When everything is done, release the capture
            video_capture.release()
            cv2.destroyAllWindows()
            pygame.quit()
    except:1





sfr = SimpleFacerec()
print('Male Images Encoding:')
sfr.load_encoding_images(images_path_M, 'Male')
print('Female Images Encoding:')
sfr.load_encoding_images(images_path_F, 'Female')



while True:
    if mode_selected == 0:
        try:
            while mode_selected != 1:
                main_GUI()
                if keyboard.is_pressed('q'):
                    cv2.destroyAllWindows()
                    mode_selected = 1
        except Exception as e:
            print(e)

    else:
        try:
            main_filter()
        except Exception as e:
            print(e)
#     # traceback.print_exc()
#     pygame.quit()