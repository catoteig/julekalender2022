import math


def main():
    num_gifts = 10 ** 6
    travel_distance = 10 ** 5  # km
    gift_interval = 100  # m
    distance_per_reindeer = 10 ** 3  # km
    reindeer_capacity = 200  # kg
    shifts = 100
    weights = {'gift': 0.100, 'reindeer': 100, 'santa': 100, 'sleigh': 900}  # kg

    gifts_per_shift = num_gifts / shifts

    weight_of_sleigh = weights['santa'] + weights['sleigh']
    reindeers_riding = 0
    reindeers_needed = 0

    for shift in range(shifts, 0, -1):
        weight_of_sleigh += (gifts_per_shift * weights['gift']) + (reindeers_riding * weights['reindeer'])
        reindeers_riding = math.ceil(weight_of_sleigh / reindeer_capacity)
        reindeers_needed += reindeers_riding

    print(reindeers_needed)  # Why is this wrong????? 🤯


if __name__ == '__main__':
    main()
