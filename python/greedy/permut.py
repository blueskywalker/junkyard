
import itertools

data= [ 1 for _ in range(40) ]
print( list(itertools.permutations(data) ))
print( set(itertools.permutations(data) ))
