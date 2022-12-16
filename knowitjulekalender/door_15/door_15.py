import csv


def main():

    with open('data.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        gifts = [[int(value), int(volume)] for value, volume in reader]

    sack_capacity, max_price, sacks_used = 120, 1700, 0

    while gifts:
        value_left, volume_left, pop = max_price, sack_capacity, []
        for i, [value, volume] in enumerate(gifts):
            if value <= value_left and volume <= volume_left:
                value_left -= value
                volume_left -= volume
                pop.append(i)

            if value_left == 0 or volume_left == 0:
                continue

        pop.sort(reverse=True)
        for i in pop: gifts.pop(i)
        sacks_used += 1

    print(sacks_used)


if __name__ == '__main__':
    main()
