def powerset(data):
    if len(data) == 0:
        return [[]]
    pivot = data[0]
    results = powerset(data[1:])
    new_results= results.copy()
    for item in results:
        new_results.append([pivot] + item)
    return new_results

data = ['a', 'b', 'c']

print(list(filter(lambda x: len(x) == 2,powerset(data))))
