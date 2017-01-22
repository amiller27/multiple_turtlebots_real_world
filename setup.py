#!/usr/bin/env python

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

rospy.init_node('patrol', anonymous=True)

clients = []
def add_client():
    client = actionlib.SimpleActionClient('/robot_%i/move_base'%(len(clients)), MoveBaseAction)
    client.wait_for_server()
    clients.append(client)

def add_clients(n):
    for i in range(n): add_client()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = '/map'
goal.target_pose.pose.orientation.w = 1

def execute(goal, n):
    clients[n].send_goal(goal)
    print clients[n].wait_for_result(rospy.Duration(30))
