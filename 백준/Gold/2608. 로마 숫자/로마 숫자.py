roman_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}

sub = {
        'IV': 4, 'IX': 9,
        'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900}

def roman_to_int(roman: str) -> int:
    i = 0 #roman 인덱스
    total = 0 #리턴할 합
    while i < len(roman):
        if i+1 < len(roman) and roman[i:i+2] in sub:
            #뺄셈에 해당하는 부분인지를 먼저 확인해야함함
            total += sub[roman[i:i+2]]
            i += 2
        else:
            total += roman_dict[roman[i]]
            i += 1
    return total

def int_to_roman(num) -> str:
    int_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in int_roman:
        while num >= value:
            result += symbol
            num -= value
    return result

roman1 = input()
roman2 = input()

ans = roman_to_int(roman1) + roman_to_int(roman2)
print(ans)
print(int_to_roman(ans))