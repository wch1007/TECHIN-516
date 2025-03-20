#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose
from .gen3lite_pymoveit2 import Gen3LiteArm, Gen3LiteGripper  

def create_pose(x, y, z, ox, oy, oz, ow):
    """Creates a Pose object."""
    pose = Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z
    pose.orientation.x = ox
    pose.orientation.y = oy
    pose.orientation.z = oz
    pose.orientation.w = ow
    return pose

class TurtleBotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        time.sleep(1)  # Allow publisher to initialize

    def move(self, linear_speed=0.0, angular_speed=0.0, duration=0.0):
        """Publishes velocity commands to move the robot."""
        twist = Twist()
        twist.linear.x = linear_speed
        twist.angular.z = angular_speed
        self.publisher_.publish(twist)
        time.sleep(duration)
        self.stop()

    def stop(self):
        """Stops the robot by publishing zero velocity."""
        twist = Twist()
        self.publisher_.publish(twist)
        time.sleep(1)

    def move_to_pick_place_position(self, distance=3.2, speed=0.2):
        """Moves forward to pick-and-place position."""
        duration = distance / speed
        self.move(speed, 0.0, duration)
        self.get_logger().info("TurtleBot reached pick-and-place position.")

    def move_back_to_start(self, distance=3.2, speed=0.2):
        """Moves backward to return to the original position."""
        duration = distance / speed
        self.move(-speed, 0.0, duration)
        self.get_logger().info("Returned to original position.")

def pick_and_place(arm, gripper, pre_pick_pose, pick_pose, pre_put_pose2, put_pose1):
    """Executes the pick-and-place operation."""
    arm.inverse_kinematic_movement(pre_pick_pose)
    time.sleep(0.5)
    gripper.move_to_position(0.0)
    arm.inverse_kinematic_movement(pick_pose)
    gripper.move_to_position(0.7)
    print("Got the cube")
    time.sleep(0.5)
    arm.inverse_kinematic_movement(pre_put_pose2)
    time.sleep(0.5)
    arm.inverse_kinematic_movement(put_pose1)
    time.sleep(0.5)
    gripper.move_to_position(0.0)
    print("Gripper opened! TurtleBot can now return.")
    time.sleep(1)  # Small delay for stabilization

def main(args=None):
    rclpy.init(args=args)

    # Initialize TurtleBot
    controller = TurtleBotController()

    # Initialize arm and gripper
    arm = Gen3LiteArm()
    gripper = Gen3LiteGripper()

    # Define poses
    pre_pick_pose = create_pose(0.380, -0.030, 0.371, 0.817, 0.574, -0.036, 0.028)
    pick_pose = create_pose(0.384, -0.058, 0.121, 0.751, 0.659, -0.025, 0.017)
    pre_put_pose2 = create_pose(-0.174, -0.002, 0.191, 0.494, 0.867, -0.007, -0.066)
    put_pose1 = create_pose(-0.186, -0.019, -0.312, -0.635, 0.748, 0.027, 0.194)

    # Step 1: Move TurtleBot to pick-and-place position
    controller.move_to_pick_place_position()

    # Step 2: Execute pick-and-place task
    pick_and_place(arm, gripper, pre_pick_pose, pick_pose, pre_put_pose2, put_pose1)

    # Step 3: Move TurtleBot back to the original position
    controller.move_back_to_start()

    # Cleanup
    controller.destroy_node()
    print("Returned to original position.")

    # Shutdown ROS 2
    rclpy.shutdown()
    gripper.shutdown()
    arm.shutdown()

if __name__ == '__main__':
    main()

