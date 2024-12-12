def read_input(input='input.txt'):
    targets = []
    equations = []

    lines = open(input, 'r').readlines()

    for line in lines:
        target, equation = line.replace('\n', '').split(':')

        target = int(target)
        equation = [int(x) for x in equation.strip().split()]

        targets.append(target)
        equations.append(equation)

    return targets, equations

def binary_traversal(root, values, target):
    if values == [] and root == target:
        return True

    if values == []:
        return False

    new_values = values.copy()
    next_value = new_values.pop(0)

    add_value = root + next_value
    mul_value = root * next_value

    return any([
        binary_traversal(add_value, new_values, target),
        binary_traversal(mul_value, new_values, target)
    ])

def ternary_traversal(root, values, target):
    if values == [] and root == target:
        return True

    if values == []:
        return False

    new_values = values.copy()
    next_value = new_values.pop(0)

    add_value = root + next_value
    mul_value = root * next_value
    con_value = int(str(root) + str(next_value))

    return any([
        ternary_traversal(add_value, new_values, target),
        ternary_traversal(mul_value, new_values, target),
        ternary_traversal(con_value, new_values, target)
    ])

def solve(input):
    targets, equations = input

    binary_count = 0
    ternary_count = 0
    for i, target in enumerate(targets):
        curr = equations[i].pop(0)
        if binary_traversal(curr, equations[i], target):
            binary_count += target

        if ternary_traversal(curr, equations[i], target):
            ternary_count += target

    return binary_count, ternary_count

if __name__ == "__main__":
    input = read_input('test_input.txt')

    answer  = solve(input)
    print(answer)
