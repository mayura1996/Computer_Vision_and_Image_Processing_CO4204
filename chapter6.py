import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')






# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal", imgHor) #horizontal stack
# cv2.imshow("Verticle",imgVer) #verticle stack


cv2.waitKey(0)