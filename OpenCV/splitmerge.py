import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

b, g, r = cv.split(img)

cv.imshow("Blue Park", b)
cv.imshow("Green Park", g)
cv.imshow("Red Park", r)


merged_image = cv.merge((b,g,r))
cv.imshow("Merged Park", merged_image)

cv.waitKey(0)
