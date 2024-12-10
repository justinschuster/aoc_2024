def read_input():
    ordering_rules = []
    updates = []
    seen_break = False
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line == '\n':
                seen_break = True
            elif seen_break is False:
                ordering_rules.append(line.strip())
            elif seen_break:
                curr_line = line.strip()
                if curr_line != '':
                    updates.append(line.strip().split(','))
    return ordering_rules, updates

def parse_ordering_rules(ordering_rules):
    rules_map = {}
    for line in ordering_rules:
        curr_line = line.split('|')
        first = curr_line[0]
        second = curr_line[1]
        if first not in rules_map:
            rules_map[first] = [second]
        else:
            rules_map[first].append(second)
    return rules_map

def make_correct(updates, rules_map):
    corrected = []
    for update in updates:
        new_update = []
        for i in range(len(update)):
            curr_page = update[i]
            if curr_page in rules_map:
                for rule in rules_map[curr_page]:
                    if rule not in update[:i]:
                        
    return corrected

def part_one(updates, rules_map):
    correct = []
    for update in updates:
        correct_update = True
        for i in range(len(update)):
            curr_page = update[i]
            if curr_page in rules_map:
                for rule in rules_map[curr_page]:
                    if rule in update[:i]: 
                        correct_update = False
        if correct_update:
            correct.append(update)
 
    correct_sum = 0
    for update in correct:
        middle_index = len(update) // 2
        correct_sum += int(update[middle_index])
    return correct_sum

def part_two(updates, rules_map):
    correct = []
    incorrect = []
    for update in updates:
        correct_update = True
        for i in range(len(update)):
            curr_page = update[i]
            if curr_page in rules_map:
                for rule in rules_map[curr_page]:
                    if rule in update[:i]: 
                        correct_update = False
        if correct_update:
            correct.append(update)
        else:
            incorrect.append(update)
 
    correct_sum = 0
    for update in correct:
        middle_index = len(update) // 2
        correct_sum += int(update[middle_index])
    return correct_sum

def main():
    ordering_rules, updates = read_input()
    rules_map = parse_ordering_rules(ordering_rules)

    # part one 
    correct = part_one(updates, rules_map)
    print(correct)

if __name__ == "__main__":
    main()

