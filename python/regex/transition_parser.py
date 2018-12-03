
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# status  state   transition
# start     0       digit,  non-digit
#
#

def main():
    data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i10[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(item, expansion(item))


if __name__ == "__main__":
    main()
