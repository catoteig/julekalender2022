def validate_parity(matrix, parity):
    total = skip = take = 0

    for value in matrix:
        if skip == 0 and take == 0:
            skip = take = parity

        if skip > 0:
            skip -= 1
        elif take > 0:
            total += value
            take -= 1

    return total % 2 == 0


def generate_counting_bits(parity, n):
    skip = take = 0
    matrix = []

    for idx in range(2**n):
        if skip == 0 and take == 0:
            skip = take = parity

        if skip > 0:
            skip -= 1
        elif take > 0:
            matrix.append(idx)
            take -= 1

    return matrix


def remove_paritybits(matrix, paritybits):
    return [v for i, v in enumerate(matrix) if i not in paritybits and i != 0]


def find_reminder(failed, passed, n):
    failed_intersection = set.intersection(*map(set, failed)) if failed else {}
    passed_flattened = {i for lst in passed for i in lst}

    return list(failed_intersection - passed_flattened - {2**n for n in range(n)})[0]


def main():

    n = 4
    matrixes = [
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    ]
    paritybits = [2**n for n in range(n)]
    original_data = []

    for matrix in matrixes:
        failed_parities, passed_parities = [], []

        for parity in paritybits:
            if validate_parity(matrix, parity):
                passed_parities.append(parity)
            else:
                failed_parities.append(parity)

        if failed_parities:
            failed = [generate_counting_bits(_, n) for _ in failed_parities]
            passed = [generate_counting_bits(_, n) for _ in passed_parities]
            reminder = find_reminder(failed, passed, n)
            matrix[reminder] = 0 if matrix[reminder] == 1 else 1
            original_data.append(remove_paritybits(matrix, paritybits))
        else:
            original_data.append(remove_paritybits(matrix, paritybits))

    print(''.join([str(i) for lst in original_data for i in lst]))


if __name__ == '__main__':
    main()
