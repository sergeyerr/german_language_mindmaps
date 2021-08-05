from os.path import exists, join, splitext
from os import listdir
from random import sample, randrange, shuffle
verb_folder = 'irregular verbs'

groups_dict = dict()

def parse_str(s: str):
    return [x.replace('"', '').lower() for x in list(filter(lambda x: len(x) > 0, s[:-1].split(',')))]

for p in listdir(verb_folder):
    groups_dict[splitext(p)[0]] = list()
    with open(join(verb_folder, p), 'r') as f:
        f.readline()
        for l in f.readlines():
            tmp = parse_str(l)
            if len(tmp) > 0:
                groups_dict[splitext(p)[0]].append(tmp)
print(groups_dict)

print('Выберите группы(можно через запятую):')
for i, k in enumerate(groups_dict.keys()):
    print(f'{i}:  {k}')
ans = [int(x.strip()) for x in input().split(',')]

selected_groups = [list(groups_dict.keys())[i] for i in ans]

print('Выбранны группы', *selected_groups, sep='\n')
print('-------------------------------------------')
difficulty = int(input("Выбери сложность от 1 до 3:"))


all_verbs = [x for y in [groups_dict[k] for k in selected_groups] for x in y]
shuffle(all_verbs)

ans = ''
correct_count = 0
all_count = 0
chosen_verb = 0
while ans != 'stop!':
    if difficulty != 3:
        exclude_forms = sample(list(range(4)), difficulty)
    else:
        exclude_forms = [1,2,3]
   # chosen_verb = randrange(len(all_verbs))

    forms = all_verbs[chosen_verb][:3]
    translation = all_verbs[chosen_verb][3]
    chosen_verb = (chosen_verb + 1) % len(all_verbs)
    forms_to_print = [('Translation: ', translation),
        ('Infinitiv: ', forms[0]), ('Präteritum: ', forms[1]), ('Partizip 2: ', forms[2])]
    for i in range(4):
        if i not in exclude_forms:
            print(f'{forms_to_print[i][0]:15s}', forms_to_print[i][1])
    for form in exclude_forms:
        print(f'{forms_to_print[form][0]:15s}', '?')
        ans = input()
        if ans == 'stop!':
            break
        all_count += 1
        ans = ans.strip().lower()
        if ans != forms_to_print[form][1]:
            print('WRONG!!!')
            print('correct was: ', forms_to_print[form][1])
        else:
            correct_count += 1
            print('correct, bro!')
    if ans == 'stop!':
        break
    print('-------------------------------------------')
print('-------------------------------------------')
print(f'|            your stats: {correct_count}/{all_count}              |')
print('-------------------------------------------')
