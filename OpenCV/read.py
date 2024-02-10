import cv2 as cv

# Reading Photos
# img = cv.imread("Photos/cat_large.jpg")

# cv.imshow("Cat", img)

# Reading Videos
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    gray_scale_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred_image = cv.GaussianBlur(gray_scale_image, (5,5), cv.BORDER_DEFAULT)
    canny = cv.Canny(blurred_image, 125, 175)


    cv.imshow("WebCam", canny)

    cv.waitKey(1) 
        

# capture.release()
# cv.destroyAllWindows()