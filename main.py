import cv2
cool_photo = cv2.imread('cool_photo.jpg')
cv2.imshow('new_photo', cool_photo)
cv2.waitKey(0)
cv2.destroyAllWindows()