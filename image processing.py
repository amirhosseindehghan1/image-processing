import cv2

# Set value (0 show the image balck and white, 1 show the image colory)
img = cv2.imread('ubuntu.jpg',0)

# Show the image, but very fast
cv2.imshow('amirhossein', img)

# Show the image with time (1000ms = 1sec)- if set (0) show the image non-stop
# with any key in keyboard the window will be close
k = cv2.waitKey(0)

if k == ord('s'):
    cv2.imwrite('newpic.jpg', img)
    cv2.destroyAllWindows()