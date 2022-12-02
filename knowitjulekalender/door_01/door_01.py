
def find_word(current_word, pos, dictionary, letter, acc):

    if letter[pos:pos+len(current_word)] != current_word and current_word != "":
        return

    if pos + len(current_word) == len(letter):
        result = acc + dictionary[current_word]
        print(len(result))
    elif pos + len(current_word) > len(letter):
        return
    else:
        new_start = letter[pos + len(current_word)]
        for word in (filter(lambda item: item.startswith(new_start), dictionary.keys())):
            find_word(word, pos + len(current_word), dictionary, letter, acc + (dictionary[current_word] + " " if current_word != "" else ""))


def main():

    with open("letter.txt") as l:
        letter = l.read()

    with open("dictionary.txt") as d:
        dictionary = d.read().splitlines()
    mydict = {}
    for _ in dictionary:
        word = _.split(",")
        mydict[word[0]] = word[1]

    find_word("", 0, mydict, letter, "")


if __name__ == '__main__':
    main()
