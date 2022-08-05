import cv2
import numpy

f1 = cv2.imread("C:\\Users\\omarh\\Desktop\\baboon.jpg")
f4 = cv2.imread("C:\\Users\\omarh\\Desktop\\baboon1.jpg")
# cv2.imshow("my image", f1)
# cv2.waitKey(0)  # spinlock

f2 = f1
# f6 = cv2.imread("D:\\backup\\Pictures\\phone photos\\nn\\14-8_2.jpg")

# # # show only one color from image:
# # # Blue
# f2[:, :, 1] = 0
# f2[:, :, 2] = 0  ## the selected color is dark
# cv2.imshow("my image blue", f2)

# # # Red
# f1[:, :, 0] = 0
# f1[:, :, 1] = 0  # the selected color is dark
# cv2.imshow("my image", f1)
# f1[:, :, 0] = 255
# f1[:, :, 1] = 255  # the selected color is light

# # # Green
# f1[:, :, 2] = 0
# f1[:, :, 0] = 0  # the selected color is dark
# cv2.imshow("my image green", f1)

# # # display colors on f1 & not in f4    ## f1 & f4 must be same image size.
# f3 = cv2.subtract(f1, f4)
# f3 = f1 - f4

# # # colored image to GrayScale
# gray = cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY)

# # # convert to Black & White:
# # # 1)
# for i in range(0, 512):  # # so 512 is the image width
#     for j in range(0, 512):  # # so 512 is the image height
#         if gray[i, j] >= 120:
#             gray[i, j] = 0
#         else:
#             gray[i, j] = 255

# # # 2)
# gray = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
# res, th1 = cv2.threshold(f2, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("my image", th1)

# # # display only red object in the image on white color and other in black:
import cv2
import numpy

f1 = cv2.imread("path...")
res, th1 = cv2.threshold(f1, 127, 255, cv2.THRESH_BINARY)
green_color = numpy.int16(th1[:, :, 2]) - numpy.int16(th1[:, :, 0]) - numpy.int16(th1[:, :, 1])   # RGB
green_color = numpy.uint8(green_color)
green_color[green_color > 255] = 255
green_color[green_color < 0] = 0

# object mid target:
# # # x access
x = numpy.arange(1, 513)
c_r = numpy.sum(green_color, 0)
mul_cr_x = numpy.multiply(c_r, x)
tot = numpy.sum(mul_cr_x)
sum1 = numpy.sum(green_color, 0)
sum2 = numpy.sum(sum1)
x_center = tot / sum2
# # # y access
y = numpy.arange(1, 513)
c_r = numpy.sum(green_color, 1)
mul_cr_y = numpy.multiply(c_r, y)
tot = numpy.sum(mul_cr_y)
sum1 = numpy.sum(green_color, 1)
sum2 = numpy.sum(sum1)
y_center = tot / sum2
print(f"center or green object (x, y): ({x_center}, {y_center})")

cv2.imshow("green object", green_color)
cv2.waitKey(0)  # # spinlock
