from jetcam.csi_camera import CSICamera
import cv2

WIDTH = 224
HEIGHT = 224

camera = CSICamera(width=WIDTH, height=HEIGHT)

image = camera.read()

cv2.imwrite("test2.jpg", image)
cv2.namedWindow("Taken image")
cv2.imshow("Taken image", image)
cv2.waitKey(0)
