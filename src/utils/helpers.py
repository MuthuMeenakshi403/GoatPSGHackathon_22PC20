import json
import networkx as nx

def load_nav_graph(file_path):
    #Loads the navigation graph from a JSON file.
    with open(file_path, "r") as f:
        data = json.load(f)

    graph = nx.Graph()

    # Add vertices 
    for idx, (x, y, attributes) in enumerate(data["vertices"]):
        graph.add_node(idx, pos=(x, y), **attributes)

    # Add lanes 
    for edge in data["lanes"]:
        graph.add_edge(edge[0], edge[1])

    return graph

def get_shortest_path(graph, start, end):
    #Finds the shortest path between two nodes.
    if nx.has_path(graph, start, end):
        return nx.shortest_path(graph, start, end)
    return None  

def is_node_charger(graph, node):
    #Checks if a node is a charging station.
    return graph.nodes[node].get("is_charger", False)
