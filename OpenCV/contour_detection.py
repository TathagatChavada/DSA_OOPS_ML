import cv2 as cv

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)

gray_scale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image", gray_scale_image)

# 1st method of finding contours
# blurred_image = cv.GaussianBlur(gray_scale_image, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blurred Image", blurred_image)


# canny = cv.Canny(blurred_image, 125, 175)
# cv.imshow("Canny Edges", canny)

# 2nd method of finding contours
# Thresholding - take an image and contvert it into binary form
ret, thresh = cv.threshold(gray_scale_image, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Image", thresh) 


# contours - returns list of countours from structuring element
# cv.RETER_LIST - returns list of all contours
# cv.CHAIN_APPROX_SIMPLE - returns all point compressed into two end points only
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print("Size of Contours", len(contours))


cv.waitKey(0)