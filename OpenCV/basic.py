import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

# # 1. Converting to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscle Image", gray)


# 2. Blur
# There are many ways to do blurs in OpenCV, here we used GaussianBlur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blurred Image", blur)


# 3. Edge Cascade
# If we want to reduce the no. of edges then we will pass 'blur' insteat of 'img'
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Edges", canny)


# 4. Dilate the image
# dilated = cv.dilate(canny, (7,7), iterations= 3)
# cv.imshow("Dialted Image", dilated)


# 4. Eroding the image back to Edge cascade
# erode = cv.erode(dilated, (7,7), iterations= 3)
# cv.imshow("Eroded Image", erode)


# 5. Resizing the image
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Image", resized) 


# 6. Cropped Image
# The first value in slicing defines the height(Rows) and the other one is for width(columns)
cropped = img[50:200, 150:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)