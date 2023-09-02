import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Drawing Shapes", blank)

# # 1. Paint the image to the certain color
# blank[1:3, 1:400] = 0,255,0
# cv.imshow("Painted Image", blank)

# 2. Drawing a rectangle
# Instead of thickness=-1 you can also use cv.FILLED
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=-1) 
# cv.imshow("Rectangle", blank)


# 3. Drawing a circle
# cv.circle(blank, (250, 250), (100), (0, 255, 0), thickness=-1)
# cv.imshow("Circle", blank)


# 4. Drawing a line
# cv.line(blank, (25, 25), (200, 25), (0, 255, 0), thickness=2)
# cv.imshow("Line", blank)


# 5. Putting text
cv.putText(blank, "My Name is Tathagat", (50, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 1)
cv.imshow("Text", blank)
cv.waitKey(0)