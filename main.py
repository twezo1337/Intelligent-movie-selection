import json
import random
from json import load
from json import dump
from random import randint

def suggestive_questions(rules):
    questions_list = ['Вам бы хотелось посмотреть', 'Вы предпочитаете', 'Вам нравятся',
                      'Вы любите', 'Вас интересуют']
    user_answer = ''
    i = 0
    j = 0
    for rule in rules:
        if i == 1:
            continue
        elif i == 0:
            user_answer = input(f'{questions_list[random.randint(0, 4)]} {rule}? ')
            if len(rules) == 1:
                return rule
            elif len(rules) == 2:
                if user_answer == 'да':
                    i = 1
                    return rule
                elif user_answer == 'нет':
                    if j == 0:
                        i = 1
                        return list(rules.keys())[j + 1]
                    elif j == 1:
                        i = 1
                        return list(rules.keys())[j - 1]
            elif len(rules) > 2:
                if user_answer == 'да':
                    i = 1
                    return rule
                elif user_answer == 'нет':
                    if len(rules) - j == 1:
                        i = 1
                        return list(rules.keys())[j + 1]
    j += 1


def movie_selection(genres_base):
    result = []
    full_genres = []
    for genre in genres_base:
        full_genres.append(genre)
    user_answer = input(f'Выберите предпочитаемые жанры(через запятую) {full_genres}: ')

    user_genres = user_answer.split(',')

    temp = []
    films = []
    for genre in genres_base:
        for film in genres_base[genre]:
            temp.append(film)
    films = list(set(temp))

    count = 0
    films_count = {}
    for film in films:
        if len(user_genres) == 1:
            for genre in user_genres:
                if list(genres_base[genre]).__contains__(film):
                    result.append(film)
        elif len(user_genres) > 1:
            for genre in user_genres:
                if list(genres_base[genre]).__contains__(film):
                    count += 1
            films_count[f'{film}'] = count
        count = 0

    if len(user_genres) != 1:
        genres_len = len(user_genres)
        i = 1
        while i:
            for film in films_count:
                if films_count[film] == genres_len:
                    result.append(film)
            if bool(result):
                i = 0
            else:
                genres_len -= 1

    return result

def create_rule(rules):
    for rule in rules:
        print(rule)
    admin_answer = input('Выберите правило или введите новое: ')

    return admin_answer
def menu():
    def first():
        while True:
            ch = input('1.Начать поиск\n2.Назад\n')
            if ch == '2':
                return
            if ch == '1':
                film_genres_check = ['Комедия', 'Драма', 'Ужасы', 'Фэнтези', 'Триллер',
                                     'Приключения', 'Криминал', 'Мелодрама', 'Биография', 'Семейный',
                                     'История', 'Детектив', 'Боевик', 'Документальный', 'Военный']
                rules = {}
                with open('rules.json', encoding="utf-8") as rules_file:
                    rules = load(rules_file)

                film_base = rules
                start = 1

                while start == 1:
                    rule = suggestive_questions(film_base)
                    film_base = film_base[rule]
                    for genre_check in film_genres_check:
                        if list(film_base.keys()).__contains__(genre_check):
                            start = 0

                print(f'Скорее всего вам подойдут эти фильмы: {movie_selection(film_base)}')

    def second():
        while True:
            ch = input('1.Добавить правила поиска\n2.Назад\n')
            if ch == '2':
                return
            if ch == '1':
                film_genres_check = ['Комедия', 'Драма', 'Ужасы', 'Фэнтези', 'Триллер',
                                     'Приключения', 'Криминал', 'Мелодрама', 'Биография', 'Семейный',
                                     'История', 'Детектив', 'Боевик', 'Документальный', 'Военный']

                with open('rules.json', encoding='utf-8') as old_json:
                    data = json.load(old_json)

                rules_base = data
                start = 1
                while start == 1:
                    rule = create_rule(rules_base)
                    if rule in rules_base:
                        rules_base = rules_base[rule]
                    else:
                        rules_base[rule] = {}
                    for genre_check in film_genres_check:
                        if list(rules_base.keys()).__contains__(genre_check):
                            start = 0

            print(rules_base)

    while True:
        ch = input("1.Пользователь\n2.Администратор\n3.Выход\n")
        if ch == '3':
            return
        if ch == '1':
            first()
        elif ch == '2':
            second()

menu()
