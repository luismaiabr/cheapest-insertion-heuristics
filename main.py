import random
import matplotlib.pyplot as plt
from Product import Product
from Graph import Graph
product = Product()
graph=Graph(product)
for nothing in range(10):
        try:
            best_edge, min_aversion = graph.next_cheapest_insertion_edge()
            graph.add_edge(best_edge)
        except Exception as e:
            pass
print(f"Final inserted nodes: {graph.inserted_nodes}")
print(f"Final affinity: {graph.calculate_total_affinity()}")
print(f"Final inserted edges: {graph.inserted_edges}")

# Expected results for 10 iterations (13 total products):
# Final inserted nodes: {0, 33, 2, 3, 37, 6, 8, 11, 14, 47, 22, 25, 26}
# Final affinity: 126
# Final inserted edges: [(0, 33), (33, 47), (47, 22), (8, 0), (22, 37), (37, 25), (3, 8), (25, 11), (6, 3), (14, 6), (11, 2), (2, 26), (26, 14)]

