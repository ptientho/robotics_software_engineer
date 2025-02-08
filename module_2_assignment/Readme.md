# Module 2 Assignment: Developing Custom ROS 2 Nodes and Launch Files

## Objective

This assignment focuses on developing your ability to write custom ROS 2 nodes and utilize launch files for running multiple nodes simultaneously. You will create a custom ROS 2 node that controls the Turtlesim simulation and develop a launch file to run the simulation and node together.

## Tasks

### Task 1: Create a Custom ROS 2 Node

- **Develop a ROS 2 node** that makes the Turtlesim follow a unique pattern:
  - **Circle Movement:** The turtle should move in a circle with a radius that is provided as a user input.
  - **Logarithmic Spiral Movement:** The turtle should move in a logarithmic spiral pattern.

#### Result Task 1
- task 1a and 1b: I create a file named **move.hpp** and **move.cpp** to have both circle movement and logarithmic spiral movement.
- the executable files for circle movement and logarithmic spiral movement are **main1.cpp** and **main2.cpp** respectively.

### Task 2: Develop a Launch File

- **Create a launch file** that starts the Turtlesim simulation and the custom ROS 2 node simultaneously.

- **Ensure proper documentation** of the node and launch file creation process, including the code and the results of executing the tasks.

#### Result Task 2
- task 2a: I create a launch file **move_turtlebot.launch.py** to start robot simulation and the movement (circular/spiral).
To start the launch file,

```
# command robots to move spiral
ros2 launch module_2_assignment move_turtlebot.launch.py is_spiral:=true

# command robots to move cicular (default)
ros2 launch module_2_assignment move_turtlebot.launch.py is_spiral:=false

```

### Task 3: Modify the Turtlesim Simulation Environment

- **Use existing Turtlesim services** such as `spawn` and `clear` to modify the simulation environment:
  - **Spawn 5 Turtlebots** with a single launch file, placing them diagonally from the top left to the bottom right.
  - **Drive the middle 3 turtles** back and forth continuously using ROS 2 services.

#### Result Task 3
- task 3a: I create a launch file **turtlebot_world.launch.py** to start an empty world with 5 turtlebots, placing diagonally
To launch the simulation,

```
ros2 launch module_2_assignment turtlebot_world.launch.py
```

- task 3b: I create a source file **turtle_move_service.cpp** that launch a service node called **move_back_and_forth_server**. This service uses a custom message created within this package called **CmdVel.srv** that requests for multiple robot name (robot_names) to be controlled with.

After launching the world with 5 robots, open a new terminal and run the service node.

```
ros2 run module_2_assignment turtle_move_service
```

Open a new terminal. This one is for calling the service with 3 middle robot names.

```
ros2 service call /cmd_vel_back_and_forth module_2_assignment/srv/CmdVel "{robot_names:['turtlebot2','turtlebot3','turtlebot4']}"
```

### Task 4: Modify Turtle Behavior with Parameters

- **Utilize ROS 2 parameters** to alter the behavior of the turtles:
  - **Change the speed** of the turtles dynamically during the simulation.

#### Result Task 4
- task 4a: I declare a parameter inside the service node called **robot_speed** to adjust robots' speed at runtime.
In this example, set the middle robots' speed (3 robots) to 0.2 m/s.

```
ros2 param set /move_back_and_forth_server robot_speed 0.2
```

### Task 5: Debugging a ROS 2 Node Using a Message Type
`Task Description:`

 Your task is to debug and fix a ROS 2 package that uses an uncommon message type, specifically std_msgs/msg/UInt8MultiArray. The node publishes and subscribes to this message type to simulate controlling the state of a robot's LEDs.

#### Result Task 5
- task 5a: I checked and found that the LED publisher and subscriber are not built within the CMakeLists.txt. Therefore, I added the executables for both of them. I inspected the publisher and subscriber separately in the terminals and they work normally without any bugs.








