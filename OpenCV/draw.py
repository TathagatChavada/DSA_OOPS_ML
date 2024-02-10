import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
# cv.imshow("Draw", blank)

# blank[:300, :300] = 0,255,0
# cv.imshow("Green", blank)

# Rectangle/Square
# -1 for filling image
cv.rectangle(blank, (20,20), (250,250), (0,255,0), thickness=-1)
# cv.imshow("Rectangle", blank)


# Circle
cv.circle(blank, (250,250), 60, (0,0,255), thickness=-1)

# Line
cv.line(blank, (20,20), (250,250), (255,255,255), thickness=2)

#Text
cv.putText(blank,"Hello World", (150,360), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2)
cv.imshow("Shape", blank)
cv.waitKey(0)