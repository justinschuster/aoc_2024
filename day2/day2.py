def readInput():
    out = []
    with open('input', 'r') as file: 
        for line in file:
            split_line = line.strip().split(' ')
            out.append(split_line)
    return out

def part_one():
    out = 0
    reports = readInput()
    for report in reports:
        safe = True
        increasing = None
        n = len(report)
        for i in range(1, n):
            diff = int(report[i]) - int(report[i-1]) 
            if 0 < diff and increasing != False:
                if increasing == None:
                    increasing = True
                if (diff < 1) or (3 < diff):
                    safe = False
            elif diff < 0 and increasing != True:
                if increasing == None:
                    increasing = False
                if (-1 < diff) or (diff < -3):
                    safe = False
            else:
                safe = False
        if safe:
            out += 1

    return out

if __name__ == '__main__':
    p1_ans = part_one()
    print(f"Part One: {p1_ans}")
