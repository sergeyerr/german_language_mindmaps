from os.path import exists, join, splitext
from os import listdir
from random import sample, randrange
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

print('Выберите группы(через запятую, индексация с 0):', *groups_dict.keys(), sep='\n')
ans = [int(x.strip()) for x in input().split(',')]

selected_groups = [list(groups_dict.keys())[i] for i in ans]

print('Выбранны группы', *selected_groups, sep='\n')

all_verbs = [x for y in [groups_dict[k] for k in selected_groups] for x in y]
ans = ''
while ans != 'stop':
    exclude_form = sample(list(range(2)), 1)[0]
    chosen_verb = randrange(len(all_verbs))
    forms = all_verbs[chosen_verb][:3]
    translation = all_verbs[chosen_verb][3]
    forms_to_print = [('Infinitiv: ', forms[0]), ('Präteritum: ', forms[1]), ('Partizip 2: ', forms[2])]
    print('Translation: ', translation)
    for i in range(3):
        if i != exclude_form:
            print(forms_to_print[i][0], forms_to_print[i][1])
    print(forms_to_print[exclude_form][0], '?')
    ans = input()
    if ans == 'stop!':
        break
    ans = ans.strip().lower()
    if ans != forms_to_print[exclude_form][1]:
        print('WRONG!!!')
        print('correct was: ', forms_to_print[exclude_form][1])
    else:
        print('correct, bro!')
    print('-------------------------------------------')

