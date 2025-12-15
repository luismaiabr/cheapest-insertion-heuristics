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

