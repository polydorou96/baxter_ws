#!/usr/bin/python  

# This script shows a basic example of how to get Baxter to use the inverse kinematics solver to get a joint position from coordinates and an orientation and how to get the right arm to move to them.

import baxter_interface
import baxter_external_devices
import rospy
import ik_solver
import math
from geometry_msgs.msg import (    
    Point,
    Quaternion,
)

# Euler angles to quaternion coordinates function
def conversion(a,b,d):
	ca = math.cos(a/2)
	cb = math.cos(b/2)
	cd = math.cos(d/2)
	sa = math.sin(a/2)
	sb = math.sin(b/2)
	sd = math.sin(d/2)

	w = (ca*cb*cd)-(sa*sb*sd)
	x = (sa*sb*cd)+(ca*cb*sd)
	y = (sa*cb*cd)+(ca*sb*sd)
	z = (ca*sb*cd)-(sa*cb*sd)

	return Quaternion(w, x, y, z)

# Function moves Baxter's left arm to the specified position and orientation
def moveTo(goal, ash):
	loc = goal
	orient = ash
	#print "loc: ", loc    
	#print "orient: ", orient[1]
	limb_joints = ik_solver.ik_solve('right', loc, orient)
	prev = loc, orient
	if limb_joints != -1:
	    #print "limb_joints: ", limb_joints
	    #print "moving arm to goal limb_joints joints"
	    print "  "
	    print "  "
	    print "  "
	    right.move_to_joint_positions(limb_joints)

rospy.init_node('move_right_hand')
rs = baxter_interface.RobotEnable()
rs.enable()

right = baxter_interface.Limb('right')
rightGripper = baxter_interface.Gripper('right')
pose = right.endpoint_pose()
b = True
pos = pose.popitem()
orient = pose.popitem()
prev = pos[1]

right.set_joint_position_speed(1.0)

print "-----------------------------------"
pose = right.endpoint_pose()
print "current pose: ", pose
s = raw_input("Press q to run ... ")
if s == 'q':

# Movement function called here, variables can be changed
	moveTo(Point(0.57,-0.18,0.23), conversion(0,0,-0.78))

