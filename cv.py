import cv2

img = cv2.imread('ubuntu.jpg')
img[:,:,0] = 255
# b,g,r = cv2.split(img)
# img = cv2.merge((g,r,b))
# print(img[100,100])
# img[100:130,100:130] = img[900:930,900:930]
# print(img.shape)
#
# v = img.shape[0]
# h = img.shape[1]
# print(v)
# print(h)

cv2.imshow('f1', img)
# cv2.imshow('f2', b)
# cv2.imshow('f3', g)
# cv2.imshow('f4', r)

cv2.waitKey(0)

cv2.destroyAllWindows()