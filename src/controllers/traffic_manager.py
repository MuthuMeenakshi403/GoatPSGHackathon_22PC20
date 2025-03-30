import threading

class TrafficManager:
    def __init__(self):
        #Initializes the TrafficManager, which handles lane occupancy to prevent collisions.
        self.lock = threading.Lock()
        self.occupied_lanes = set()

    def request_lane(self, lane):
        #Attempts to acquire a lane for a robot.
        with self.lock:
            if lane in self.occupied_lanes:
                return False
            self.occupied_lanes.add(lane)
            return True

    def release_lane(self, lane):
        #Releases a previously occupied lane, making it available for other robots.
        with self.lock:
            self.occupied_lanes.discard(lane)
