import cv2

img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #greyscaling
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imageCanny = cv2.Canny(img,150,200)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imageCanny)


cv2.waitKey(0)