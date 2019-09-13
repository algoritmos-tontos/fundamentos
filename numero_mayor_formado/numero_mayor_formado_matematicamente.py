def __main__():
    n = input('Ingrese un número: ')
    p = False
    if int(n) < 0:
        p = True
        n = n.replace('-', '')

    j = []
    for i in range(0, len(n)):
        s = '1' + ('0' * (len(n) - 1 - i))
        if i > 0:
            if i == len(n) - 1:
                d = a
            else:
                d = int(a) // int(s)
                a = int(a) % int(s)
        else:
            d = int(n) // int(s)
            a = int(n) % int(s)

        j.append(str(d))

    i = 0
    while i < len(j):
        # TODO: this sorting process is not optimum for many numbers
        if i > 0:
            n = j[i]
            if j[i] > j[i - 1] and not p or j[i] < j[i - 1] and p:
                j[i] = j[i - 1]
                j[i - 1] = n
                i = 0
        i = i + 1

    j = ''.join(j)
    if p:
        j = '-' + j
    print(j)


if __name__ == '__main__':
    __main__()
