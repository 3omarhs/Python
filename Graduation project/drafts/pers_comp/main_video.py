import cv2
from simple_facerec import SimpleFacerec

path = "10photos/"
class detect_face:
    def __init__(self):
        photoname = ''
        oldphoto = ''

    def load_encoding_images(self, images_path):
        photoname = ''
        oldphoto = ''
        sfr = SimpleFacerec()
        sfr.load_encoding_images(images_path)
        cap = cv2.VideoCapture(0)

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
    detect_face.load_encoding_images(self=None,images_path=path)
except:
    print("Ended!")
