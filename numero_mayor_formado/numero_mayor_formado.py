def __main__():
    n = input('Ingrese un número: ')
    i = 0
    n = list(n)
    while i < len(n):
        # TODO: this sorting process is not optimum for many numbers
        if i > 0:
            a = n[i]
            if n[i] > n[i - 1]:
                n[i] = n[i - 1]
                n[i - 1] = a
                i = 0
        i = i + 1

    print(''.join(n))


if __name__ == '__main__':
    __main__()
