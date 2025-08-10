import Jetson.GPIO as GPIO
import time
import datetime
from jetcam.csi_camera import CSICamera
import cv2
import os

# Pin definitions
input_pin = 12

# Create camera object
WIDTH = 720
HEIGHT = 720

img_path = "/home/wildlife/Desktop/FinalImplementation/Images"
camera = CSICamera(width=WIDTH, height=HEIGHT)

def obtainImage():
    prev_value = None

    # Pin setup
    # board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)

    # setup input and output pins
    GPIO.setup(input_pin, GPIO.IN)

    try:
        while True:
            #read the input pin
            value = GPIO.input(input_pin)

            if value == GPIO.LOW:
                value_str = "LOW"
       	        print("No Motion detected")
       	    elif value == GPIO.HIGH:
                print("Motion detected")
                value_str = "HIGH"
                print("Taking photo")
                image = camera.read()
                day = str(datetime.datetime.now())
                #cv2.imwrite("/Images/"+day+".jpeg", image)
                cv2.imwrite(os.path.join(img_path, day + ".jpeg"), image)
                #cv2.namedWindow("Taken image")
                #cv2.imshow("Taken image", image)
                #cv2.waitKey(0)
                break
            time.sleep(1)

    finally: 
        return image              
        GPIO.cleanup()

if __name__ == '__main__':
    obtainImage()



