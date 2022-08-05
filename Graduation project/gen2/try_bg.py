import cv2
import cvzone

# cap = cv2.VideoCapture(0)
while True:
    # success, img = cap.read()
    imgBG = cv2.imread("BG.jpg")
    img = cv2.imread(f'1.png', cv2.IMREAD_UNCHANGED)
    imgBG = cvzone.overlayPNG(imgBG, img, (0, 0))
    # print(img.shape())
    # img = cv2.imread("BG0.jpg")
    #
    # imgBG = cvzone.overlayPNG(imgBG, img)

    cv2.imshow("BG", imgBG)
    key = cv2.waitKey(0)


    #(480,640,3) into shape (466,400,3)