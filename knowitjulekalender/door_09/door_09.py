from collections import defaultdict
import re


def run_machine(params):

    t, v, k = params
    if 95 <= t <= 105 and 400 <= v <= 1500 and 300 <= k <= 500:
        v -= 100
        k //= 10
        liters = v + k
        liters -= (liters//40 if t >= 100 else 0)
    else:
        liters = 0

    return liters


def main():

    produced = defaultdict(int)

    with open('julebrusmaskiner.txt') as f:
        for _ in f.read().splitlines():
            log_items = _.split(', ')
            machine = log_items[0][7:]
            params = [int(re.findall('\d+', x)[0]) for x in log_items[1:]]
            produced[machine] += run_machine(params)

    sum = 0
    for _ in produced:
        sum += produced[_]
    best_machine = max(produced, key=produced.get)

    print(f'{sum} {best_machine}')


if __name__ == '__main__':
    main()
