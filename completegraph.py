import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (greater than 3): "))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    G = nx.complete_graph(n)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=800, font_size=12, font_weight='bold')

    plt.title(f"Complete Graph with {n} Vertices")
    plt.show()
