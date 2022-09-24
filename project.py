import cv2
import numpy as np


img = np.zeros((512,512,3))

img = cv2.circle(img, (256,256), 100, (0,255,0), -1)
img = cv2.line(img, (0,0), (511,511), (255,0,0), 3)
img = cv2.rectangle(img, (20,20), (150,150), (0,0,255), -1)
img = cv2.ellipse(img, (250,250), (100,50), 0,45, 340, (0,0,255), -1)

cv2.imshow('frame', img)
cv2.waitKey(0)