# https://soumyapatilblogs.medium.com/face-and-eyes-detection-using-opencv-9fcad47656a4
# resultimage = cv2.bitwise_and(imageread1, imageread2, mask = None)
# added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)


import cv2


def process_image(image_path, resize_x, resize_y, scale_x, scale_y, frame):
# def process_image(image_path, increase_sizex, increase_sizey, move_right, move_up, frame):
    resize_x = int(resize_x)
    resize_y = int(resize_y)
    scale_x = int(scale_x)
    scale_y = int(scale_y)
    logo = image_path

    logo = cv2.resize(logo, (resize_y, resize_x))

    # (x, y), (x + w, y + h)

    # logo = cv2.imread(image_path)
    # centerX = x+(w/2)
    # centerY = y+(h/2)
    # roi = frame[scale_y:scale_y+resize_y, scale_x:scale_x+resize_x]
    # roi += logo
    frame[scale_y:scale_y+resize_y, scale_x:scale_x+resize_x] += logo

    return frame


#
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     # frame = add_haircut(frame=frame, image_path='data/filters/hair5.png')
#     frame = process_image(image_path=cv2.imread('data/hair5.png'), frame=frame)
#     cv2.imshow('WebCam', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
