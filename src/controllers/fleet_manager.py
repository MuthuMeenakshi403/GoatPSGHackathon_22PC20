from models.robot import Robot

class FleetManager:
    def __init__(self, graph):
        #Initializes the FleetManager, which handles robot operations within a navigation graph.
        self.robots = []
        self.graph = graph

    def spawn_robot(self, start):
        #Creates and adds a new robot at a given starting position.
        robot = Robot(len(self.robots), start, self.graph)
        self.robots.append(robot)

    def assign_task(self, robot_index, destination):
        #Assigns a movement task to a specific robot.
        if 0 <= robot_index < len(self.robots):
            self.robots[robot_index].assign_task(destination)
