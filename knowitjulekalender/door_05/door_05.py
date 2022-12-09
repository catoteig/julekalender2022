def shuffle(deck):

    newdeck = []
    for a, b in zip(deck[:(len(deck)//2)], deck[(len(deck)//2):]):
        newdeck.extend([a, b])

    return newdeck


def main():

    size = 0
    outshuffles = 0

    while outshuffles != 13:

        size += 2
        initialdeck = list(range(1, size+1))
        newdeck = shuffle(initialdeck)
        attempts = 1

        while initialdeck != newdeck:
            newdeck = shuffle(newdeck)
            attempts += 1

        outshuffles = attempts

    print(size)


if __name__ == '__main__':
    main()
