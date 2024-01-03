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


G = nx.DiGraph()
input_graph(G)
nx.draw(G, with_labels=True, font_color='red')

flowCost, flowDict = nx.capacity_scaling(G)
print(flowDict)

mpl.show()