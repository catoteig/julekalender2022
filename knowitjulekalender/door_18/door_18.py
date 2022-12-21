import knowitjulekalender.door_11.door_11 as door_11


def bits2string(bits):
    print(f'Converting: {bits}')
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'little').decode('ascii')


def main():
    with open('input.txt') as f:
        nisse_safe = (f.read())

    n = 5
    paritybits = [2 ** n for n in range(n)]
    datablocks = [nisse_safe[datapart:datapart + 2 ** n] for datapart in range(0, len(nisse_safe), 2 ** n)]
    encoded_text = ''

    for data in datablocks:

        datablock = [int(_) for _ in data]
        failed_parities, passed_parities = [], []

        for parity in paritybits:
            if door_11.validate_parity(datablock, parity):
                passed_parities.append(parity)
            else:
                failed_parities.append(parity)

        if failed_parities:
            failed = [door_11.generate_counting_bits(_, n) for _ in failed_parities]
            passed = [door_11.generate_counting_bits(_, n) for _ in passed_parities]

            reminder = door_11.find_reminder(failed, passed, n)
            datablock[reminder] = 0 if datablock[reminder] == 1 else 1

        encoded_data = door_11.remove_paritybits(datablock, paritybits)
        encoded_data_string = ''.join([str(_) for _ in encoded_data])

        for bit in range(0, 24, 8):
            print(encoded_data_string[bit+1:bit + 8] + " :: " + bits2string(encoded_data_string[bit+1:bit + 8]))
            encoded_text += bits2string(encoded_data_string[bit+1:bit + 8])

    print(f'Encoded text: {encoded_text}')  # IS WRONG!!!!


if __name__ == '__main__':
    main()
