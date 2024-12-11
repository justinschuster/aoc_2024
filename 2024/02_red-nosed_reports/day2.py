def readInput():
    out = []
    with open('input', 'r') as file: 
        for line in file:
            split_line = line.strip().split(' ')
            out.append(split_line)
    return out

def check_diff(report):
    for i in range(1, len(report)):
        diff = abs(int(report[i]) - int(report[i-1]))
        if diff < 1 or 3 < diff:
            return False
    return True

def check_asc_or_desc(report):
    asc = 0
    desc = 0
    n = len(report)
    for i in range(1, n):
        if (int(report[i]) - int(report[i-1])) > 0:
            asc += 1

    for i in range(1, n):
        if (int(report[i]) - int(report[i-1])) < 0:
            desc += 1

    if (n-1 == asc) or (n-1 == desc):
        return True
    else:
        return False

def check_remove_one(report):
    for i in range(1, len(report)):
        report_copy = report.copy()
        report_copy.pop(i)
        diff = check_diff(report_copy)
        asc_or_desc = check_asc_or_desc(report_copy)
        if diff and asc_or_desc:
            return True
    return False

def part_one():
    out = 0
    reports = readInput()
    for report in reports:
        diff = check_diff(report)
        asc_or_desc = check_asc_or_desc(report) 
        if diff and asc_or_desc:
            out += 1
    return out 

def part_two():
    out = 0
    reports = readInput()
    for report in reports:
        diff = check_diff(report)
        asc_or_desc = check_asc_or_desc(report) 
        if diff and asc_or_desc:
            out += 1
        elif check_remove_one(report):
            out += 1
    return out

if __name__ == '__main__':
    p1_ans = part_one()
    print(f"Part One: {p1_ans}")

    p2_ans = part_two()
    print(f"Part Two: {p2_ans}")
