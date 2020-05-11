from mnemo_functions.cards_generator import cards_54_generator, cards_data_for_sql

cards_list = cards_data_for_sql()

for card in cards_list:
    print(card[0], card[1], card[2])