# TurtleBot3 Controller — Yıldız Rover Ödev 4

A ROS 2 Python package (`turtlebot3_controller`) for controlling a TurtleBot3 robot. Developed as Assignment 4 for the Yıldız Rover team.

---

## Requirements

- ROS 2 (Humble or later recommended)
- Python 3
- `rclpy`
- `geometry_msgs`
- `nav_msgs`
- TurtleBot3 packages installed and configured

---

## Package Structure

```
yildiz-rover-odev-4/
├── turtlebot3_controller/
│   └── turtlebot3_move.py   # Main controller node
├── resource/
│   └── turtlebot3_controller
├── test/                    # Linting and unit tests
├── package.xml
├── setup.cfg
└── setup.py
```

---

## Installation

Clone the repository into your ROS 2 workspace and build it:

```bash
cd ~/ros2_ws/src
git clone https://github.com/TariWind/yildiz-rover-odev-4.git
cd ~/ros2_ws
colcon build --packages-select turtlebot3_controller
source install/setup.bash
```

---

## Usage

Run the controller node:

```bash
ros2 run turtlebot3_controller turtlebot_controller
```

Make sure your TurtleBot3 simulation (e.g., Gazebo) or physical robot is already running before launching the node.

---

## Topics

| Topic | Type | Description |
|---|---|---|
| `cmd_vel` (published) | `geometry_msgs/Twist` | Velocity commands sent to the robot |
| `odom` (subscribed) | `nav_msgs/Odometry` | Odometry feedback from the robot |

> Exact topic names may vary — refer to `turtlebot3_move.py` for the full list.

---

## Running Tests

```bash
cd ~/ros2_ws
colcon test --packages-select turtlebot3_controller
colcon test-result --verbose
```

Tests use `pytest` and ROS 2 linting tools (`ament_flake8`, `ament_pep257`, `ament_copyright`).

---

## Dependencies

Declared in `package.xml`:

- `rclpy` — ROS 2 Python client library
- `geometry_msgs` — Velocity and pose message types
- `nav_msgs` — Odometry message types

---

## Maintainer

**tari** — Yıldız Rover Team

---

## License

To be declared.
