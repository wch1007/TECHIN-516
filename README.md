# TECHIN-516 Project Chenghao
## Overview
This project involves Kinova, Turtlebot, and command launch.
## Features
- Kinova integration
- Turtlebot control
- Command launch configurations
## Notes
Revision history will be tracked.
trajectory_from_csv.py is the main code.
## Steps to Initiate
Arm 10.18.2.240
Turtlebot 10.18.3.94
Username: ubuntu
Password: robot1234
Laptop IP  10.19.159.77

Command Line Bash:
''' bash
fastdds discovery --server-id 0
'''



ros2 launch kortex_bringup gen3_lite.launch.py \
robot_ip:=10.18.2.240
launch_rviz:=false

ros2 launch kortex_bringup gen3_lite.launch.py \
robot_ip:=10.18.2.239
launch_rviz:=false

ros2 launch kinova_gen3_lite_moveit_config robot.launch.py \
robot_ip:=10.18.2.240

ros2 launch kinova_gen3_lite_moveit_config robot.launch.py \
robot_ip:=10.18.2.239

colcon build --packages-select lab_quaternion --symlink-install

ssh ubuntu@10.18.3.92

export ROS_DISCOVERY_SERVER=10.19.159.77:11811

echo $ROS_DISCOVERY_SERVER

fastdds discovery --server-id 0


ros2 launch turtlebot3_bringup robot.launch.py


ros2 run turtlebot3_teleop teleop_keyboard
