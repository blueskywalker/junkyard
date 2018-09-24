

import regex

pattern='{((?>[^{}]+|(?R))*)}'

print(regex.findall(pattern,'{1, {2, 3}} {4, 5}'))


