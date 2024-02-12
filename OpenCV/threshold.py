import cv2 as cv

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)


gray_scale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray scale image", gray_scale_image)

threshold, thresh = cv.threshold(gray_scale_image, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Image", thresh) 

threshold, thresh_inv = cv.threshold(gray_scale_image, 125, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Threshold Image Inverse", thresh_inv) 


# Adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(gray_scale_image, 255,
cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow("Adaptive threshold image", adaptive_threshold) 

cv.waitKey(0)