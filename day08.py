from math import gcd

with open('input.txt') as file:
    data = file.read().split('\n')
    sequence = data[0]
    mapping = {}
    currents = []
    for line in data[2:]:
        inputs = line.split()

        try:
            key = inputs[0]
            l = inputs[2][1:-1]
            r = inputs[3][:-1]

            mapping[key] = (l, r)

            if 'A' in key:
                currents.append(key)

        except Exception:
            break

    cycles = []

    for current in currents:
        stepcounter = 0
        seq = 0
        while True:
            stepcounter += 1
            if sequence[seq] == 'L':
                current = mapping[current][0]
            else:
                current = mapping[current][1]

            if 'Z' in current:
                cycles.append(stepcounter)
                break

            seq += 1
            if seq == len(sequence):
                seq = 0

    lcm = 1
    for i in cycles:
        lcm = lcm * i // gcd(lcm, i)

    print(lcm)