def __main__():
    n = input('Ingrese un número: ')
    j = []
    a = None
    for i in range(0, len(n)):
        s = '1' + ('0' * (len(n) - 1 - i))
        if a is not None:
            if i == len(n) - 1:
                d = a
            else:
                d = int(a) // int(s)
                a = int(a) % int(s)
        else:
            d = int(n) // int(s)
            a = int(n) % int(s)

        j.append(d)

    i = 0
    while i < len(j):
        # TODO: this sorting process is not optimum for many numbers
        if i > 0:
            n = j[i]
            if j[i] > j[i - 1]:
                j[i] = j[i - 1]
                j[i - 1] = n
                i = 0
        i = i + 1

    print(''.join(j))


if __name__ == '__main__':
    __main__()
