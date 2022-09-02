import cv2
import face_recognition
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
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

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

class detect_face:
    def __init__(self):
        # Encode faces from a folder
        # sfr.load_encoding_images("images/")
        # sfr.load_encoding_images("D:/Backup/PycharmProjects/datasets/Celebrities photos/")
        # Load Camera
        photoname = ''
        oldphoto = ''

    def load_encoding_images(self, images_path, personPhoto):
        photoname = ''
        oldphoto = ''
        sfr = SimpleFacerec()
        # sfr.load_encoding_images("D:/Backup/PycharmProjects/datasets/10photos/")
        sfr.load_encoding_images(images_path)
        cap = cv2.VideoCapture(0)


        while True:
            ret, frame = cap.read()
            # ret, frame = r"C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_8.jpg"
            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                # if(name == 'Unknown'):
                #     name = 'Aaron_Eckhart_0001'
                photoname = name
                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            cv2.imshow("Scan Your face to detect the best hair cut for you", frame)
            if(photoname != 'Unknown'):
                # img = cv2.imread(f'D:/Backup/PycharmProjects/datasets/500photos/{photoname}.jpg')
                img = cv2.imread(f'{images_path}/{photoname}.png')
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
# try:
detect_face.load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/10photos/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_8.jpg')
    # 1
    # detect_face.load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/men/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_100.jpg')
# except:
#     print("Ended!")
