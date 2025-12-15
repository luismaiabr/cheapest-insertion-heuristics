import logging
from Product import Product, ProductData

# Configure logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Graph:
    def __init__(self,product):
        logger.info("Initializing Graph")
        initial_triplet, initial_aversion = self.get_initial_smallest_aversion_three_inserted_edges(ProductData(data=product.data))
        self.inserted_nodes = set(initial_triplet)
        self.inserted_edges = [(initial_triplet[0], initial_triplet[1]), 
                      (initial_triplet[1], initial_triplet[2]), 
                      (initial_triplet[2], initial_triplet[0])]
        self.product = product
        logger.info(f"Initial triplet: {initial_triplet}, Initial aversion: {initial_aversion}")
        logger.info(f"Initial inserted_edges: {self.inserted_edges}")
        
    def get_initial_smallest_aversion_three_inserted_edges(self, data: ProductData):
        min_aversion = float('inf')
        best_triplet = None
        for i in range(49):
            for j in range(i + 1, 49):
                for k in range(j + 1, 49):
                    aversion = (data.data.iat[i, j] * -1 +
                                data.data.iat[j, k] * -1 +
                                data.data.iat[k, i] * -1)
                    if aversion < min_aversion:
                        min_aversion = aversion
                        best_triplet = (i, j, k)
        return best_triplet, min_aversion
    def non_inserted_nodes(self):
        all_nodes = set(range(49))
        return all_nodes - self.inserted_nodes
    def calculate_total_affinity(self):
        affinity = 0
        for i,j in self.inserted_edges:
            affinity += self.product.calculate_affinity(i,j)
        return affinity
    def next_cheapest_insertion_edge(self):
        logger.info("Finding next cheapest insertion edge")
        try:
            #we're gonna check for the smallest aversion
            min_aversion = float('inf')
            best_edge = None
            logger.debug(f"Current inserted_edges: {self.inserted_edges}")
            logger.debug(f"Inserted nodes: {self.inserted_nodes}")
            
            for ni in self.non_inserted_nodes():
                
                for i,j in self.inserted_edges:
                    
                    
                    aversion = (self.product.calculate_aversion(i, ni) + self.product.calculate_aversion(ni, j) - self.product.calculate_aversion(i, j))
                    if aversion < min_aversion:
                        min_aversion = aversion
                        best_edge = (ni, i, j)
            return best_edge, min_aversion
        except Exception as e:
            logger.exception(f"Error while calculating next cheapest insertion edge: {e}")
            raise
    def add_edge(self, edge):
        ni, i, j = edge
        logger.info(f"Inserting edge with non-inserted node: {ni} between nodes: {i} and {j}")
        self.inserted_nodes.add(ni)
        self.inserted_edges.remove((i, j))
        self.inserted_edges.append((i, ni))
        self.inserted_edges.append((ni, j))
        logger.debug(f"Updated inserted_nodes: {self.inserted_nodes}")
        logger.debug(f"Updated inserted_edges: {self.inserted_edges}")
    def insert_edge(self, edge):
        pass

    