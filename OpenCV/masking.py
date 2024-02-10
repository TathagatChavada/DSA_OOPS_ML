import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)


blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

mask  = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),100, 255, -1)
cv.imshow("Mask", mask)

frame = cv.bitwise_and(img,img, mask=mask)
cv.imshow("Masked Image", frame)


cv.waitKey(0)