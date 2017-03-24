class Card:

    def __init__(self,id,month,value,desc):
        self.id = id
        self.month = month
        self.value = value
        self.desc = desc

    def __repr__(self):
        return "%s [%d]" % (self.desc, self.id)

    def __str__(self):
        return self.desc

    def __cmp__(self, other):
        return self.id - other.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id

hwa_too = [
    Card(1, 1, 20, '1 gwang'),      # 1 gwang
    Card(2, 1, 5, '1 hong-dan'),    # 1 hong-dan
    Card(3, 1, 1, '1 pee'),         # 1 pee
    Card(4, 1, 1, '1 pee'),         # 1 pee
    Card(5, 2, 10, '2 bird'),       # 2 bird
    Card(6, 2, 5, '2 hong-dan'),    # 2 hong-dan
    Card(7, 2, 1, '2 pee'),         # 2 pee
    Card(8, 2, 1, '2 pee'),         # 2 pee
    Card(9, 3, 20, '3 gwang'),      # 3 gwang
    Card(10, 3, 5, '3 hong-dan'),   # 3 hong-dan
    Card(11, 3, 1, '3 pee'),        # 3 pee
    Card(12, 3, 1, '3 pee'),        # 3 pee
    Card(13, 4, 10, '4 bird'),      # 4 bird
    Card(14, 4, 5, '4 cho-dan'),    # 4 cho-dan
    Card(15, 4, 1, '4 pee'),        # 4 pee
    Card(16, 4, 1, '4 pee'),        # 4 pee
    Card(17, 5, 10, '5 nan'),       # 5 nan tree
    Card(18, 5, 5, '5 cho-dan'),    # 5 cho-dan
    Card(19, 5, 1, '5 pee'),        # 5 pee
    Card(20, 5, 1, '5 pee'),        # 5 pee
    Card(21, 6, 10, '6 mo-ran'),    # 6 mo-ran
    Card(22, 6, 5, '6 chung-dan'),  # 6 chung-dan
    Card(23, 6, 1, '6 pee'),        # 6 pee
    Card(24, 6, 1, '6 pee'),        # 6 pee
    Card(25, 7, 10, '7 pig'),       # 7 pig
    Card(26, 7, 5, '7 cho-dan'),    # 7 cho-dan
    Card(27, 7, 1, '7 pee'),        # 7 pee
    Card(28, 7, 1, '7 pee'),        # 7 pee
    Card(29, 8, 20, '8 gwang'),     # 8 gwang
    Card(30, 8, 10, '8 bird'),      # 8 bird
    Card(31, 8, 1, '8 pee'),        # 8 pee
    Card(32, 8, 1, '8 pee'),        # 8 pee
    Card(33, 9, 10, '9 kookhwa'),   # 9 kookhwa (pee)
    Card(34, 9, 5, '9 chung-dan'),  # 9 chung-dan
    Card(35, 9, 1, '9 pee'),        # 9 pee
    Card(36, 9, 1, '9 pee'),        # 9 pee
    Card(37, 10, 10, '10 deer'),    # 10 deer
    Card(38, 10, 5, '10 chung-dan'),     # 10 chung-dan
    Card(39, 10, 1, '10 pee'),           # 10 pee
    Card(40, 10, 1, '10 pee'),           # 10 pee
    Card(41, 11, 20, '11 crap gwang'),      # crap gwang
    Card(42, 11, 1, '11 crap double pee'),  # 11 double pee
    Card(43, 11, 1, '11 pee'),           # 11 pee
    Card(44, 11, 1, '11 pee'),           # 11 pee
    Card(45, 12, 20, '12 rain gwang'),      # 12 rain gwang
    Card(46, 12, 10, '12 rain bird'),       # 12 rain bird
    Card(47, 12, 5, '12 rain-dan'),         # 12 rain-dan
    Card(48, 12, 1, '12 rain double pee')   # 12 double pee
]

double_pee = {33, 42, 48}
hong_dan = {2, 6, 10}
chung_dan = {22, 34, 38}
cho_dan = {14, 18, 26}
godori = {5, 13, 30}
