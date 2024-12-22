import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

def generate_points():
    # Generate points for A, B, and C
    A_points = [(1 + i, i - 1) for i in range(6)]
    B_points = [(-i, i) for i in range(6)]
    C_points = [(0, i) for i in range(6)]
    return np.array(A_points + B_points + C_points)

def count_half_lines(vor):
    # Count edges extending to infinity (half-lines)
    half_lines = 0
    for point_idx, vertex_indices in enumerate(vor.ridge_vertices):
        if -1 in vertex_indices:  # -1 indicates infinity
            half_lines += 1
    return half_lines

def main():
    # Generate points
    points = generate_points()

    # Compute Voronoi diagram
    vor = Voronoi(points)

    # Count half-lines
    half_line_count = count_half_lines(vor)

    # Plot the Voronoi diagram
    fig, ax = plt.subplots(figsize=(8, 8))
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=1.5, point_size=10)

    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], color='blue', label='Points')

    # Annotate the points for clarity
    for idx, (x, y) in enumerate(points):
        ax.text(x, y, f"P{idx}", fontsize=8, color="green")

    # Customize plot
    ax.set_title("Voronoi Diagram with Half-Lines", fontsize=14)
    ax.legend()
    ax.grid(True)
    plt.axis("equal")

    # Show result
    plt.show()

    # Print the count of half-lines
    print(f"Number of half-lines in the Voronoi diagram: {half_line_count}")

if __name__ == "__main__":
    main()
