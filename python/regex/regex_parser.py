


import regex


pattern=r'((\d+)(\[.*\]))'

def main():
    data=['abc', '10[abc]','10[ab3[c]d]', 'abc10[abc3[de]fg]hij', 'abc2[d]fgh3[i]', 'abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    #data = ['abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]']
    for item in data:
        print(regex.findall(pattern, item))

if __name__ == "__main__":
    main()
