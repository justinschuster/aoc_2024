def get_input(input='input.txt'):
    targets = []
    parts = []
    with open(input, 'r') as file:
        for line in file:
            before, after = line.strip().split(':')
            targets.append(int(before))
            parts.append([int(num) for num in after.strip().split()])
    return targets, parts

def try_both_rec(target, parts, prev, idx):
    if idx == len(parts):
        return False

    new_sum = prev + parts[idx]
    new_prod = prev * parts[idx]
    if new_prod == target or new_sum == target:
        return True
    return any([
        try_both_rec(target, parts, new_prod, idx+1),
        try_both_rec(target, parts, new_sum, idx+1)
    ])

def solve(targets, parts):
    valid = []
    for i, target in enumerate(targets):
        curr = parts[i]
        if try_both_rec(target, curr, curr[0], 1):
            valid.append(target)
    return sum(valid)

if __name__ == "__main__":
    targets, parts = get_input()

    ans1 = solve(targets, parts)
    print(ans1)
