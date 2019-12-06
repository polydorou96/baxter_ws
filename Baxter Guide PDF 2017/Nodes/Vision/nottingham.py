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

#callback function for camera subscriber, called by the camera subscriber for every frame.
def callback(data):

    #Republish the camera stream to the screen
    rospy.Publisher('/robot/xdisplay',Image).publish(data)

    #Convert incoming image from a ROS image message to a CV image that open CV can process.
    cv_image = CvBridge().imgmsg_to_cv(data, "bgr8")
    #Display the converted cv image, this is the raw camera feed data.
    cv.ShowImage("Raw Camera Feed", cv_image)

    #Create an empty image variable, the same dimensions as our camera feed.
    gray = cv.CreateImage((cv.GetSize(cv_image)), 8, 1)
    #Into this previously created empty image variable, place the grayscale conversion of our camera feed.
    cv.CvtColor(cv_image,gray,cv.CV_BGR2GRAY)
    #Display the grayscale image.
    cv.ShowImage("Grayscale Conversion", gray)

    #Create another empty image variable.
    canny = cv.CreateImage((cv.GetSize(cv_image)), 8, 1)
    #Fill the new image variable with a canny edge detection map of the greyscale image created earlier.
    cv.Canny(gray, canny, 50, 150, 3)
    #Display the canny mapping.
    cv.ShowImage("Canny Edge Detection", canny)

    #3ms wait, required to refresh display windows
    cv.WaitKey(3)

if __name__ == '__main__':
    rospy.init_node('activerobots_baxter_nottingham_uni_camera_example', anonymous=True)

#create subscriber to the right hand camera, each frame recieved calls the callback function
camera_sub = rospy.Subscriber("/cameras/right_hand_camera/image",Image,callback)

print "ended, now spinning, Ctrl-c to exit"
#prevents program from exiting, allowing subscribers and publishers to keep operating
#in our case that is the camera subscriber and the image processing callback function
rospy.spin()

