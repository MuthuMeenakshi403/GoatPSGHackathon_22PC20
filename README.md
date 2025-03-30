
# Fleet Management System 

The Fleet Management System is a Tkinter-based GUI application for managing a fleet of robots in a networked environment. The application uses NetworkX for graph representation and Matplotlib for visualization. Robots can be spawned, assigned tasks, and will navigate to their destinations using the shortest available paths while avoiding blockages.

## Features

- Graph Visualization: Displays the network of nodes and edges where robots operate.
- Robot Spawning: Robots can be added to any node in the network.
- Task Assignment: Assign tasks to robots to move from one node to another.
- Path Planning: Uses Dijkstra's algorithm to compute the shortest path.
- Obstacle Handling: Robots wait or re-route in case of blockages.
- Logging System: Logs robot movements and events in a file.

## Installation

To run this project, ensure you have the following dependencies installed:

```bash
pip install networkx matplotlib
```

## Run Locally

Clone the project

```bash
git clone https://github.com/MuthuMeenakshi403/GoatPSGHackathon_22PC20.git
```

Navigate to the project directory

```bash
cd fleet_management_system
```

Navigate to the src directory

```bash
cd src
```

Now Run

```bash
python main.py
```

## How it works

- Graph Loading:
    - The graph is loaded from a JSON file (e.g., nav_graph_1.json).
    - Nodes represent locations, and edges represent paths.
    - Positions are determined using nx.spring_layout().

- Robot Spawning:
    - Click on a node to spawn a robot at that location.
    - The robot gets a unique ID (e.g., Robot 1).

- Task Assignment:
    - Click on an existing robot to select it.
    - Click on another node to assign the robot a destination.
    - The system computes the shortest path and animates movement.

- Movement Handling:
    - Robots follow the shortest available path.
    - If a path is blocked, an alternative route is chosen.
    - If no alternate path exists, the robot waits.

- Logging:
    - Events such as robot movements, rerouting, and task completion are logged in logs/fleet_logs.txt.

## Screenshots
- Click on a node to spawn a robot.
    - ![Screenshot 2025-03-29 153555](https://github.com/user-attachments/assets/20fa48c0-1080-4f35-aed0-3fa148686ce4)

- Click on an existing robot to select it and assign the robot to move to particular destination. On reaching destination pop window is displayed.
    - ![Screenshot 2025-03-29 153624](https://github.com/user-attachments/assets/c1d99e30-bdf9-4d35-86a6-44df2fd1f3dd)

- The robot will follow the shortest path and wait if there is blockage of some other robots inbetween and dynamically reroute if necessary.
    - ![Screenshot 2025-03-29 153641](https://github.com/user-attachments/assets/866d8577-8199-43df-b8c1-4f88f085ccd0)

- The dynamic movements of robots are written to fleet_logs.txt file.
    - ![Screenshot 2025-03-29 153809](https://github.com/user-attachments/assets/16f4883d-e039-4a2b-bf2c-71f23c21b480)
 

    
    


