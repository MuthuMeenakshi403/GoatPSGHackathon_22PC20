from models.nav_graph import load_all_graphs
from gui.fleet_gui import FleetGUI
import os

# Define the data folder
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "../data/nav_graph_samples")

def main():
    # Load all navigation graphs
    graphs = load_all_graphs(DATA_FOLDER)
    
    if not graphs:
        print("Error: No valid navigation graphs found in data folder.")
        return
    
    # Select the first available graph as default
    default_graph = list(graphs.values())[0]
    
    # Start the GUI
    app = FleetGUI(default_graph)
    app.run()

if __name__ == "__main__":
    main()
