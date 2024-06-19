import csv
from json import dump

rules_dict = {}

with open('movies.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        name = row[0]
        genre = row[1]
        studio = row[2]
        year = row[7]

        if not year.isdigit() or not studio or not genre or not name:
            continue

        rule = f'Year = {year}'
        rules_dict[rule] = rules_dict.get(rule, []) + [name]

        rule = f'Genre = {genre}'
        rules_dict[rule] = rules_dict.get(rule, []) + [name]

        rule = f'Studio = {studio}'
        rules_dict[rule] = rules_dict.get(rule, []) + [name]

with open('rules.json', 'w', encoding='utf-8') as json_file:
    dump(rules_dict, json_file, ensure_ascii=False)




