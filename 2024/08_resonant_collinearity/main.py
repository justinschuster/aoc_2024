from collections import defaultdict
from itertools import combinations
from math import sqrt

def read_input(input='input.txt'):
    lines = open(input, 'r').readlines()
    return [list(line.replace('\n', '')) for line in lines]

def solve(input):
    antennas = defaultdict(list)
    rows, cols = len(input), len(input[0])

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == '.':
                continue

            if col not in antennas:
                antennas[col] = [(i, j)]
            else:
                antennas[col].append((i, j))

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == '.':
                continue

            if input[i][j] not in antennas:
                antennas[input[i][j]] = [(i, j)]
            else:
                antennas[input[i][j]].append((i, j))

    antinodes = set()
    for frequency in antennas:
        pairs = set(combinations(antennas[frequency], 2))
        for pair in pairs:
            x1, y1 = pair[0]
            x2, y2 = pair[1]

            v = (x2-x1, y2-y1)
            d = sqrt((x2-x1)**2 + (y2-y1)**2)

            if d == 0:
                continue

            u = (v[0]/d, v[1]/d)

            ax = int(round(2*d*u[0] + x1, 2))
            ay = int(round(2*d*u[1] + y1, 2))

            if 0 <= ax < cols and 0 <= ay < rows:            
                antinodes.add((ax, ay))

    return len(antinodes)

if __name__ == '__main__':
    input = read_input() 
    print(solve(input))
