import glob
import os
import time
import face_recognition
import keyboard
import cv2
import numpy as np
import filter
import filter_w
import pickle

# current_run = 'train'
current_run = 'run'
mode_selected = 0   # select which mode to start run with..
# mode_selected = 1
tolerance=0.80  #un-accuracy "error" percentage
camera_number = 0  # change to change to other camera connected to this device..
wait_to_change_time = 2  # time to change between persons photos in mode0 and to change haircut in mode1
run_fully = True  # in second mode to just view haircuts (controlled using arrows) without finding most likely person or gender detection..
# run_fully = False
threshold_of_read_face = 0.75

oldphoto = ''
gender = ''
filter1 = filter2 = ""
img2 = ''
male = ''
person_name = ''
old_img = r'photos\mens\Ashton Kutcher (4).png'  #first photo define in mode0 (will not be shown but mustn't be null).
saved_time_2 = saved_time = round(time.time())  # ass millis timer..
encoding_images_path = 'encoded images files'
BG_photo_path = "photos/BG.jpg"
white_photo_path = 'photos/white.png'
images_path_M = 'photos/mens/'
images_path_F = 'photos/womens/'
images_path_M_single_per = 'photos/mens1/'
images_path_F_single_per = 'photos/womens1/'
images_path = ''
Male_list = []
Female_list = []
filter3_m = 0
filter3_f = 0


faceProto = "AGE-Gender-Detection-main/opencv_face_detector.pbtxt"
faceModel = "AGE-Gender-Detection-main/opencv_face_detector_uint8.pb"

genderProto = "AGE-Gender-Detection-main/gender_deploy.prototxt"
genderModel = "AGE-Gender-Detection-main/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
genderList = ['Male', 'Female']

#load the network:
genderNet = cv2.dnn.readNet(genderModel, genderProto)  # create and manipulate comprehensive artificial neural networks (for gender det.)
faceNet = cv2.dnn.readNet(faceModel, faceProto)  # create and manipulate comprehensive artificial neural networks (for gender det.)
video_capture = cv2.VideoCapture(camera_number)  # return selected camera capturing video

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
                img = cv2.imread(img_path)  # read and show image
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert image to another color space, There are more than 150 color-space
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)  # split colored/multi-channel image into separate single-channel images
                try:
                    img_encoding = face_recognition.face_encodings(rgb_img)[0]  #return the 128-dimension face encoding for each face
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
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)  # to change photo size
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # convert image to another color space, There are more than 150 color-space
        face_locations = face_recognition.face_locations(rgb_small_frame)  # bounding boxes of human faces
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # return the 128-dimension face encoding for each face
        face_names = []
        for face_encoding in face_encodings:
            if category == 'Male':
                matches = face_recognition.compare_faces(self.known_face_encodings_m, face_encoding, tolerance=tolerance)  # Compare faces to see if they match
            else:
                matches = face_recognition.compare_faces(self.known_face_encodings_f, face_encoding, tolerance=tolerance)  # Compare faces to see if they match
            name = "Unknown"

            if category == 'Male':
                face_distances = face_recognition.face_distance(self.known_face_encodings_m, face_encoding)  # get distance (un-similarity) for each comparison face
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names_m[best_match_index]
                else:
                    print('unknown detected!!')
                if len(face_names) < 2:
                    face_names.append(name)
            else:
                face_distances = face_recognition.face_distance(self.known_face_encodings_f, face_encoding)  # get distance (un-similarity) for each comparison face
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names_f[best_match_index]
                else:
                    print('unknown detected!!')
                if len(face_names) < 2:
                    face_names.append(name)
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names

def getFaceBox(net, frame, conf_threshold=threshold_of_read_face):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)     # "read caffe model" function returns a blob which is our input image after mean subtraction, normalizing, and channel swapping.
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
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)  # draw rectangle on photo “usually used for face boundaries”
    return frameOpencvDnn, bboxes

def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)  # split colored/multi-channel image into separate single-channel images
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)  # convert image to another color space, There are more than 150 color-space
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # convert image to another color space, There are more than 150 color-space
    try:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)  # merging photos
    except:
        imgRGBA = cv2.bitwise_and(imgFront, maskBGR)  # merging photos
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)  # convert image to another color space, There are more than 150 color-space
    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv
    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)  # merging photos
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)
    return imgBack

