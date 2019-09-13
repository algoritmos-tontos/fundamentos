def __main__():
    n1 = int(input('Ingrese fecha nacimiento Juan: '))
    n2 = int(input('Ingrese fecha nacimiento Mario: '))
    n3 = int(input('Ingrese fecha nacimiento Pedro: '))

    c1 = (n1 % 10)
    rs_1 = n1 - c1
    rf_1 = rs_1 + 9

    c2 = (n2 % 10)
    rs_2 = n2 - c2
    rf_2 = rs_2 + 9

    if rs_1 <= n2 <= rf_1 and rs_1 <= n3 <= rf_1:
        print('Juan, Mario y Pedro contemporáneos')
    elif rs_1 <= n2 <= rf_1:
        print('Juan y Mario contemporáneos')
    elif rs_1 <= n3 <= rf_1:
        print('Juan y Pedro contemporáneos')
    elif rs_2 <= n3 <= rf_2:
        print('Mario y Pedro contemporános')
    else:
        print('Ninguno contemporáneo')


if __name__ == '__main__':
    __main__()
