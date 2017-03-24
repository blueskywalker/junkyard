import hwatoo
import random
from collections import defaultdict


class CardScoringBoard:

    def __init__(self):
        self.score = 0
        self.cards = {20: set(), 10: set(), 5: set(), 1: set() }
        self.numOfGo = 0

    def add(self, card):
        self.cards[card.value].add(card)
        self.calc_score()

    def calc_score(self):
        self.score = self.numOfGo
        self.score += self.pee_score()
        self.score += self.ribon_score()
        self.score += self.ten_score()
        self.score += self.gwang_score()

    def pee_score(self):
        peelist = set([c.id for c in self.cards[1]])
        double = peelist & hwatoo.double_pee
        n = len(peelist) + len(double)

        if n < 10:
            return 0

        return n - 9

    def is_dan(self, danlist):
        data = set([c.id for c in self.cards[5]])
        hongdan = data & danlist
        if len(hongdan) == 3:
            return True
        else:
            return False

    def is_hongdan(self):
        return self.is_dan(hwatoo.hong_dan)

    def is_chungdan(self):
        return self.is_dan(hwatoo.chung_dan)

    def is_chodan(self):
        return self.is_dan(hwatoo.cho_dan)

    def ribon_score(self):
        n = 0
        if self.is_hongdan():
            n += 3
        if self.is_chungdan():
            n += 3
        if self.is_chodan():
            n += 3
        size = len(self.cards[5])
        if size > 4:
            n += size - 4
        return n

    def is_godori(self):
        data = set([c.id for c in self.cards[10]])
        godori = data & hwatoo.godori
        if len(godori) == 3:
            return True
        return False

    def ten_score(self):
        n = 0
        if self.is_godori():
            n += 5

        size = len(self.cards[10])
        if size > 4:
            n += size - 4
        return n

    def gwang_score(self):

        data = set([c.id for c in self.cards[20]])
        size = len(data)
        n = 0
        if size > 2:
            n = size

        if n == 3 and 45 in data:
            n = 2

        return n

    def __str__(self):
        out = []
        out.append("SCORE : %d with GO (%d) " % (self.score, self.numOfGo))
        out.append("GWANG : " + str(map(str, self.cards[20])))
        out.append("TEN : " + str(map(str, self.cards[10])))
        out.append("RIBON : " + str(map(str, self.cards[5])))
        out.append("PEE : " + str(map(str, self.cards[1])))
        return "\n".join(out)


class Player:

    def __init__(self):
        self.holding = dict()
        self.scoring = CardScoringBoard()

    def reset(self):
        self.__init__()

    def assign(self, cards):
        for c in cards:
            self.holding[c.id] = c

    def collect(self, cards):
        for card in cards:
            self.scoring.add(card)

    def str_holding(self):
        return ",".join(map(repr,sorted(self.holding.values())))

    def __str__(self):
        return '\n'.join([str(self.scoring), self.str_holding()])

    def play(self):
        while True:
            select = input("select number : ")
            if select in self.holding:
                print self.holding[select]
                break
        return self.holding.pop(select, None)


class ComputerPlayer(Player):

    def __str__(self):
        return str(self.scoring)

    def paly(self):
        pass


class GameFloor:

    def __init__(self, player1, player2):
        self.cards = []
        self.floor = defaultdict(dict)
        self.tmp_holding = defaultdict(dict)
        self.player1 = player1
        self.player2 = player2

    def shuffle_and_distribute(self):
        while True:
            self.cards = hwatoo.hwa_too[:]
            random.shuffle(self.cards)
            for _ in range(2):
                self.player1.assign([self.cards.pop() for _ in range(5)])
                self.player2.assign([self.cards.pop() for _ in range(5)])
                for c in [self.cards.pop() for _ in range(4)]:
                    self.floor[c.month][c.id] = c

            if 4 in [len(v) for v in self.floor.values()]:
                continue

            break

    def playing(self, player, card):
        month_set = self.floor[card.month]
        def nothing():
            self.tmp_holding[card.month][card.id] = card

        def match_one():
            self.tmp_holding[card.month][card.id] = card
            target = list(month_set.values())[0]
            self.tmp_holding[card.month][target.id] = target

        def match_two():
            if isinstance(player, ComputerPlayer):
                pass
            else:
                print ','.join(map(repr,month_set.values()))
                while True:
                    select = input("select one of these : ")
                    if select in [c.id for c in month_set]:
                        break
                self.tmp_holding[card.month][card.id] = card
                self.tmp_holding[card.month][select] = month_set.pop(select)

        def match_three():
            for id in month_set:
                self.tmp_holding[card.month][id] = month_set.pop(id)
            self.tmp_holding[card.month][card.id] = card
            # todo : bring pee from the other player

        switch = {0: nothing, 1: match_one, 2: match_two, 3: match_three}

        switch[len(month_set)]()
        self.flip_over(player)

    def flip_over(self, player):
        card = self.cards.pop()
        print card
        month_set = self.floor[card.month]

        def nothing():
            matching_set = self.tmp_holding[card.month]
            if len(matching_set) == 0:
                self.floor[card.month][card.id] = card
            elif len(matching_set) == 1:
                # kiss
                # todo : bring one "pee" from other player
                self.tmp_holding[card.month][card.id] = card
                print "kiss"
            elif len(matching_set) == 2:
                # diarrhea
                self.floor[card.month][card.id] = card
                for key in matching_set:
                    self.floor[card.month][key] = matching_set.pop(key)
                print 'diarrhea'

        def match_one():
            self.tmp_holding[card.month][card.id] = card
            target = list(month_set.values())[0]
            self.tmp_holding[card.month][target.id] = target

        def match_two():
            if isinstance(player, ComputerPlayer):
                pass
            else:
                print ','.join(map(repr,month_set.values()))
                while True:
                    select = input("select one of these : ")
                    if select in [c for c in month_set]:
                        break
                self.tmp_holding[card.month][card.id] = card
                self.tmp_holding[card.month][select] = month_set.pop(select)

        def match_three():
            for id in month_set:
                self.tmp_holding[card.month][id] = month_set.pop(id)
            self.tmp_holding[card.month][card.id] = card
            # todo : bring pee from the other player

        switch = { 0 : nothing, 1 : match_one, 2 : match_two, 3 : match_three}
        switch[len(month_set)]()

    def play(self, player, card):
        self.playing(player,card)
        for month in self.tmp_holding:
            player.collect(self.tmp_holding[month].values())

        self.tmp_holding = defaultdict(dict)

    def __str__(self):
        return str(map(str, reduce(list.__add__, [m.values() for m in self.floor.values()])))


class TwoPlayerGoStopGame:

    def __init__(self):
        self.player1 = Player()
        self.player2 = ComputerPlayer()
        self.floor = GameFloor(self.player1, self.player2)
        self.floor.shuffle_and_distribute()

    def play(self):
        while True:
            print self
            card = self.player1.play()
            self.floor.play(self.player1, card)
            print self
            self.player2.play()
            if len(self.cards) == 0:
                break

    def __str__(self):
        out = []
        out.append(
            '========================================================================')
        out.append(str(self.player2))
        out.append('\n')
        out.append(str(self.floor))
        out.append('\n')
        out.append(str(self.player1))
        return '\n'.join(out)

game = TwoPlayerGoStopGame()
game.play()
