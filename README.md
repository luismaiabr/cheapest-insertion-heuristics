# Cheapest Insertion Heuristic for Product Affinity Optimization

A Python implementation of the Cheapest Insertion Heuristic algorithm for optimizing product arrangement based on affinity scores. This project finds an optimal sequence of 49 products that maximizes total affinity between adjacent items.

## Overview

This implementation uses a graph-based approach to solve a product placement optimization problem. Given a 49×50 affinity matrix representing compatibility scores between products, the algorithm constructs a tour that maximizes the sum of affinities between consecutive products.

## Algorithm Description

The Cheapest Insertion Heuristic works as follows:

1. **Initialization**: Find the triplet of products (i, j, k) with minimum total aversion (negative affinity)
2. **Iterative Insertion**: For each remaining product:
   - Evaluate the cost of inserting it between each pair of adjacent products in the current sequence
   - Insert the product at the position that minimizes the aversion increase
   - Cost calculation: `aversion(i, new) + aversion(new, j) - aversion(i, j)`
3. **Repeat**: Continue until all 49 products are inserted into the sequence

This greedy approach provides a good approximation in polynomial time: O(n³) for initialization and O(n²) per insertion.

## Project Structure

```
cheapest-insertion-heuristics/
├── main.py                          # Main execution script
├── Graph.py                         # Graph class with insertion logic
├── Product.py                       # Product data loader and affinity calculations
├── data.xlsx                        # Excel file with affinity matrix (not in repo)
├── pyproject.toml                   # Project dependencies
└── README.md                        # This file
```

## Implementation Details

### Core Classes

#### `Product` (Product.py)
- Loads affinity data from Excel file (`data.xlsx`)
- Validates 49×50 dataframe structure using Pydantic
- Provides methods:
  - `calculate_affinity(p1, p2)`: Returns affinity score between products
  - `calculate_aversion(p1, p2)`: Returns negative affinity (cost)

#### `Graph` (Graph.py)
- Manages the product insertion sequence
- Key attributes:
  - `inserted_nodes`: Set of products already in the sequence
  - `inserted_edges`: List of tuples representing adjacent product pairs
  - `product`: Reference to Product instance
- Key methods:
  - `get_initial_smallest_aversion_three_inserted_edges()`: Finds optimal starting triplet
  - `next_cheapest_insertion_edge()`: Finds best (product, position) to insert next
  - `add_edge()`: Inserts product into sequence and updates edges
  - `calculate_total_affinity()`: Computes sum of all edge affinities

### Data Format

The `data.xlsx` file must contain:
- A sheet named `'affinity'`
- Columns B through AY (50 columns)
- 49 rows of numeric affinity scores
- Header row (skipped during loading)

## Requirements

```
python >= 3.10
pandas >= 2.3.3
openpyxl >= 3.1.5
matplotlib >= 3.10.8
pydantic >= 2.12.5
```

## Installation
## Installation

```bash
# Clone the repository
git clone https://github.com/luismaiabr/cheapest-insertion-heuristics.git
cd cheapest-insertion-heuristics

# Install dependencies using poetry
poetry install
```

## Usage

```bash
poetry run python main.py
```
### Output

The script will output:
```
Final inserted nodes: {0, 1, 2, ..., 48}
Final affinity: <total_affinity_score>
```

Plus detailed logging showing each insertion step (when DEBUG logging is enabled).

## Example

```python
from Product import Product
from Graph import Graph

# Load product affinity data
product = Product()

# Initialize graph with optimal starting triplet
graph = Graph(product)

# Perform insertions
for _ in range(10):  # Insert 10 products
    best_edge, min_aversion = graph.next_cheapest_insertion_edge()
    graph.add_edge(best_edge)

# View results
print(f"Inserted nodes: {graph.inserted_nodes}")
print(f"Total affinity: {graph.calculate_total_affinity()}")
```

print(f"Total affinity: {graph.calculate_total_affinity()}")
```

## Known Limitationsn uses directed tuples `(i, j)`, which can cause lookup failures when edge is stored as `(j, i)`
- No guarantee of tour continuity (edges stored as list, not ordered sequence)
- `main.py` only runs 10 iterations instead of all 46 remaining products
- Silent exception handling may hide bugs

## Future Improvements

- [ ] Refactor to use ordered tour list instead of edge tuples
- [ ] Add visualization of final product sequence
- [ ] Implement tour validation checks
- [ ] Add unit tests
- [ ] Support for different optimization objectives
- [ ] Performance benchmarking

## Author

Luis Maia (luismaiasombra@gmail.com)

## License

Not specified - see repository for details.
