import cv2

img = cv2.imread('image.jpg')
cv2.imshow('Show Images',img)
cv2.waitKey()
cv2.destroyAllWindows() 