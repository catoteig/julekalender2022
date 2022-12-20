def main():
    elf_paths, start_pos, found = [], [], set()
    with open('alv_sti.txt') as f:
        for i, line in enumerate(f.read().splitlines()):
            if i > 0:
                pos, path = line.split(')')
                x, y = pos[1:].split(', ')
                start_pos.append((int(x), int(y)))
                elf_paths.append(path)

    for pos, path in zip(start_pos, elf_paths):
        x, y = pos
        for loc in path:
            if loc == 'g':
                found.add((x, y))
            elif loc == 'n':
                y += 1
            elif loc == 's':
                y -= 1
            elif loc == 'e':
                x += 1
            elif loc == 'v':
                x -= 1

    print(len(found))


if __name__ == '__main__':
    main()
