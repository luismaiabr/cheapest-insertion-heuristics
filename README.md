# Cheapest Insertion TSP Heuristic

⚠️ **ALPHA VERSION** - This is an alpha/preliminary version. I didn't have time to polish the code or documentation yet.

## Overview

This repository contains a Python implementation of the **Cheapest Insertion Heuristic** for solving the Traveling Salesman Problem (TSP). The algorithm builds a tour by iteratively adding cities at positions that minimize the total distance increase.

## Algorithm Description

The Cheapest Insertion Heuristic is a constructive algorithm for the TSP that works as follows:

1. **Initialization**: Start with a small tour of 3 cities forming a triangle
2. **Iterative Insertion**: For each remaining city:
   - Calculate the cost of inserting it at each possible position in the current tour
   - Insert the city at the position with minimum cost increase
3. **Repeat**: Continue until all cities are included in the tour

The algorithm provides a reasonable approximation for the TSP in polynomial time, making it suitable for small to medium-sized problem instances.

## Implementation Details

### Main Components

- **`Distances` class**: Manages the distance matrix, city coordinates, and tour construction
  - `distances`: 6x6 matrix representing distances between cities (cities 0-5)
  - `city_coords`: Coordinates for visualization
  - `tour`: Current tour as an ordered list of cities
  - `linked_cities`: Set of edges representing connections in the tour

### Key Methods

- `get_total_distance()`: Calculates the total distance of the current tour
- `tour_to_edges(tour)`: Converts an ordered tour list to a set of edges
- `get_distance(i, j)`: Returns the distance between cities i and j
- `get_initial_tour()`: Initializes the algorithm with a 3-city triangle
- **Cheapest insertion logic**: Finds the optimal position to insert each remaining city

### Visualization

The implementation includes visualization using `matplotlib` to display:
- Cities as numbered points
- Current tour edges
- Step-by-step construction of the solution

## Requirements

```
python >= 3.6
matplotlib
```

## Usage

The notebook can be run in:
- Google Colab (recommended)
- Jupyter Notebook
- Any Python environment with matplotlib support

Simply open `Cheapest_insertion (1).ipynb` and run all cells to see the algorithm in action with the provided example problem.

## Example Problem

The included example uses a 6-city problem with:
- Cities numbered 0-5
- Predefined distance matrix
- 2D coordinates for visualization

## Limitations & Future Work

Since this is an alpha version:
- Limited documentation and comments in code
- Hardcoded example problem (6 cities)
- No command-line interface or configurable inputs
- Visualization could be improved
- No performance optimization
- Missing unit tests

## References

The Cheapest Insertion Heuristic is a well-known TSP approximation algorithm. For more information on TSP heuristics and optimization:
- Rosenkrantz, D. J., Stearns, R. E., & Lewis, P. M. (1977). "An analysis of several heuristics for the traveling salesman problem"
- General TSP literature on constructive heuristics

## License

[Add your preferred license]

## Author

[Your name/contact]

---

*Note: This is a work in progress. Contributions, suggestions, and improvements are welcome!*
