
import logging
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


OPEN=re.compile(r'(\d+)[')

def find_matched_brack(data):
    stack=[]
    for achar in data:
        if achar == '[':

    

def expansion(data, num=0):
    m = re.search(OPEN, data)
    if m is None:
        if num > 0:
            index=data.index(CLOSE)






def main():
    #data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]']
    data=['abc2[d]fgh3[i]']
    for item in data:
        print(item, expansion(item))

    print stack

if __name__ == "__main__":
    main()
