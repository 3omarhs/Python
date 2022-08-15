# https://pysource.com/2021/08/16/face-recognition-in-real-time-with-opencv-and-python/
# https://www.youtube.com/watch?v=5yPeKQzCPdI
# not used:
# https://towardsdatascience.com/celebrity-doppelganger-finder-using-vgg-face-dataset-dlib-and-opencv-30ea1806200
# https://sefiks.com/2019/02/13/apparent-age-and-gender-prediction-in-keras/
# https://sefiks.com/2019/05/05/celebrity-look-alike-face-recognition-with-deep-learning-in-keras/
# https://www.kaggle.com/code/gustavoliberado/understanding-pca-applying-it-for-compression
# https://www.kaggle.com/code/serkanpeldek/face-detection-with-opencv/data
# https://www.kaggle.com/code/serkanpeldek/face-detection-with-opencv/notebook


import cv2
from simple_facerec import SimpleFacerec

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
try:
    detect_face.load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/10photos/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_8.jpg')
    # 1
    # detect_face.load_encoding_images(self=None,images_path="D:/Backup/PycharmProjects/datasets/men/",personPhoto=r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images\person_100.jpg')
except:
    print("Ended!")
