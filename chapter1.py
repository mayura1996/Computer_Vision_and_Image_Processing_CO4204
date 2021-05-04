import cv2
print("Package Imported")

#read image
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#read from webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(3,480)
cap.set(10,100) #change brightness
while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

