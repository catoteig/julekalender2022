from math import pi, sqrt


def main():

    height = 180 - 20
    radius = 50
    side = sqrt(radius**2 + height**2)
    surface_dm2 = (pi*radius*side)/100
    decorations = [
        ['red', 4, 10],
        ['gold', 4, 15],
        ['light', 2, 30],
        ['glitter', 5, 15]
    ]

    price = [(coverage/100) * surface_dm2 * price for name, coverage, price in decorations]
    print(round(sum(price), -1))


if __name__ == '__main__':
    main()
