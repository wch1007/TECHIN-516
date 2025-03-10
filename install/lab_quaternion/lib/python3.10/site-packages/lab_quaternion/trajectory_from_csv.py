#!/usr/bin/env python3
import time
import rclpy
from geometry_msgs.msg import Pose, Point, Quaternion
from pyquaternion import Quaternion as PyQuaternion
from .gen3lite_pymoveit2 import Gen3LiteArm, Gen3LiteGripper
import numpy as np


cube_pick_data = np.loadtxt('lab8_pick_data.csv', delimiter=',')
def slerp(data, qStart, qEnd, arm):
    qList = []
    for q in PyQuaternion.intermediates(qStart, qEnd, len(data)-2,
include_endpoints=True):
        qList.append(q.elements)
    for i in range(len(data)):
        pose = Pose()
        pose.position.x = data[i][0]
        pose.position.y = data[i][1]
        pose.position.z = data[i][2]
        pose.orientation.x = qList[i][0]
        pose.orientation.y = qList[i][1]
        pose.orientation.z = qList[i][2]
        pose.orientation.w = qList[i][3]
        arm.inverse_kinematic_movement(pose)
        print(f"Reached control point {i}")


def pick_and_place(pick_data, arm, gripper, qStart, qPick):
    gripper.move_to_position(0.0)
    pose1 = Pose()
    pose1.position.x = 0.39
    pose1.position.y = -0.029
    pose1.position.z = 0.36
    pose1.orientation.x = 1.000
    pose1.orientation.y = -0.015
    pose1.orientation.z = 0.020
    pose1.orientation.w = -0.005
    arm.inverse_kinematic_movement(pose1)
    time.sleep(0.5)
    pose2 = Pose()
    pose2.position.x = 0.398
    pose2.position.y = -0.027
    pose2.position.z = 0.16
    pose2.orientation.x = 1.000
    pose2.orientation.y = -0.015
    pose2.orientation.z = 0.020
    pose2.orientation.w = -0.005
    arm.inverse_kinematic_movement(pose2)
    time.sleep(0.5)
    print("Got to pick position")
    gripper.move_to_position(0.5)
    time.sleep(0.5)
    pre_put_pose = Pose()
    pre_put_pose.position.x = 0.387
    pre_put_pose.position.y = -0.030
    pre_put_pose.position.z = 0.445
    pre_put_pose.orientation.x = 1.000
    pre_put_pose.orientation.y = -0.015
    pre_put_pose.orientation.z = 0.020
    pre_put_pose.orientation.w = -0.006
    arm.inverse_kinematic_movement(pre_put_pose)
    time.sleep(0.5)
    put_pose = Pose()
    put_pose.position.x = 0.399
    put_pose.position.y = 0.263
    put_pose.position.z = 0.374
    put_pose.orientation.x = 1.000
    put_pose.orientation.y = -0.016
    put_pose.orientation.z = 0.020
    put_pose.orientation.w = -0.005
    arm.inverse_kinematic_movement(put_pose)
    time.sleep(0.5)
    pose3 = Pose()
    pose3.position.x = 0.408
    pose3.position.y = 0.265
    pose3.position.z = 0.150
    pose3.orientation.x = 1.000
    pose3.orientation.y = -0.015
    pose3.orientation.z = 0.020
    pose3.orientation.w = -0.005
    arm.inverse_kinematic_movement(pose3)
    
    print("Got to put position")
    gripper.move_to_position(0.0)

def main():
    rclpy.init()
    arm = Gen3LiteArm()
    gripper = Gen3LiteGripper()
    qStartCube = PyQuaternion(array=np.array([0.703,0.706,0.022,-0.079]))
    qPickCube = PyQuaternion(array=np.array([1.000, -0.015, 0.020, -0.005]))
    pick_and_place(cube_pick_data, arm, gripper,
qStartCube, qPickCube)
    rclpy.shutdown()
    gripper.shutdown()
    arm.shutdown()

if __name__ == '__main__':
    main()
