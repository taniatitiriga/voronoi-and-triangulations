import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

def generate_points():
    """
    Generate three sets of points A, B, and C based on exercise requirements:
    - A_points: (1 + i, i - 1) for i in range(6)
    - B_points: (-i, i) for i in range(6)
    - C_points: (0, i) for i in range(6)

    Returns:
        tuple: A numpy array of all points combined and individual lists of A_points, B_points, and C_points.
    """
    A_points = [(1 + i, i - 1) for i in range(6)]
    B_points = [(-i, i) for i in range(6)]
    C_points = [(0, i) for i in range(6)]
    return np.array(A_points + B_points + C_points), A_points, B_points, C_points

def count_half_lines(vor):
    """
    Count the number of half-lines in the Voronoi diagram.

    Args:
        vor (scipy.spatial.Voronoi): The Voronoi diagram object.

    Returns:
        int: The count of half-lines in the Voronoi diagram.
    """
    half_lines = 0
    for point_idx, vertex_indices in enumerate(vor.ridge_vertices):
        if -1 in vertex_indices:  # -1 indicates infinity
            half_lines += 1
    return half_lines

def main():
    """
    Main function: generates points, computes the Voronoi diagram, and visualizes it.
    It counts the number of half-lines in the Voronoi diagram and prints it to console.
    """
    # generate points
    points, A_points, B_points, C_points = generate_points()

    # compute Voronoi diagram
    vor = Voronoi(points)

    # count half-lines
    half_line_count = count_half_lines(vor)

    # Visualize
    fig, ax = plt.subplots(figsize=(8, 8))
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=1.5, point_size=10)

    ax.scatter(points[:, 0], points[:, 1], color='blue', label='Points')

    for i, (x, y) in enumerate(A_points):
        ax.text(x, y, f"A{i}", fontsize=8, color="green")
    for i, (x, y) in enumerate(B_points):
        ax.text(x, y, f"B{i}", fontsize=8, color="purple")
    for i, (x, y) in enumerate(C_points):
        ax.text(x, y, f"C{i}", fontsize=8, color="red")

    ax.set_title("Voronoi Diagram Example", fontsize=14)
    ax.legend()
    ax.grid(True)

    ax.set_xlim(-6, 8)
    ax.set_ylim(-2, 8)

    ax.set_aspect('equal', adjustable='datalim')

    plt.show()

    # Print the count of half-lines in terminal
    print(f"Number of half-lines in the Voronoi diagram: {half_line_count}")

if __name__ == "__main__":
    main()
