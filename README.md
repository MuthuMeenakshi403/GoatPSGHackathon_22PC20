
# Fleet Management System 

The Fleet Management System is a graphical user interface (GUI) application built using Python and Tkinter. It allows users to visualize and manage a fleet of autonomous robots moving within a network graph. The robots navigate between nodes, avoiding obstacles and recalculating paths dynamically.

## Features

- Graph Visualization: Displays a network graph using NetworkX and Matplotlib.
- Robot Management: Allows spawning, selecting, and removing robots.
- Task Assignment: Assigns movement tasks to robots using shortest-path calculations.
- Dynamic Re-routing: Automatically recalculates paths to avoid congestion.

## Installation

To run this project, ensure you have the following dependencies installed:

```bash
pip install tkinter networkx matpl
```

## Run Locally

Clone the project

```bash
git clone https://github.com/MuthuMeenakshi403/GoatPSGHackathon_22PC20.git
```

Go to the project directory

```bash
cd fleet_management_system
```

Go to the src directory

```bash
cd src
```

Now Run

```bash
  python main.py
```

## Usage

- Click on a node to spawn a robot.

- Click on an existing robot to select it.

- Click on another node to assign the robot to move there.

- The robot will follow the shortest path and dynamically reroute if necessary(in case of collision or blockage).

- Check logs for movement updates. In the file named fleet_logs.txt , it has all history of movements of the robot.

## Screenshots

![Screenshot 2025-03-29 153555](https://github.com/user-attachments/assets/20fa48c0-1080-4f35-aed0-3fa148686ce4)

![Screenshot 2025-03-29 153624](https://github.com/user-attachments/assets/c1d99e30-bdf9-4d35-86a6-44df2fd1f3dd)

![Screenshot 2025-03-29 153641](https://github.com/user-attachments/assets/866d8577-8199-43df-b8c1-4f88f085ccd0)

![Screenshot 2025-03-29 153809](https://github.com/user-attachments/assets/16f4883d-e039-4a2b-bf2c-71f23c21b480)

    
    


