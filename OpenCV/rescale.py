import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")

# cv.imshow("Cat", img)


def rescaleImage(frame, scale = 0.75):
    # Works for Photos, Videos & Live videos
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

# cv.imshow("Resized Cat", rescaleImage(img, scale=0.2))



# Reading Video
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    resize_frame = rescaleImage(frame)
    
    cv.imshow("WebCam",frame)
    cv.imshow("WebCam Resized",resize_frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()    
cv.destroyAllWindows()

cv.waitKey(0)