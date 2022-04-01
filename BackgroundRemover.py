import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

#to resize bg image in the folder to 640 X 480.

import cv2
img = cv2.imread('3.jpg')
img = cv2.resize(img, (640,480))
# cv2.imshow("img", img)
# cv2.waitKey(0)
cv2.imwrite("5.jpg", img)

# pop up a window if you have a webcam, Here the frame size is 640 X 480.
# So we need to take a note here because the background replacing images should be of the same size as the frame, that is 640 X 480.
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# cap.set(cv2.CAP_PROP_FPS, 60)

#‘SelfiSegmentation’ is used to remove the background of the frame and replace it with our images in the directory.
segmentor = SelfiSegmentation()
#In order to display the frames per second(fps) in the output frames, we use cvzone.FPS() function.
fpsReader = cvzone.FPS()

# imgBG = cv2.imread("BackgroundImages/3.jpg")


imgBg = cv2.imread("5.jpg")

while True:
    success, img = cap.read()
    # imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83)
    # The threshold cuts everything if it’s set to 1, here we set it to 0.8, for better edges, play with different threshold values
    imgOut = segmentor.removeBG(img, imgBg, threshold=0.8)

    cv2.imshow("image", imgOut)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break