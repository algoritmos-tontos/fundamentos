def __main__():
    l1 = int(input('L1: '))
    l2 = int(input('L2: '))
    l3 = int(input('L3: '))
    v = True
    if l1 == l2 == l3:
        print('Triangulo equilatero')
    else:
        if l1 >= l2 and l1 >= l3 and l1 > l2 + l3:
            print('Triangulo no válido')
            v = False

        if l2 >= l1 and l2 >= l3 and l2 > l1 + l3:
            print('Triangulo no válido')
            v = False

        if l3 >= l1 and l3 >= l2 and l3 > l1 + l2:
            print('Triangulo no válido')
            v = False

        if v:
            if l1 == l2 or l2 == l3 or l1 == l3:
                print('Triangulo Isóseles')
            else:
                print('Triangulo escaleno')


if __name__ == '__main__':
    __main__()