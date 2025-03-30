import random

class Robot:
    def __init__(self, robot_id, start_position):
        #Initializes a robot with a unique ID, starting position, and a random color.
        self.robot_id = robot_id
        self.position = start_position
        self.target = None
        self.status = "waiting"
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def move_to(self, target):
        #Assigns a target position to the robot and updates its status to 'moving'.
        self.target = target
        self.status = "moving"

    def update_status(self, new_status):
        #Updates the status of the robot.
        self.status = new_status
