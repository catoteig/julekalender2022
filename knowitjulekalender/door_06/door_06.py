from collections import defaultdict


def main():

    naughty_actions = {}
    candidates = defaultdict(float)

    with open("slemmehandlinger.txt") as f:

        for line in f.read().splitlines():
            split = line.split(':')
            naughty_actions[split[0]] = float(split[1])

    with open("stemmer.txt") as f:

        for line in f.read().splitlines():
            actions_weighted = []
            action_vote = line.split(':')
            for action in action_vote[0].split(','):
                if action in naughty_actions:
                    actions_weighted.append(naughty_actions[action])
                else:
                    actions_weighted.append(1)

            if len(actions_weighted) > 0:
                candidates[action_vote[1]] += min(actions_weighted)

    winner = candidates.pop(max(candidates.keys(), key=(lambda k: candidates[k])))
    second = candidates.pop(max(candidates.keys(), key=(lambda k: candidates[k])))

    print(round(winner - second))


if __name__ == '__main__':
    main()
