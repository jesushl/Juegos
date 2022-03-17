"""
If I receibe a string with binary numer like '11011101'
The game is this:
    If the number is pair divide the number on 2.
    if the number is odd, then rest 1 and continue to 0
    return the number of times you did this 
    16 8 4 2 1
    
    10 = 1010
    5 =0101
"""
def run_to_right(value: str):
    int_value = int(value, 2)
    steps = 0
    while int_value != 0:
        steps = steps + 1
        int_value = int_value >> 1
    return steps 

if __name__ == "__main__":
    assert run_to_right('1010') == 4
    # lets try with a super huge number 
    huge_imput = '{0:b}'.format(9999999999)
    print("movements on huge number: {}".format(run_to_right(huge_imput)))
