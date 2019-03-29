def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i, value in enumerate(s):
        if i > 0 and rom_val[value] > rom_val[s[i - 1]]:
            int_val += rom_val[value] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

print(roman_to_int('MMMCMLXXXVI'))
print(roman_to_int('MMMM'))
print(roman_to_int('C'))
print(roman_to_int('IV'))
