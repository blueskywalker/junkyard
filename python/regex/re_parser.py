
import re

pattern = r'(\d+)\[(.*)\]'

tokenizer=re.compile(pattern)

def expansion(data):

    def expand(times, data):
        return int(times) * expansion(data) 

    matched = tokenizer.search(data)
    if matched is None:
        return data


    pre = data[:matched.start()]
    expanded = expand(matched.group(1), matched.group(2)) 
    post = expansion(data[matched.end():])

    #print("{pre}:{expanded}:{post}".format(**locals()))
    return pre + expanded + post

data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]']
data = [ 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]' ]
for item in data:
    print(item, expansion(item))
