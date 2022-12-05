def main():

    with open("gaver.txt") as f:
        gaver = f.readlines()

    validlines, validgifts, total = 1, 0, 0

    for _ in gaver:
        if "alv" in _:
            total += 2 + validlines if validgifts > 3 else 2
        else:
            validgifts += 1
            if validgifts > 3:
                validlines += 1
            total += 1 + validlines

    print(total)


if __name__ == '__main__':
    main()
