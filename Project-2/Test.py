import networkx as nx
import matplotlib.pyplot as plt

# Define the edges
edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'),
    ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'K'),
    ('K', 'L'), ('L', 'M'), ('M', 'N'), ('N', 'O'), ('O', 'P'),
    ('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'T'), ('T', 'U'),
    ('U', 'V'), ('V', 'W'), ('W', 'X'), ('X', 'Y'), ('Y', 'Z'),
    ('Z', 'A')
]

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

# Show the plot
plt.show()
