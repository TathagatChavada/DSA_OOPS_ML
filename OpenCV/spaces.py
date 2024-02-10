import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# Gray scale images shows the distribution of pixel intensities at a particular location
gray_scale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale image",gray_scale_image)


# BGR -> HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV image",hsv_img)

cv.waitKey(0)