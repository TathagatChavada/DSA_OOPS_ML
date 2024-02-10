import cv2 as cv
import numpy as np

# Translation an image
def translate(img, x, y):
    translation_matrix = np.float32(([1,0,x], [0,1,y]))
    dimensions = (img.shape[1],img.shape[0])

    return cv.warpAffine(img, translation_matrix, dimensions)
    

# Rotate an image
# img.shape returns a tuple representing the dimensions of the array. 
# 1st element is the height,
# 2nd element is the width, and 
# if it's a color image, the third element might represent the number of color channels.

def rotate(img, angle, rotation_point = None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle,1)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)



img = cv.imread("Photos/park.jpg")
# cv.imshow("Translated Park image", translate(img, 100, 100))
# cv.imshow("Rotated Park image", rotate(img, 90))


# Resize an image
resized_image = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
cv.imshow("Resized image", resized_image)


# Flipping an image
flipped_image = cv.flip(img,-1)
cv.imshow("Flipped image", flipped_image)

cv.waitKey(0)