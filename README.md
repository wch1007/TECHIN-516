# TECHIN-516 Project Chenghao

## Overview
This project involves **Kinova**, **TurtleBot**, and **ROS 2 command launch**.

## Features
- ✅ **Kinova Gen3 Lite Integration**
- ✅ **TurtleBot 3 Control**
- ✅ **ROS 2 Fast DDS Discovery**
- ✅ **Command Launch Configurations**
- ✅ **Trajectory Execution with `trajectory_from_csv.py`**

## Notes
- **Revision history will be tracked.**
- The main execution script is: **`trajectory_from_csv.py`**.

## **System Information**
| **Device**      | **IP Address**  |
|---------------|----------------|
| **Arm**       | `10.18.2.240`   |
| **TurtleBot** | `10.18.3.94`    |
| **Laptop**    | `10.19.159.77`  |

### **Login Credentials**
```
Username: ubuntu
Password: robot1234
```

---

## **Command Line Instructions**

### **Fast DDS Discovery Server**
```bash
fastdds discovery --server-id 0
```

---

### **Kinova Gen3 Lite Setup**
```bash
ros2 launch kortex_bringup gen3_lite.launch.py \
robot_ip:=10.18.2.240 launch_rviz:=false

ros2 launch kortex_bringup gen3_lite.launch.py \
robot_ip:=10.18.2.239 launch_rviz:=false
```

---

### **Kinova MoveIt Configuration**
```bash
ros2 launch kinova_gen3_lite_moveit_config robot.launch.py \
robot_ip:=10.18.2.240

ros2 launch kinova_gen3_lite_moveit_config robot.launch.py \
robot_ip:=10.18.2.239
```

---

### **Building & SSH Access**
```bash
colcon build --packages-select lab_quaternion --symlink-install

ssh ubuntu@10.18.3.92
```

---

### **ROS 2 Discovery Server Setup**
```bash
export ROS_DISCOVERY_SERVER=10.19.159.77:11811

echo $ROS_DISCOVERY_SERVER

fastdds discovery --server-id 0
```

---

### **TurtleBot 3 Setup**
```bash
ros2 launch turtlebot3_bringup robot.launch.py
```

---

### **TurtleBot 3 Teleoperation**
```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

---

## **Execution Steps**
1. **Start Fast DDS Discovery Server** on **all devices**:
   ```bash
   fastdds discovery --server-id 0
   ```

2. **Launch Kinova Gen3 Lite:**
   - **For Arm 10.18.2.240**
     ```bash
     ros2 launch kortex_bringup gen3_lite.launch.py \
     robot_ip:=10.18.2.240 launch_rviz:=false
     ```

3. **Launch MoveIt Configuration:**
   ```bash
   ros2 launch kinova_gen3_lite_moveit_config robot.launch.py \
   robot_ip:=10.18.2.240
   ```

4. **Build and Deploy the Package:**
   ```bash
   colcon build --packages-select lab_quaternion --symlink-install
   ```

5. **Launch TurtleBot 3:**
   ```bash
   ros2 launch turtlebot3_bringup robot.launch.py
   ```

6. **Run Trajectory Execution (`trajectory_from_csv.py`):**
   ```bash
   ros2 run lab_quaternion trajectory_from_csv
   ```

---

## **Troubleshooting**
### **1. If TurtleBot 3 doesn't move**
Check if `/cmd_vel` is receiving commands:
```bash
ros2 topic echo /cmd_vel
```

### **2. If Kinova Arm is not responding**
Check running ROS 2 nodes:
```bash
ros2 node list
```
If `gen3_lite_arm` is missing, restart the Kinova launch.

### **3. If ROS 2 Discovery Server is not working**
Verify the discovery server:
```bash
echo $ROS_DISCOVERY_SERVER
```
Restart if necessary:
```bash
fastdds discovery --server-id 0
```


