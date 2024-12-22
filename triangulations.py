import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np

def generate_points(lambda_value):
    """
    Generates the set of points {A, B, C, D, E, M} from the exercise.

    Args:
        lambda_value (float): The value of \u03bb for the point M.

    Returns:
        numpy.ndarray: Array of points.
    """
    A = (1, -1)
    B = (-1, 1)
    C = (2, -1)
    D = (1, 1)
    E = (0, 2)
    M = (1, lambda_value)
    return np.array([A, B, C, D, E, M])

def analyze_triangulation(points):
    """
    Performs Delaunay triangulation and analyzes the results.

    Args:
        points (numpy.ndarray): The set of points to triangulate.

    Returns:
        tuple: Number of triangles and edges in the triangulation.
    """
    tri = Delaunay(points)
    num_triangles = len(tri.simplices)
    edges = set()
    for simplex in tri.simplices:
        for i in range(len(simplex)):
            edge = tuple(sorted([simplex[i], simplex[(i + 1) % len(simplex)]]))
            edges.add(edge)
    num_edges = len(edges)
    return num_triangles, num_edges, tri

def plot_triangulation(points, tri):
    """
    Visualizes the Delaunay triangulation.

    Args:
        points (numpy.ndarray): The set of points.
        tri (scipy.spatial.Delaunay): The triangulation object.
    """
    plt.figure(figsize=(8, 8))
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, color='darkorange')
    plt.scatter(points[:, 0], points[:, 1], color='blue')

    # Annotate points
    labels = ["A", "B", "C", "D", "E", "M"]
    for i, (x, y) in enumerate(points):
        plt.text(x, y, labels[i], fontsize=12, ha='right')

    plt.title("Delaunay Triangulation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    """
    Main function to compute and visualize the triangulation for the given points.
    """
    lambda_value = float(input("Enter the value of lambda (\u03bb): "))
    points = generate_points(lambda_value)
    num_triangles, num_edges, tri = analyze_triangulation(points)
    
    print(f"Number of triangles: {num_triangles}")
    print(f"Number of edges: {num_edges}")

    plot_triangulation(points, tri)

if __name__ == "__main__":
    main()
