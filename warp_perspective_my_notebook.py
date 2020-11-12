import cv2
import numpy as np

img = cv2.imread("C://Users//NELSON JOSEPH//Desktop//note_book.jpeg")

width,height = 210,297
pts1 = np.float32([[123,250],[500,240],[559,717],[24,720]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("image", img)
cv2.imshow("output",output)
cv2.waitKey(0)
