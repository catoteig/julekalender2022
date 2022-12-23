import csv
import re


def main():

    permutations = {
        'Mye regn': {
            'down': 120*1000,
            'none': 80*1000,
            'up': 40*1000
        },
        'Lite eller ingen regn': {
            'down': 100*1000,
            'none': 60*1000
        }
    }

    with open('vannstand.txt') as f:
        water_all, water_list = [list(line) for line in f.read().splitlines()], []
        for _ in zip(*water_all):
            water_list.append(int([100-i for i, item in enumerate(_) if re.search(r'[^ ]', item)][0]))

    with open('vaer.csv', mode='r') as f:
        reader, weather_list = csv.reader(f), []
        next(reader)
        for i, weather in reader:
            weather_list.append(weather)

    production = 0
    prev = water_list[0]

    for weather, water in zip(weather_list, water_list[1:]):
        dir = 'none'
        if prev < water: dir = 'up'
        elif prev > water: dir = 'down'

        production += permutations[weather][dir]
        prev = water

    print(production)


if __name__ == '__main__':
    main()
