def __main__():
    nm = 0
    for i in range(1, 4):
        n = int(input('Ingrese un valor {n} entero positivo: '.format(n=i)))
        if i > 1:
            if n < nm:
                nm = n
        else:
            nm = n

    print('El número menor es: ', nm)


if __name__ == '__main__':
    __main__()
