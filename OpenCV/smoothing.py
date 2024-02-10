import cv2 as cv

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)


# Averaging
# High kernel size more blur
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)


gaussian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gaussian_blur)


median_blur = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median_blur)

bilateral_blur = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral Blur", bilateral_blur)


cv.waitKey(0)