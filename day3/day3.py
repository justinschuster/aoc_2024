import re

def read_file():
    f = open('input.txt', 'r')
    return f.read()

def find_operations():
    data = read_file()
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(mul_pattern, data)
    out = []
    for match in matches:
        s = match.split(',')
        s[0] = int(s[0].replace('mul(', ''))
        s[1] = int(s[1].replace(')', ''))
        out.append(s)
    return out

def part_one():
    operations = find_operations()
    out = 0
    for op in operations:
        total_prod = op[0] * op[1]
        out += total_prod
    return out

def main():
    print(part_one())

if __name__ == '__main__':
    main()
