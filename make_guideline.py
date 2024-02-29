import numpy as np
import cv2

image = np.ones((1188,840),dtype=np.uint8)*255

image[393:396]=np.zeros((3,840),dtype=np.uint8)
image[787:790]=np.zeros((3,840),dtype=np.uint8)

for i in range(len(image)):
    image[i][418:421]=np.zeros((1,3),dtype=np.uint8)

cv2.imshow('image',image)
cv2.imwrite(f'guideline.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()