def fill_Male_list():
    file_list = os.listdir(images_path_M_single_per)
    for img_name in file_list:
        Male_list.append(img_name[:-4])


def fill_Female_list():
    file_list = os.listdir(images_path_F_single_per)
    for img_name in file_list:
        Female_list.append(img_name[:-4])

fill_Male_list()
fill_Female_list()

def main_GUI():
    # read frame:
    hasFrame, frame = cap.read()
    imgBG = cv2.imread(BG_photo_path)  # read and show image
    imgBG[170:650, 725:1365] = frame
    cv2.putText(imgBG, f'Finding Best Haircut For You`r Face..', (70, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255),6)  # to add text into an image
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # creating a smaller frame for better optimization:
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
            images_path = images_path_M_single_per
        else:
            images_path = images_path_F_single_per
        print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
    face_locations, face_names = sfr.detect_known_faces(frame, gender)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        try:
            cv2.putText(frame, (gender[0] + ', ' + name), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)  # to add text into an image
        except:
            1
        global person_name
        cv2.putText(imgBG, f'The best Haircut For You ', (20, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)  # to add text into an image
        cv2.putText(imgBG, f' Is Like: {person_name}', (50, 230), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)  # to add text into an image
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 3)  # draw rectangle on photo “usually used for face boundaries”
        imgBG[170:650, 725:1365] = frame  # all image height = 700-50=650 & - video height"480"        all image width = 1375-10=1365 & - video width"640"

        if (name != 'Unknown'):
            name = name[:-4]
            name1 = name[:-1]
            name2 = name[:-2]
            dim = (276, 276)
            personBG = cv2.imread(white_photo_path, cv2.IMREAD_UNCHANGED)  # read and show image
            personBG = cv2.resize(personBG, dim)  # to change photo size
            imgBG = overlayPNG(imgBG, personBG, (50, 250))
            global old_img
            global saved_time
            image = old_img
            if round(time.time()) > saved_time:
                person_name = name
                print(person_name)
                saved_time = round(time.time())
                saved_time += wait_to_change_time     # 3
                print('count sec. passed, changing person`s photo   ')
                try:
                    cv2.resize(cv2.imread(f'{images_path}{name}.png'), dim)
                    old_img = f'{images_path}{name}.png'
                except:
                    try:
                        cv2.resize(cv2.imread(f'{images_path}{name1}.png'), dim)
                        old_img = f'{images_path}{name1}.png'
                    except:
                        cv2.resize(cv2.imread(f'{images_path}{name2}.png'), dim)
                        old_img = f'{images_path}{name2}.png'
            try:
                img = cv2.imread(image, cv2.IMREAD_UNCHANGED)  # read and show image
                img2 = cv2.resize(img, dim)  # to change photo size
                # print(img.shape)
                imgBG = overlayPNG(imgBG, img2, (50, 250))  # (x, y)
            except:
                1
    cv2.waitKey(1)  # read and show image
    cv2.imshow("Detection..", imgBG)  # read and show image

