#!/usr/bin/env python

"""
Active Robots, Assisting Nottinghan University
Camera Subscriber Example
Copyright 2014 Active Robots Ltd, for Educational Use Only
"""

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv
import cv2
import numpy as np

#callback function for camera subscriber, called by the camera subscriber for every frame.
def callback(data):

    #Republish the camera stream to the screen
    rospy.Publisher('/robot/xdisplay',Image).publish(data)

    #Convert incoming image from a ROS image message to a CV image that open CV can process.
    cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    #Display the converted cv image, this is the raw camera feed data.
    cv2.imshow("Raw Camera Feed", cv_image)

    #Into this previously created empty image variable, place the grayscale conversion of our camera feed.
    gray1 = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    #Display the grayscale image.
    cv2.imshow("Grayscale Conversion", gray1)

    #Fill the new image variable with a canny edge detection map of the greyscale image created earlier.
    canny1 = cv2.Canny(gray1, 50, 150)
    #Display the canny mapping.
    cv2.imshow("Canny Edge Detection", canny1)

    #3ms wait, required to refresh display windows
    cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('activerobots_baxter_nottingham_uni_camera_example', anonymous=True)

#create subscriber to the right hand camera, each frame recieved calls the callback function
camera_sub = rospy.Subscriber("/cameras/right_hand_camera/image",Image,callback)

print "ended, now spinning, Ctrl-c to exit"
#prevents program from exiting, allowing subscribers and publishers to keep operating
#in our case that is the camera subscriber and the image processing callback function
rospy.spin()

