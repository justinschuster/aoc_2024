
def readInput():
    content = ''
    with open('input.txt', 'r') as file:
        content = file.readlines()
    return content

def check_horizontal(input):
    count = 0
    # left to right
    for line in input:
        for i in range(3, len(line)):
            x = line[i-3] == 'X'
            m = line[i-2] == 'M'
            a = line[i-1] == 'A'
            s = line[i] == 'S'
            if x and m and a and s:
                count += 1

    # right to left
    for line in input:
        for i in range(3, len(line)):
            s = line[i-3] == 's'
            a = line[i-2] == 'A'
            m = line[i-1] == 'M'
            x = line[i] == 'X'
            if x and m and a and s:
                count += 1

    return count

def check_vertical(input):
    n = len(input)
    count = 0
    # top down
    for i in range(n-3):
        for j in range(len(input[i])):
            x = input[i][j] == 'X'
            m = input[i+1][j] == 'M'
            a = input[i+2][j] == 'A'
            s = input[i+3][j] == 'S'
            if x and m and a and s:
                count += 1

    # bottom up
    for i in range(n-3):
        for j in range(len(input[i])):
            s = input[i][j] == 'S'
            a = input[i+1][j] == 'A'
            m = input[i+2][j] == 'M'
            x = input[i+3][j] == 'X'
            if x and m and a and s:
                count += 1

    return count

def check_diagonal(input):
    count = 0

    # check moving down right first
    for i in range(len(input)-3):
        for j in range(len(input[i])-3):
            x = input[i][j] == 'X'
            m = input[i+1][j+1] == 'M'
            a = input[i+2][j+2] == 'A'
            s = input[i+3][j+3] == 'S'
            if x and m and a and s:
                count += 1

    # check diagonal down left
    for i in range(len(input)-3):
        for j in range(3, len(input)):
            x = input[i][j] == 'X'
            m = input[i+1][j-1] == 'M'
            a = input[i+2][j-2] == 'A'
            s = input[i+3][j-3] == 'S'
            if x and m and a and s:
                count += 1

    # check diagonal up right
    for i in range(3, len(input)):
        for j in range(len(input[i])-3):
            x = input[i][j] == 'X'
            m = input[i-1][j+1] == 'M'
            a = input[i-2][j+2] == 'A'
            s = input[i-3][j+3] == 'S'
            if x and m and a and s:
                count += 1

    # check diagonal up left
    for i in range(3, len(input)):
        for j in range(3, len(input[i])):
            x = input[i][j] == 'X'
            m = input[i-1][j-1] == 'M'
            a = input[i-2][j-2] == 'A'
            s = input[i-3][j-3] == 'S'
            if x and m and a and s:
                count += 1

    return count

def part_one(input):
    count = 0
    count += check_horizontal(input)
    count += check_vertical(input)
    count += check_diagonal(input)
    return count

def main():
    input = readInput() 

    # part one
    print(part_one(input))
 
if __name__ == '__main__':
    main()
