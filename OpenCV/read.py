import cv2 as cv

# Reading Image
# img = cv.imread("Photos/cat.jpg")

# cv.imshow("Cat", img)
# cv.waitKey(0)


# Reading Video
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    cv.imshow("WebCam",frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()    
cv.destroyAllWindows()
