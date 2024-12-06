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

def part_two():
    #data = read_file()
    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    split_data = data.split("don't")
    print(split_data)
    pattern = r'^(.*?)(?:don\'t\(\)|$)'
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.finditer(pattern, data)
    out = 0
    for match in matches:
        section = match.group(1)
        mul_matches = re.finditer(mul_pattern, section)
        for mul in mul_matches:
            s = mul.group(0).replace('mul(', '')
            s = s.replace(')', '')
            split_list = s.split(',')
            print(split_list)
            curr = int(split_list[0]) * int(split_list[1]) 
            out += curr
    return out

def main():
    print(part_one())
    print(part_two())

if __name__ == '__main__':
    main()
