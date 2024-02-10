import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)


bitwiseAnd = cv.bitwise_and(rectangle,circle)
# cv.imshow("AND", bitwiseAnd)


bitwiseOr= cv.bitwise_or(rectangle,circle)
# cv.imshow("OR", bitwiseOr)

bitwiseXor = cv.bitwise_xor(rectangle,circle)
# cv.imshow("XOR", bitwiseXor)



cv.waitKey(0)