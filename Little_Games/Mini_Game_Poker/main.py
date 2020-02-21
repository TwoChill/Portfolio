import base as clss
import time

nr_of_cards = 5
clss.sys_clear()

cards = clss.Cards()
dealer = clss.Dealer()

# Create nr_of_cards
ascii_cards, rand_comb_cards = cards.create_cards(nr_of_cards)

# dealer.deal_cards(ascii_cards)


result = []

for next_down in range(9):
    for next_side in range(1):
        result.append('  '.join(ascii_cards[next_side][next_down]))

t = time.time()


for card in result:

    if '║Joker    ║  ║J    ║' or '║    Joker║  ║    J║' in card:
        card = card.replace('║Joker    ║  ║J    ║', '║Joker    ║  ║J        ║')
        card = card.replace('║    Joker║  ║    J║', '║    Joker║  ║        J║')

    if '║Joker    ║  ║K        ║  ║Q    ║' or '║    Joker║  ║        K║  ║    Q║' in card:
        card = card.replace('║Joker    ║  ║K        ║  ║Q    ║',
                            '║Joker    ║  ║K        ║  ║Q        ║')
        card = card.replace('║    Joker║  ║        K║  ║    Q║',
                            '║    Joker║  ║        K║  ║        Q║')

    if '║Joker    ║  ║Q    ║' or '║    Joker║  ║    Q║' in card:
        card = card.replace('║Joker    ║  ║Q    ║', '║Joker    ║  ║Q        ║')
        card = card.replace('║    Joker║  ║    Q║', '║    Joker║  ║        Q║')

    if '║Q        ║  ║Q    ║' or '║    Q    ║  ║    Q║' in card:
        card = card.replace('║Q        ║  ║Q    ║', '║Q        ║  ║Q        ║')
        card = card.replace('║        Q║  ║    Q║', '║    Q    ║  ║        Q║')

    if '║Q       ║  ║10       ║' or '║       Q║  ║       10║' in card:
        card = card.replace('║Q       ║  ║10       ║',
                            '║Q        ║  ║10       ║')
        card = card.replace('║       Q║  ║       10║',
                            '║        Q║  ║       10║')

    if '║Joker    ║  ║K    ║' or '║    Joker║  ║    K║'in card:
        card = card.replace('║Joker    ║  ║K    ║', '║Joker    ║  ║K        ║')
        card = card.replace('║    Joker║  ║    K║', '║    Joker║  ║        K║')

    if '║Joker    ║  ║K        ║  ║K    ║' or '║    Joker║  ║        K║  ║    K║'in card:
        card = card.replace('║Joker    ║  ║K        ║  ║K    ║',
                            '║Joker    ║  ║K        ║  ║K    ║    ')
        card = card.replace('║    Joker║  ║        K║  ║    K║',
                            '║    Joker║  ║        K║  ║    K║    ')

    if '║K    ║  ║K    ║  ║K    ║' or 'K║  ║    K║  ║    K║         'in card:
        card = card.replace('K    ║  ║K    ║  ║K    ║',
                            'K      ║  ║K       ║  ║K       ║')
        card = card.replace('K║  ║    K║  ║    K║         ',
                            'K║  ║        K║  ║        K║')

    if '║A       ║  ║2        ║' or '║       A║  ║        2║'in card:
        card = card.replace('║A       ║  ║2        ║',
                            '║A        ║  ║2        ║')
        card = card.replace('║       A║  ║        2║',
                            '║        A║  ║        2║')

    if '║10       ║  ║A       ║' or '║       10║  ║       A║'in card:
        card = card.replace('║10       ║  ║A       ║',
                            '║10       ║  ║A        ║')
        card = card.replace('║       10║  ║       A║',
                            '║       10║  ║        A║')

    if '║A    ║  ║6        ║' or '║    A║  ║        6║'in card:
        card = card.replace('║A    ║  ║6        ║', '║A        ║  ║6        ║')
        card = card.replace('║    A║  ║        6║', '║        A║  ║        6║')

    if '║J       ║  ║2        ║' or '║       J║  ║        2║'in card:
        card = card.replace('║J       ║  ║2        ║',
                            '║J        ║  ║2        ║')
        card = card.replace('║       J║  ║        2║',
                            '║        J║  ║        2║')

    print(card)
print(((time.time() - t) % 60))

# for card in ascii_cards[((nr_of_cards)-1)][next_down]:
#     print(card)


# for k, v in ascii_cards.items():
#     print(k, v)
# print('\n')
# print(ascii_cards[1][1])
# print('\n')
# print(ascii_cards[1][1])
# print('\n')
# print(ascii_cards[1][1][0] + ascii_cards[1][1][1]+ ascii_cards[1][1][2]+ ascii_cards[1][1][3])
# print('\n')
