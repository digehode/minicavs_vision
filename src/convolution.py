import cv2
import numpy as np
import sys

image = cv2.imread('images/parked_small.jpg')

if image is None:
    print('Could not read image')
    sys.exit()
    
# Create the kernel
kernel = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])


# Apply it to the image to create a new image
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)


#Display Images
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)


#Wait for a key and exit
cv2.waitKey()
cv2.destroyAllWindows()

