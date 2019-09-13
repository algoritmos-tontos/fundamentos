def __main__():
    n1 = input('Ingrese un número: ')
    i = 0
    n = list(n1)
    p = True
    if int(n1) < 0:
        p = False


    while i < len(n):
        # TODO: this sorting process is not optimum for many numbers
        if i > 0:
            a = n[i]
            if n[i] > n[i - 1] and p or n[i] < n[i - 1] and not p:
                n[i] = n[i - 1]
                n[i - 1] = a
                i = 0
        i = i + 1

    print(''.join(n))


if __name__ == '__main__':
    __main__()
