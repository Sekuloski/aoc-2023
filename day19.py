from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def process_rule(rule, rules_dict, current_path):
    if rule == 'A':
        return True, current_path

    if rule == 'R':
        return (False,)

    print(rule, rules_dict, current_path)
    if not isinstance(rule, tuple):
        new_path = current_path.copy()
        new_path.append(rule)
        new_rules = rules_dict[rule]
        for new_rule in new_rules:
            return process_rule(new_rule, rules_dict, new_path)

    # else:
    #     match rule[0][1]:
    #         case '>':
    #             if numbers[rule[0][0]] > int(rule[0].split('>')[-1]):
    #                 current_rule = rule[1]
    #                 break
    #         case '<':
    #             if numbers[rule[0][0]] < int(rule[0].split('<')[-1]):
    #                 current_rule = rule[1]
    #                 break
    #         case _:
    #             if numbers[rule[0][0]] == int(rule[0].split('=')[-1]):
    #                 current_rule = rule[1]
    #                 break
    return (False,)

def main():
    # data = get_data().split('\n')
    data = open('test').read().split('\n')

    answer = 0
    rules_dict = defaultdict(list)
    possible_scenarios = []
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

    for rule in rules_dict['in']:
        results = process_rule(rule, rules_dict, [])
        if results[0]:
            possible_scenarios.append(results[1])

                # for rule in rules_dict[current_rule]:
                #     print(rule)
                #

    print(answer)
    # submit(answer)


if __name__ == '__main__':
    main()
