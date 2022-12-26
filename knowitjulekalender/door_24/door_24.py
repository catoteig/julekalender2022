import matplotlib.pyplot as plt


def main():

    with open('kryptert_julehilsen.txt') as f:
        values = [tuple(map(lambda _: int(_), x.split(','))) for x in f.read()[1:-1].split('), (')]
        for x, y in values:
            plt.plot(x, y, marker='o', markeredgecolor='red', markerfacecolor='red')
        plt.show()
        # Reads:
        # 01100111 01101100 01100101 01100100 01100101 01101100 01101001
        # 01100111 00100000 01101010 01110101 01101100 00100001 00100001


if __name__ == '__main__':
    main()
