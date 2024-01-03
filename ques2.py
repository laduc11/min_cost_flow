import networkx as nx
import matplotlib.pyplot as mpl

# input graph
def input_graph(G):
    # add node
    G.add_node("0", demand=0)
    G.add_node("1", demand=-13)
    G.add_node("2", demand=0)
    G.add_node("3", demand=0)
    G.add_node("4", demand=13)

    #add egde
    G.add_edge("0", "1", weight=2, capacity=10)
    G.add_edge("0", "2", weight=6, capacity=5)
    G.add_edge("1", "2", weight=1, capacity=15)
    G.add_edge("1", "3", weight=3, capacity=9)
    G.add_edge("2", "3", weight=1, capacity=10)
    G.add_edge("2", "4", weight=3, capacity=10)
    G.add_edge("3", "4", weight=5, capacity=5)

# detect negative cycle
def have_neg_cycle(G, source, sink):
    for node in G.nodes(data=True):
        if node[1]['demand'] > 0:
            sink += [node[0]]
        elif node[1]['demand'] < 0:
            source += [node[0]]

    for node in source:
        try: 
            nx.find_negative_cycle(G, source='1') 
        except nx.NetworkXError:
            pass
        else:
            print("Graph have negative cycle")
            exit()

source = []
sink = []
G = nx.DiGraph()
input_graph(G)
have_neg_cycle(G, source, sink)
position = nx.circular_layout(G)
nx.draw(G, with_labels=True, font_color='red', node_size=800, pos=position)
nx.draw_networkx_edge_labels(G, pos=position, edge_labels=nx.get_edge_attributes(G, 'weight'))
flowCost, flowDict = nx.capacity_scaling(G)

# Print result
print(flowDict)
print(flowCost)

mpl.show()