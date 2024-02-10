import cv2 as cv

img = cv.imread("Photos/park.jpg")
# cv.imshow("Park", img)


# grayscale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Scale Image", grayscale_image)


# blurred_img = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blurred Image", blurred_img)

# Edge Cascade
# canny = cv.Canny(blurred_img, 125,175)
# cv.imshow("Canny Image", canny)


# # Dilating the image
# dilated_image = cv.dilate(canny,(7,7), iterations=3)
# cv.imshow("Dilated Image", dilated_image)


# # Eroded image
# # Erode back to edge cascade
# eroded_img = cv.erode(dilated_image, (7,7), iterations=3)
# cv.imshow("Eroded Image", eroded_img)


# Resize image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized Image", resize)

cropped_image = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped_image)

cv.waitKey(0)