def filter_GUI(mode_selected):
    def show_boundaries(rects, color):
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)  # draw rectangle on photo “usually used for face boundaries”

    def detect_multi_scale(cascade, min_neighbors, min_size):
        return cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=min_neighbors,
            minSize=min_size,
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    if __name__ == "__main__":
        face_cascade = cv2.CascadeClassifier('data/cascades/face.xml')

        while True:
            global name
            imgBG = cv2.imread(BG_photo_path, -1)  # read and show image
            _, my_frame = video_capture.read()
            frame = my_frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert image to another color space, There are more than 150 color-space
            faces = detect_multi_scale(face_cascade, 50, (30, 30))
            global run_fully
            global gender
            if keyboard.is_pressed('f'):
                print('switch to manual_F mode!')
                run_fully = False
                gender = 'Female'
            elif keyboard.is_pressed('m'):
                print('switch to manual_M mode!')
                run_fully = False
                gender = 'Male'
            elif keyboard.is_pressed('a'):
                print('switch to Automatic mode!')
                run_fully = True

            if run_fully:
                small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # to change photo size
                frameFace, bboxes = getFaceBox(faceNet, small_frame)
                global images_path
                for bbox in bboxes:
                    face = small_frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
                           max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
                    try:
                        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)  # function returns a blob which is our input image after mean subtraction, normalizing, and channel swapping.
                        genderNet.setInput(blob)
                    except:
                        1
                    genderPreds = genderNet.forward()
                    gender = genderList[genderPreds[0].argmax()]
                    if gender == 'Male':
                        images_path = images_path_M
                    else:
                        images_path = images_path_F
                    print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
                face_locations, face_names = sfr.detect_known_faces(frame, gender)
                for face_loc, name in zip(face_locations, face_names):
                    print(f'you look like: {name}')
                    global filter2
                    global saved_time_2
                    if round(time.time()) > saved_time_2:
                        filter2 = name
                        saved_time_2 = round(time.time())
                        saved_time_2 += wait_to_change_time  # 3

                    if gender == 'Male':
                        try:
                            frame = filter.show_filter(filter2, faces, frame)
                            cv2.putText(imgBG, f'M, {name[:3]}', (70, 170), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 255), 6)  # to add text into an image
                        except:
                            cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 8)  # to add text into an image
                            cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)  # to add text into an image
                    elif gender == 'Female':
                        try:
                            frame = filter_w.show_filter(filter2, faces, frame)
                            cv2.putText(imgBG, f'F, {name[:3]}', (70, 170), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 255), 6)  # to add text into an image
                        except:
                            cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 8)  # to add text into an image
                            cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)  # to add text into an image
                    else:
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 8)  # to add text into an image
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)  # to add text into an image

            else:
                global filter3_m
                global filter3_f
                if gender == 'Male':
                    if keyboard.is_pressed('right'):
                        filter3_m += 1
                        if filter3_m > len(Male_list)-1:
                            filter3_m = 0
                        time.sleep(0.1)
                    elif keyboard.is_pressed('left'):
                        filter3_m -= 1
                        if filter3_m < -1*(len(Male_list)-1):
                            filter3_m = 0
                        time.sleep(0.1)
                    print(Male_list[filter3_m])
                    try:
                        frame = filter.show_filter(str(Male_list[filter3_m]), faces, frame)
                        cv2.putText(imgBG, f'M, {str(Male_list[filter3_m])[:3]}', (70, 170), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 6)  # to add text into an image
                    except:
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 8)  # to add text into an image
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)  # to add text into an image
                else:
                    if keyboard.is_pressed('right'):
                        filter3_f += 1
                        if filter3_f > len(Female_list)-1:
                            filter3_f = 0
                        time.sleep(0.1)
                    elif keyboard.is_pressed('left'):
                        filter3_f -= 1
                        if filter3_f < -1*(len(Female_list)-1):
                            filter3_f = 0
                        time.sleep(0.1)
                    print(Female_list[filter3_f])
                    try:
                        frame = filter_w.show_filter(str(Female_list[filter3_f]), faces, frame)
                        cv2.putText(imgBG, f'F, {str(Female_list[filter3_f])[:3]}', (70, 170), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 6)  # to add text into an image
                    except:
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 8)  # to add text into an image
                        cv2.putText(imgBG, f'Hair is out of bounds, move or step away a bit..', (50, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)  # to add text into an image
            cv2.putText(imgBG, f'Placing the haircut on your face..', (70, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)  # to add text into an image
            imgBG[150:630, 367:1007] = frame  # boundaries: [top:down, left:right]    ## live stream video size: 480 * 640
            cv2.waitKey(1)  # read and show image
            cv2.imshow("Mode(2) fitting haircut into face..", imgBG)  # read and show image
            if keyboard.is_pressed('q') or keyboard.is_pressed(' '):
                cv2.destroyAllWindows()
                return 0
            elif keyboard.is_pressed('esc'):
                cv2.destroyAllWindows()
                return -1

sfr = SimpleFacerec()
print('Male Images Encoding:')
sfr.load_encoding_images(images_path_M, 'Male')
print('Female Images Encoding:')
sfr.load_encoding_images(images_path_F, 'Female')


try:
    while True:
        if mode_selected == 0:
            while mode_selected == 0:
                main_GUI()
                if keyboard.is_pressed('q') or keyboard.is_pressed(' '):
                    cv2.destroyAllWindows()
                    mode_selected = 1

                elif keyboard.is_pressed('esc'):
                    cv2.destroyAllWindows()
                    mode_selected = -1
                    break
        elif mode_selected == 1:
            mode_selected = filter_GUI(mode_selected)
        else:
            exit()
except:
    pass