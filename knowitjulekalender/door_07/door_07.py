import matplotlib.pyplot as plt


def is_evil(number):
    return True if str(f'{int(number):08b}').count('1') % 2 == 0 else False


def main():

    plt.rcParams["figure.figsize"] = [30, 30]
    plt.rcParams["figure.autolayout"] = True

    coords_x, coords_y = [], []

    with open('encrypted.txt') as f:
        for x, line in enumerate(f.read().splitlines()):
            for y, number in enumerate(line[:-1].split(' ')):
                if is_evil(number):
                    coords_x.append(x)
                    coords_y.append(y)

    plt.plot(coords_x, coords_y, 'r*')
    plt.show()


if __name__ == '__main__':
    main()
