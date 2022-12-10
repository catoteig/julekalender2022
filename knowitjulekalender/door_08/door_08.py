import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt


def main():

    coords = np.ndarray((0, 2), dtype=tuple)
    with open('data.txt') as f:
        for i, line in enumerate(f.read().splitlines()):
            coords = np.append(coords, [tuple(float(x) for x in line.split(' '))], axis=0)

    hull = ConvexHull(coords)
    print(round(hull.volume))

    # Plot:
    plt.plot(coords[:,0], coords[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(coords[simplex, 0], coords[simplex, 1], 'k-')
    plt.show()


if __name__ == '__main__':
    main()
