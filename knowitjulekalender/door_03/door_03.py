import csv


def csv_to_list(csv_file):
    with open(csv_file, mode='r') as f:
        reader, result = csv.reader(f), []
        next(reader)
        for b, h, l in reader:
            result.append([int(b), int(h), int(l)])
    return result


def main():
    pakker = csv_to_list("pakker.csv")
    bredde = 110
    total = 0

    for pakke in pakker:
        pakke.sort()
        x, y, z = pakke

        muligheter = []
        if bredde >= 2 * (z + x):
            muligheter.append(x + y)
        if bredde >= 2 * (y + x):
            muligheter.append(z + x)
        if bredde >= z + x:
            muligheter.append(2 * (x + y))
        if bredde >= y + x:
            muligheter.append(2 * (z + x))

        total += min(muligheter)

    print(total)


if __name__ == '__main__':
    main()
