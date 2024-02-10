import cv2 as cv

def rescale_Frame(frame, scale = 0.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_res(width, height):
    # For Live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture("Videos/dog.mp4")

# while True:
#     isTrue, frame = capture.read()
    
#     resized_frame = rescale_Frame(frame)

#     cv.imshow("Video", frame)
#     cv.imshow("Resized Video", resized_frame)



#     if cv.waitKey(20) & 0xFF == ord("x"):
#         break

# capture.release()
# cv.destroyAllWindows()

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)
cv.imshow("Resized Cat", rescale_Frame(img))
cv.waitKey(0)