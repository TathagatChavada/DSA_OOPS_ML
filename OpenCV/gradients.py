import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
# cv.imshow("Cats", img)


gray_scale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image", gray_scale_image)

# Laplacian
lap = cv.Laplacian(gray_scale_image, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian Edges", lap)


# Sobel 
sobelx = cv.Sobel(gray_scale_image, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray_scale_image, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)


cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)



cv.waitKey(0)
