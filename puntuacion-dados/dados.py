def __main__():
    d1 = int(input('Ingrese dado 1: '))
    d2 = int(input('Ingrese dado 2: '))
    d3 = int(input('Ingrese dado 3: '))

    if d1 == 6 and d1 == d2 == d3:
        print('Puntuación: Excelente')
    elif d1 == 6 == d2 or d1 == 6 == d3 or d2 == 6 == d3:
        print('Puntuación: Muy bien')
    elif d1 == 6 or d2 == 6 or d3 == 6:
        print('Puntuación: Regular')
    else:
        print('Puntuación: Pésima')


if __name__ == '__main__':
    __main__()
