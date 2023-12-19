from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def main():
    data = get_data().split('\n')
    # data = open('test').read().split('\n')

    answer = 0
    rules_dict = defaultdict(list)
    rules_found = False
    for line in data:
        if not line:
            rules_found = True
            continue

        if not rules_found:
            rule_name, rules = line.removesuffix('}').split('{')
            for rule in rules.split(','):
                if ':' in rule:
                    parts = rule.split(':')
                    rules_dict[rule_name].append((parts[0], parts[1]))

                else:
                    rules_dict[rule_name].append(rule)

        else:
            parts = line.removesuffix('}').removeprefix('{').split(',')
            numbers = {'x': int(parts[0].split('=')[1]),
                       'm': int(parts[1].split('=')[1]),
                       'a': int(parts[2].split('=')[1]),
                       's': int(parts[3].split('=')[1])}

            current_rule = 'in'
            exit_loop = False
            print(numbers)
            while True:
                if exit_loop:
                    break

                if current_rule == 'A':
                    answer += sum(numbers.values())
                    break

                if current_rule == 'R':
                    break

                for rule in rules_dict[current_rule]:
                    print(rule)
                    if not isinstance(rule, tuple):
                        print(rule)
                        if rule == 'R':
                            exit_loop = True
                            break

                        elif rule == 'A':
                            answer += sum(numbers.values())
                            exit_loop = True
                            break

                        else:
                            current_rule = rule
                            break

                    else:
                        match rule[0][1]:
                            case '>':
                                if numbers[rule[0][0]] > int(rule[0].split('>')[-1]):
                                    current_rule = rule[1]
                                    break
                            case '<':
                                if numbers[rule[0][0]] < int(rule[0].split('<')[-1]):
                                    current_rule = rule[1]
                                    break
                            case _:
                                if numbers[rule[0][0]] == int(rule[0].split('=')[-1]):
                                    current_rule = rule[1]
                                    break

    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
