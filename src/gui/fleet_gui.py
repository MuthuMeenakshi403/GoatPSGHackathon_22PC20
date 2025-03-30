import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import time
import threading
import json

class FleetGUI:
    #Initialize the Fleet Management GUI with the given graph.
    def __init__(self, graph):
        self.graph = graph
        self.robots = {}
        self.robot_positions = {}
        self.robot_paths = {}
        self.robot_statuses = {}
        self.selected_robot = None
        self.log_file = "logs/fleet_logs.txt"
        
        # Set up node positions for visualization
        self.pos = nx.spring_layout(self.graph)
        
        # Initialize Tkinter GUI window
        self.root = tk.Tk()
        self.root.title("Fleet Management System")
        self.root.geometry("1200x800")
        
        # Create a Matplotlib figure for visualization
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()
        
        # Status label to display messages
        self.status_label = tk.Label(self.root, text="Status: Idle", font=("Arial", 14))
        self.status_label.pack()
        
        # Log window to display messages
        self.logs_text = tk.Text(self.root, height=10, state='disabled')
        self.logs_text.pack()
        
        # Draw the initial graph
        self.draw_graph()
        self.canvas.mpl_connect("button_press_event", self.on_click)
        
        # Start the GUI loop
        self.run()
    
    def draw_graph(self):
        #Draw the network graph and update the visualization.
        self.ax.clear()
        nx.draw(self.graph, self.pos, ax=self.ax, with_labels=True, node_color='lightblue', edge_color='gray')
        
        # Display robot positions
        for robot, node in self.robot_positions.items():
            self.ax.text(self.pos[node][0], self.pos[node][1], f"{robot}", fontsize=12, color='red', ha='center')
        
        # Highlight assigned paths
        for robot, path in self.robot_paths.items():
            edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=edges, ax=self.ax, edge_color='green', width=2)
        
        self.canvas.draw()
    
    def log(self, message):
        #Log events and display them in the GUI.
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")
        print(message)
        self.status_label.config(text=f"Status: {message}")
        
        # Update log display
        self.logs_text.config(state='normal')
        self.logs_text.insert(tk.END, message + "\n")
        self.logs_text.config(state='disabled')
    
    def on_click(self, event):
        #Handle mouse click events for selecting or assigning robots.
        if event.xdata is None or event.ydata is None:
            return
        
        # Find the closest node to the clicked position
        closest_node = min(self.graph.nodes, key=lambda n: (event.xdata - self.pos[n][0])**2 + (event.ydata - self.pos[n][1])**2)
        
        if self.selected_robot is not None:
            self.assign_task(self.selected_robot, closest_node)
            self.selected_robot = None
        else:
            self.select_or_spawn_robot(closest_node)
    
    def select_or_spawn_robot(self, node):
        #Select a robot if present, or spawn a new one.
        for robot, pos in self.robot_positions.items():
            if pos == node:
                self.selected_robot = robot
                self.log(f"{robot} selected for task assignment")
                return
        
        self.spawn_robot(node)
    
    def spawn_robot(self, node):
        #Spawn a new robot at the given node if it's not already occupied.
        if node in self.robot_positions.values():
            messagebox.showwarning("Warning", "A robot is already at this node!")
            return
        
        robot_id = len(self.robot_positions) + 1
        robot_name = f"Robot {robot_id}"
        self.robot_positions[robot_name] = node
        self.robot_statuses[robot_name] = "Idle"
        self.log(f"{robot_name} spawned at node {node}")
        self.draw_graph()
    
    def assign_task(self, robot, destination):
        #Assign a movement task to a selected robot.
        if destination == self.robot_positions[robot]:
            messagebox.showwarning("Warning", "Robot is already at the destination!")
            return
        
        try:
            path = nx.shortest_path(self.graph, self.robot_positions[robot], destination)
            self.robot_paths[robot] = path
            self.robot_statuses[robot] = "Moving"
            self.log(f"{robot} assigned task to move from {self.robot_positions[robot]} to {destination}")
            threading.Thread(target=self.move_robot, args=(robot, destination)).start()
        except nx.NetworkXNoPath:
            messagebox.showerror("Error", "No valid path found!")
    
    def move_robot(self, robot, destination):
        #Move a robot along its assigned path, handling obstacles.
        path = self.robot_paths[robot]
        
        for node in path:
            while any(pos == node and r != robot for r, pos in self.robot_positions.items()):
                alternative_path = self.find_alternate_path(robot, destination)
                if alternative_path:
                    self.robot_paths[robot] = alternative_path
                    path = alternative_path
                    self.log(f"{robot} rerouted to avoid blockage and is taking a different path")
                    self.draw_graph()
                    break
                else:
                    self.log(f"{robot} waiting at {self.robot_positions[robot]} due to blockage")
                    time.sleep(2)
                    continue
            
            if any(pos == node and r != robot for r, pos in self.robot_positions.items()):
                continue
            
            self.robot_positions[robot] = node
            self.draw_graph()
            self.log(f"{robot} moved to {node}")
            time.sleep(1)
        
        self.robot_statuses[robot] = "Task Complete"
        self.log(f"{robot} reached its destination {destination}")
        self.status_label.config(text=f"{robot} reached its destination")
        messagebox.showinfo("Task Complete", f"{robot} reached its destination")
    
    def find_alternate_path(self, robot, destination):
        #Find an alternate path if the original is blocked.
        try:
            for path in nx.all_simple_paths(self.graph, self.robot_positions[robot], destination):
                if not any(node in self.robot_positions.values() for node in path[1:]):
                    return path
        except nx.NetworkXNoPath:
            return None
        return None
    
    def run(self):
        self.root.mainloop()

# Load Graph Data from JSON
def load_graph(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)

    # Assign positions to nodes
    graph = nx.Graph()
    nodes = {i: (item[0], item[1]) for i, item in enumerate(data.get("vertices", []))}
    graph.add_nodes_from(nodes.keys())
    
    for node, pos in nodes.items():
        graph.nodes[node]['pos'] = pos
    
    graph.add_edges_from(data.get("lanes", []))
    return graph

if __name__ == "__main__":
    json_file = "data/nav_graph_sample/nav_graph_1.json"
    graph = load_graph(json_file)
    FleetGUI(graph)
