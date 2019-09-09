

def sum10(given, a, b):
    lookup = dict()
    for item in a:
        if item in lookup:
            lookup[sum(item)].append(item)
        else:
            lookup[sum(item)] = [item]
    
    for item in b:
        remain = given - sum(item)
        if remain in lookup:
            if len(lookup[remain]) > 0:
                the_other = lookup[remain][-1]
                del lookup[remain][-1]
                yield the_other + item

def make_tuple(a,b):
    for a_item in a:
        for b_item in b:
            yield (a_item, b_item)


def four_inputs(data):
    if len(data) == 4:
        one = make_tuple(data[0], data[1])
        two = make_tuple(data[2], data[3])

        for item in sum10(10, one, two):
            print(item)

def main():
    data = [
        [1, 3, -4, 6],
        [4, -5, 2, -3],
        [-1, 3, 5, 4],
        [2, 5, 6, 7]
    ]
    four_inputs(data)

if __name__ == "__main__":
    main()