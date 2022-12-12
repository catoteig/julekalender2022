import os
import matplotlib.pyplot as plt
from exif import Image


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def main():
    coords_x, coords_y = [], []
    for filename in os.listdir('pokemon'):
        f = os.path.join('pokemon', filename)
        if os.path.isfile(f):
            with open(f, 'rb') as src:
                img = Image(src)
                coords_x.append(decimal_coords(img.gps_longitude, img.gps_longitude_ref))
                coords_y.append(decimal_coords(img.gps_latitude, img.gps_latitude_ref))

    plt.rcParams["figure.figsize"] = [7, 7]
    plt.rcParams["figure.autolayout"] = True
    plt.plot(coords_x, coords_y, 'r*')
    plt.show()


if __name__ == '__main__':
    main()
