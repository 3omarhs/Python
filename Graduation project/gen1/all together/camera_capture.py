import cv2
class detect_face:
    def __init__(self):
        pass

    def countphotos(self):
        import os
        # folder path
        dir_path = r'C:\Users\Omar Hassan\PycharmProjects\Graduation project\all together\captured_images'
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        # print('File count:', count)
        return count

    def capture(self):

        cam = cv2.VideoCapture(0)
        cv2.namedWindow("tap space to capture")
        img_counter = detect_face.countphotos(self=None)

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("tap space to capture", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "captured_images/person_{}.jpg".format(img_counter)
                # img_name = "Your_Image_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                print("You`r photo has been captured sucessfully..")
                break

        cam.release()

        cv2.destroyAllWindows()
        return img_name+''

# detect_face.capture(self=None)