# voronoi-and-triangulations
This repository contains Python implementations of examples of the Voronoi diagram and the Delaunay triangulation, with visualization and console outputs.

## Repository structure
This repository contains the following Python scripts:
1. `voronoi.py`:
  - Determines the number of half-lines contained in the **Voronoi diagram** associated with a given set of example points.
  - Visualizes the result with `matplotlib`
2.  `triangulations.py`:
  - Represents an algorithm to indicate the number of triangles and the number of edges of a triangulation.
  - Visualizes how the \( \lambda \) value influences the triangulation with `matplotlib`.

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

You can check your Python version using:
```
python --version
```

## Installation
1. Clone the Repository:
```
git clone https://github.com/taniatitiriga/voronoi-and-triangulations.git
cd voronoi-and-triangulations
```
2. Set Up a Virtual Environment (Optional but Recommended):
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3. Install Required Libraries:
- Install `matplotlib` for visualization:
```
pip install matplotlib
```
- Install `scipy` for Voronoi and Delaunay algorithms:
```
pip install scipy
```

## Usage
Each script can be executed individually to see its functionality. Below are the details for each:
1. `voronoi.py`
  - **Task:** Determine the number of half-lines contained in the Voronoi diagram associated with the given set of points.
  - **Run the script** (or use your prefered IDE - I recommend VSCode):
```
python voronoi.py
```
2. `triangulations.py`
  - **Task:** Write and implement an algorithm to indicate the number of triangles and the number of edges of a triangulation associated with the set {A, B, C, D, E, M}.
  - **Run the script** (or use your prefered IDE - I recommend VSCode):
```
python triangulations.py
```
