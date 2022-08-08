# edited by 3omar.hs
# other filters project to see: https://github.com/shyaa23/Snapchat-like-Filters-Using-Computer-Vision-Techniques
# opencv change images using buttons: https://www.youtube.com/watch?v=7Uhw2nrkqa8
# use tkinter with pygame: https://python-forum.io/thread-17965.html

# this project link:
# https://github.com/OlaPietka/Snapchat-Filters



import argparse
import sys
import keyboard
import cv2
import numpy as np
import pygame
import filter

#  Directory paths
CASCADE_DIR = "data/cascades/"


filter1 = "mask"


def main():

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

    if __name__ == "__main__":
        ap = argparse.ArgumentParser()
        ap.add_argument("-f", "--filter", nargs='+', required=False, help="filters to use")
        ap.add_argument("-p", "--package", required=False, help="filter package (optional)")
        ap.add_argument("-b", "--boundaries", required=False, action='store_true', help="show boundaries of detected areas (optional)")
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
        pygame.display.set_caption("Snapchat filters")
        screen = pygame.display.set_mode([640, 480])

        #  Sets the video source to the default webcam
        video_capture = cv2.VideoCapture(0)

        while True:
            #  Read one frame from the video source (webcam)
            _, frame = video_capture.read()

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



            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed
                    filter1 = "santabeard"
                    print('You choose santabeard filter!')
                elif keyboard.is_pressed('w'):  # if key 'q' is pressed
                    filter1 = "santahat"
                    print('You choose santahat filter!')
                elif keyboard.is_pressed('e'):  # if key 'q' is pressed
                    filter1 = "clownhair"
                    print('You choose clownhair filter!')
                elif keyboard.is_pressed('r'):  # if key 'q' is pressed
                    filter1 = "clownnose"
                    print('You choose clownnose filter!')
                elif keyboard.is_pressed('t'):  # if key 'q' is pressed
                    filter1 = "mustache"
                    print('You choose mustache filter!')
                elif keyboard.is_pressed('y'):  # if key 'q' is pressed
                    filter1 = "hat"
                    print('You choose hat filter!')
                elif keyboard.is_pressed('u'):  # if key 'q' is pressed
                    filter1 = "glasses"
                    print('You choose glasses filter!')
                elif keyboard.is_pressed('i'):  # if key 'q' is pressed
                    filter1 = "ballmask"
                    print('You choose ballmask filter!')
                elif keyboard.is_pressed('o'):  # if key 'q' is pressed
                    filter1 = "eyeballs"
                    print('You choose eyeballs filter!')
                elif keyboard.is_pressed('s'):  # if key 'q' is pressed
                    filter1 = "eyes"
                    print('You choose eyes filter!')
                elif keyboard.is_pressed('a'):  # if key 'q' is pressed
                    filter1 = "mustache2"
                    print('You choose mustache2 filter!')
                elif keyboard.is_pressed('p'):  # if key 'q' is pressed
                    filter1 = "pinkglasses"
                    print('You choose pinkglasses filter!')
                elif keyboard.is_pressed('d'):  # if key 'q' is pressed
                    filter1 = "pinkhair"
                    print('You choose pinkhair filter!')
                elif keyboard.is_pressed('f'):  # if key 'q' is pressed
                    filter1 = "pinklips"
                    print('You choose pinklips filter!')
                elif keyboard.is_pressed('g'):  # if key 'q' is pressed
                    filter1 = "silverglasses"
                    print('You choose silverglasses filter!')
                elif keyboard.is_pressed('h'):  # if key 'q' is pressed
                    filter1 = "sunglasses"
                    print('You choose sunglasses filter!')
                # else:
                #     filter1 = "mask"
                #     print('You didn`t choose a filter!!')
            except:1

            try:
                filter.show_filter(filter1, eyes, faces, screen)
                # filter.show_filter("santahat", eyes, faces, screen)

            except:1


            #  Display the resulting frame
            pygame.display.update()

            for event in pygame.event.get():1
                # if event.type == pygame.KEYDOWN:
                #     sys.exit(0)

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
        pygame.quit()


# try:
main()
# except Exception:
# #     # traceback.print_exc()
#     pygame.quit()
