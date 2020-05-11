# генератор карт  13 карт по 4 масти - 52 карты + 2 джокера
# 2, 3, 4, 5, 6, 7, 8, 9, 10, V, D, K, T

def cards_54_generator():
    cards_set = []
    cards_2_10 = [x for x in range(2,11)] # генерируем список карт от 2 до 10
    # создаем список карт одной масти от 2 до Туза, приведя цифры к строкам и добавив Валет, Даму, Короля, Туза
    cards_no_suit = list(map(str, cards_2_10)) + 'V D K T'.split()
    # масти
    suits = u'\u2660,\u2665,\u2663,\u2666'.split(',')
    for suit in suits:
        for card in cards_no_suit:
            card = f'{suit}{card}'
            cards_set.append(card)
    cards_set.append('JB')
    cards_set.append('JR')
    return cards_set

def cards_data_for_sql():
    '''
    generates 54 cards
    :return: tuple(id, card_name, card_value)
    '''
    data = []
    card_list = cards_54_generator()
    id = 0
    power = 1 # сила карты
    for card in card_list:
        id+=1

        if power == 14:
            power = 2
            row = (id, card, power)
            data.append(row)
            continue
        power+=1
        row = (id, card, power)
        data.append(row)
    return data





if __name__=='__main__':
    data = cards_data_for_sql()
    for row in data:
        print(row)