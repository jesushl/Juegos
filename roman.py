#  0 <= n <=100

roman = {
    1 : 'I', # Seccioin 1
    4 : 'IV',
    5 : 'V',
    9: 'IX', # Seccion 1
    10: 'X', # seccion 2
    50: 'L',# Seccion 2
    90: 'XC',# Seccion 2
    100: 'C'
}

roman_multi_occurrency = {
    1 : True, # Seccioin 1
    4 : False,
    5 : False,
    9: False, # Seccion 1
    10: True, # seccion 2
    50: False,# Seccion 2
    90: False,# Seccion 2
    100: False

}

order = [100,90, 50, 10, 9, 5, 4, 1]

def arabic_to_roman_2(n):
    arabic = []
    for roman_index in order:
        if n == 0 :
            break
        if n > roman_index:
            print(n)
            if roman_multi_occurrency[roman_index]:
                arabic, n = muilti_ocurrency_munber(
                    arabic,
                    n,
                    roman_index
                )
            else:
                arabic, n = direct_number(
                    arabic,
                    n,
                    roman_index
                )
    return ''.join(arabic)


def direct_number(
    arabic,
    arabic_number,
    roman_index
):
    _ = arabic_number / roman_index
    if _ >= 1:
        arabic.append(roman[roman_index])
        arabic_number = arabic_number - roman_index
    return arabic, arabic_number

def muilti_ocurrency_munber(
    arabic,
    arabic_number,
    roman_index
):
    _ = arabic_number / roman_index
    if _ >= 1:
        for i in range(int( _)):
            arabic.append(roman[roman_index])
        arabic_number = arabic_number - roman_index
    return arabic, arabic_number



if __name__ == '__main__':
    arabico_1 = 70
    print(arabico_1)
    print(arabic_to_roman_2(arabico_1))
    arabico_2 = 5
    print(arabico_2)
    print(arabic_to_roman_2(arabico_2))
    arabico_3 = 55
    print(arabico_3)
    print(arabic_to_roman_2(arabico_3))
    arabico_4 = 95
    print(arabico_4)
    print(arabic_to_roman_2(arabico_4))
    arabico_5 = 94
    print(arabico_5)
    print(arabic_to_roman_2(arabico_5))
    arabico_6 = 99
    print(arabico_6)
    print(arabic_to_roman_2(arabico_6))
    arabico_7 = 78
    print(arabico_7)
    print(arabic_to_roman_2(arabico_7))
