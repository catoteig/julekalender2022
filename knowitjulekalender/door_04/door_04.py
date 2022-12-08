import numpy


def is_palindrome(number):
    n = str(number)
    return True if n == n[::-1] else False


# WARNING: superslow 🐌🐌🐌
def main():

    limit = 10000000
    bases = list(range(2, 17))
    total = 0

    for number in range(0, limit+1):

        is_valid = []
        for base in bases:
            if is_palindrome(numpy.base_repr(number, base)):
                is_valid.append(number)

        if len(is_valid) >= 3:
            total += number

    print(total)


if __name__ == '__main__':
    main()
