import cv2

test_cam=cv2.VideoCapture(0)

#camera warm up
for i in range(10):
    test_cam.read()
    

chk,frame=test_cam.read()
cv2.imwrite("testimage.jpeg", frame)
test_cam.release()