import json
import networkx as nx
import os

def load_nav_graph(json_file):
    #Loads the navigation graph from a JSON file and returns a NetworkX graph.
    with open(json_file, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode {json_file}. Ensure it's a valid JSON.")
            return None

    # Extract the first level dynamically (assuming single-level structure)
    if "levels" not in data or not isinstance(data["levels"], dict):
        print(f"Error: {json_file} does not contain 'levels'.")
        return None

    # Get the first key in "levels"
    level_key = next(iter(data["levels"]))  
    level_data = data["levels"][level_key]

    if "vertices" not in level_data or "lanes" not in level_data:
        print(f"Error: {json_file} is missing required keys ('vertices' or 'lanes').")
        return None

    G = nx.Graph()

    # Add vertices
    for i, vertex in enumerate(level_data["vertices"]):
        if not isinstance(vertex, list) or len(vertex) < 3:
            print(f"Error: Invalid vertex format in {json_file}. Expected list format.")
            continue  

        x, y, attrs = vertex
        G.add_node(i, pos=(x * 50 + 100, y * 50 + 100), **attrs)

    # Add lanes
    for lane in level_data["lanes"]:
        if not isinstance(lane, list) or len(lane) < 2:
            print(f"Error: Invalid lane format in {json_file}. Expected list of two integers.")
            continue  
        G.add_edge(lane[0], lane[1])

    return G

def load_all_graphs(data_folder):
    #Loads all navigation graphs from the given data folder.
    graphs = {}
    for file in os.listdir(data_folder):
        if file.endswith(".json") and not file.startswith("._"):  
            graph_name = file.replace(".json", "")
            graph = load_nav_graph(os.path.join(data_folder, file))
            if graph is not None:
                graphs[graph_name] = graph
    return graphs
