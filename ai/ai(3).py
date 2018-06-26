import re
import itertools
from collections import Counter
from core import hand_rank, hand_max
from robot_cards_check import data_map

value_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
             '2': 2}

key_map = {v: k for k, v in value_map.items()}


class AI:
    data_pre_flop = "data_pre_flop"
    data_flop = "data_flop"
    data_turn = "data_turn"
    data_river = "data_river"

    def __init__(self, index, small_blinds, pot, call, left, hand_cards, public_cards):
        self.index = index
        self.hand_cards = hand_cards
        self.public_cards = public_cards
        self.all_cards = self.public_cards + self.hand_cards
        self.content = {
            "BB": small_blinds * 2,
            "Allin": left,
            "Chips": left,
            "Pot": pot,
            "Fold": -1,
            "Call": call,
            "Raise": 0,
            "Check&Fold": 0 if call == 0 else -1,
            "Check&Call": 0 if call == 0 else call,
            "Bet": 0,
        }

    def parse(self):
        counter = itertools.count(1)
        index = str(next(counter))
        stage_index = {0: 0, 3: 1, 4: 2, 5: 3}[len(self.public_cards)]
        while data_map.get(self.data_pre_flop + index):
            data_stage = (
                data_map[self.data_pre_flop + index],
                data_map[self.data_flop + index],
                data_map[self.data_turn + index],
                data_map[self.data_river + index]
            )
            stage = data_stage[stage_index]
            for rule in sorted(stage.values(), key=lambda x: x["id"]):
                move = self._parse_rule(rule)
                print('here:%s' % rule["id"])
                if move is not None:
                    return move
            index = str(next(counter))
        return 0

    def _parse_rule(self, rule):
        print(self.parse_hand_cards_type(rule["handCards"]),
              self.parse_public_cards_type(rule["publicCards"]),
              self.parse_cards_type(rule["cardType"]),
              self.parse_condition(rule["leftChips"]),
              self.parse_condition(rule["callChips%d" % min(self.index, 2)]))
        if self.parse_hand_cards_type(rule["handCards"]) and \
                self.parse_public_cards_type(rule["publicCards"]) and \
                self.parse_cards_type(rule["cardType"]) and \
                self.parse_condition(rule["leftChips"]) and \
                self.parse_condition(rule["callChips%d" % min(self.index, 2)]):
            return self.parse_operation(rule["operation%d" % min(self.index, 2)])
        return None

    def _parse_amount(self, word):
        print(word)
        if not word:
            return 0
        times = 1
        r = re.match("(\d+(\.\d+)?)", word)
        if r:
            times = float(r.group())
        w = re.search("([a-zA-Z]&?)+", word).group()
        print(times, self.content[w])
        return int(times * self.content[w])

    def parse_operation(self, operation):
        return sum([self._parse_amount(s) for s in operation.split(" ")])

    def parse_condition(self, condition):
        for k, v in self.content.items():
            condition = condition.replace(k, str(v))
        return True if condition == "" else eval(condition)

    # hand cards
    def parse_hand_cards_type(self, desc):
        func = getattr(self, "hand_cards__" + desc, None)
        if not func:
            return self.hand_cards__exact(desc)
        return func()

    def hand_cards__(self):
        return True

    def hand_cards__pairs(self):
        return self.hand_cards[0][0] == self.hand_cards[1][0]

    def hand_cards__same_color(self):
        return self.hand_cards[0][1] == self.hand_cards[1][1]

    def hand_cards__adjoin(self):
        return (value_map[self.hand_cards[0][0]] - value_map[self.hand_cards[1][0]]) in (-1, 1)

    def hand_cards__exact(self, desc):
        cards_list = desc.split(" ")
        for cards in cards_list:
            if self._hand_cards_judge(cards):
                return True
        return False

    def _hand_cards_judge(self, cards):
        ccc = [cs[0] for cs in self.hand_cards]
        cc = cards[:-1]
        if cards[-1].islower():
            t = cards[-1]
            if len(cc) == 1:
                if cc not in ccc:
                    return False
                if t == "s":
                    return self.hand_cards[0][1] == self.hand_cards[1][1]
                elif t == "o":
                    return self.hand_cards[0][1] != self.hand_cards[1][1]
                else:
                    raise Exception()
            else:
                if set(cc) != set(ccc):
                    return False
                if t == "s":
                    return self.hand_cards[0][1] == self.hand_cards[1][1]
                elif t == "o":
                    return self.hand_cards[0][1] != self.hand_cards[1][1]
        else:
            return set([cs[0] for cs in cards]) == set(ccc)

    ########

    # public cards
    def parse_public_cards_type(self, desc):
        return getattr(self, "public_cards__" + desc)()

    def public_cards__(self):
        return True

    def public_cards__same_color3(self):
        return 3 in Counter([card[1] for card in self.public_cards]).values()

    def public_cards__same_color2(self):
        return 2 in Counter([card[1] for card in self.public_cards]).values()

    def public_cards__pairs1(self):
        return Counter(Counter([card[0] for card in self.public_cards]).values()).get(2) == 1

    def public_cards__pairs2(self):
        return Counter(Counter([card[0] for card in self.public_cards]).values()).get(2) == 2

    def public_cards__three_kind(self):
        return 3 in Counter([card[0] for card in self.public_cards]).values()

    def public_cards__straight(self):
        return hand_rank(self.public_cards)[0] == 4

    def public_cards__flush(self):
        return hand_rank(self.public_cards)[0] == 5

    def public_cards__full_house(self):
        return hand_rank(self.public_cards)[0] == 6

    def public_cards__four_kind(self):
        return hand_rank(self.public_cards)[0] == 7

    def public_cards__straight_flush(self):
        ranks = hand_rank(self.public_cards)
        return (9 if ranks == (8, (14, 13, 12, 11, 10)) else ranks[0]) == 8

    def public_cards__royal_flush(self):
        return hand_rank(self.public_cards) == (8, (14, 13, 12, 11, 10))

    ###

    # cards_type: <, <=, ==, >=, >
    def parse_cards_type(self, desc):
        if not desc:
            return True
        op = re.search("([a-zA-Z0-9]_?)+", desc).group()
        compare = desc.replace(op, "")
        return getattr(self, "cards__" + op)(compare)

    def _compare(self, compare, a, b):
        if compare == "<":
            return a < b
        elif compare == "<=":
            return a <= b
        elif compare == "=":
            return a == b
        elif compare == ">=":
            return a >= b
        elif compare == ">":
            return a > b

    def cards__top_pairs(self, compare):
        m = max([value_map[card[0]] for card in self.public_cards])
        t = hand_max(self.all_cards)
        return self._compare(compare, (t[0], t[1][0]), (1, m))

    def cards__super_pairs(self, compare):
        m = max([value_map[card[0]] for card in self.public_cards])
        if m + 1 > 14:
            return False
        t = hand_max(self.all_cards)
        return self._compare(compare, (t[0], t[1][0]), (1, m + 1))

    def cards__same_color1(self, compare):
        counter = Counter([card[1] for card in self.public_cards])
        c = None
        for k, v in counter.items():
            if v == 3:
                c = k
        return c is not None and c in [card[1] for card in self.hand_cards]

    def cards__same_color2(self, compare):
        counter = Counter([card[1] for card in self.public_cards])
        hand = [card[1] for card in self.hand_cards]
        if hand[0] != hand[1]:
            return False
        for k, v in counter.items():
            if v == 2 and k == hand[0]:
                return True
        return False

    def cards__straight_lack(self):
        if len(self.all_cards) not in (4, 5, 6):
            return None
        color = ["H", "D", "C", "S"]
        all_cards = [card[0] + color[i % len(color)] for i, card in enumerate(self.all_cards)]
        counter = 0
        for i in range(2, 15):
            if hand_max(all_cards + [key_map[i] + "H"])[0] in (4, 8, 9):
                counter += 1
        return counter

    def cards__straight_lack1(self, compare):
        return self.cards__straight_lack() == 1

    def cards__straight_lack2(self, compare):
        return self.cards__straight_lack() == 2

    def cards__same_color1_straight_lack2(self, compare):
        return self.cards__same_color1(compare) and self.cards__straight_lack2(compare)

    def cards__same_color2_straight_lack1(self, compare):
        return self.cards__same_color2(compare) and self.cards__straight_lack1(compare)

    def cards__same_color2_straight_lack2(self, compare):
        return self.cards__same_color2(compare) and self.cards__straight_lack2(compare)

    def cards__pairs1(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 1)

    def cards__pairs2(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 2)

    def cards__three_kind(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 3)

    def cards__straight(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 4)

    def cards__flush(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 5)

    def cards__full_house(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 6)

    def cards__four_kind(self, compare):
        return self._compare(compare, hand_max(self.all_cards)[0], 7)

    def cards__straight_flush(self, compare):
        ranks = hand_max(self.all_cards)
        return self._compare(compare, 9 if ranks == (8, (14, 13, 12, 11, 10)) else ranks[0], 8)

    def cards__royal_flush(self, compare):
        return self._compare(compare, hand_max(self.all_cards), (8, (14, 13, 12, 11, 10)))

print(AI(0, 10, 1000, 20, 1900, ["5C", "7H"], ["9H", "TH", "JH", "QH", "KH"]).parse())