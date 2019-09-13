def __main__():
    td = int(input('Ingrese tornillos defectuosos: '))
    tp = int(input('Ingrese tornillos producidos: '))
    if td < 200 and tp > 10000:
        print('Grado 8')
    elif tp > 10000:
        print('Grado 7')
    elif td < 200:
        print('Grado 6')
    else:
        print('Grado 5')


if __name__ == '__main__':
    __main__()
