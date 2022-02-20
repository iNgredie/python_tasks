"""
Итак, новая задача для всех желающих попробовать свои силы, в этот раз попроще (Никита жаловался).
Реализовать функцию, которая принимает на вход список из 5 целых положительных чисел и возвращает название комбинации в покере:
* если одинаковы 5, то вернуть "Impossible", иначе
* если одинаковы 4, то вернуть "Four of a Kind", иначе
* если одинаковы 3 и 2 ([1,1,3,3,3]), то вернуть "Full House", иначе
* если есть 5 последовательных ([1,2,3,4,5]), то вернуть "Straight", иначе
* если одинаковы 3, то вернуть "Three of a Kind", иначе
* если одинаковы 2 и 2, то вернуть "Two Pairs", иначе
* если одинаковы 2, то вернуть "One Pair", иначе
* вернуть "Nothing".
сигнатура def check_combination(cards: list) -> str:
нужно только дописать код в функции, не нужно ничего лишнего, импорт чего-либо запрещен (разве что рандом для проверки)
"""
from typing import List


def check_combination(cards: List[int]) -> str:
    options = {
        1: 'Impossible',
        2: {
            0: 'Full House',
            1: 'Four of a Kind',
        },
        3: {
            1: 'Two Pairs',
            2: 'Three of a Kind',
        },
        4: 'One Pair',
        5: {
            0: 'Nothing',
            1: 'Straight',
        },
    }
    if len(cards) == 5:
        unique = len(set(cards))
        if unique in [2, 3]:
            number_unique_cards = len([x for x in cards if cards.count(x) == 1])
            return options[unique][number_unique_cards]
        elif unique == 5:
            its_straight = int(list(range(min(cards), max(cards) + 1)) == sorted(cards))
            return options[unique][its_straight]
        return options[unique]

    return options[5][0]


assert check_combination([1, 3, 3, 3, 3]) == 'Four of a Kind'
assert check_combination([1, 1, 3, 3, 3]) == 'Full House'
assert check_combination([1, 2, 3, 4, 5]) == 'Straight'
assert check_combination([1, 2, 3, 3, 3]) == 'Three of a Kind'
assert check_combination([1, 1, 3, 3, 2]) == 'Two Pairs'
assert check_combination([1, 1, 4, 5, 2]) == 'One Pair'
assert check_combination([1, 3, 2, 4, 6]) == 'Nothing'
assert check_combination([1, 3, 2, 4]) == 'Nothing'

