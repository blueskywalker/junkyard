


def digits_of(number):
    return [int(i) for i in str(number)]

def lunh_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

print lunh_checksum(4100234123123438)

def is_lunh_valid(card_number):
    return luhn_checksum(card_number) == 0

