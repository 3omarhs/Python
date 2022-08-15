import cv2
import face_recognition
import pickle
import os
import glob


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path, category):
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
        # with open(f'encoded images files/{category}_encoding.txt', 'w') as f:
        #     f.write(str(self.known_face_encodings))

        with open(f'encoded images files/{category}_encoding.txt', "wb") as fp:  # Pickling
            pickle.dump(self.known_face_encodings, fp)
        # with open(f'encoded images files/{category}_encoding.txt', 'w') as f:
        #     for s in self.known_face_encodings:
        #         f.write(str(s) + '*#*')

        with open(f'encoded images files/{category}_names.txt', "wb") as fp:  # Pickling
            pickle.dump(self.known_face_names, fp)
        # with open(f'encoded images files/{category}_names.txt', 'w') as f:
        #     for s in self.known_face_names:
        #         f.write(str(s) + '*#*')

        # with open(f'encoded images files/{category}_names.txt', 'w') as f:
        #     f.write(str(self.known_face_names))

####### read


    # def load_encoding_images(self, images_path, category):
    #     # with open(f'encoded images files/{category}_encoding.txt', 'r') as f:
    #     #     try: self.known_face_encodings = [float(line.rstrip('*#*')) for line in f]
    #     #     except: self.known_face_encodings = [line.rstrip('*#*') for line in f]
    #     with open(f'encoded images files/{category}_encoding.txt', "rb") as fp:  # Unpickling
    #         self.known_face_encodings = pickle.load(fp)
    #
    #     # with open(f'encoded images files/{category}_names.txt', 'r') as f:
    #     #     self.known_face_names = [line.rstrip('*#*') for line in f]
    #     with open(f'encoded images files/{category}_names.txt', "rb") as fp:  # Unpickling
    #         self.known_face_names = pickle.load(fp)
    #     print("Encoding images loaded")
