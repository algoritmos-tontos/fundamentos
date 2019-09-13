def __main__():
    n = []
    p = 0
    for i in range(1, 5):
        n1 = float(input('Ingrese nota {i}: '.format(i=i)))
        if i > 1:
            if n[i - 2] >= n1:
                n.append(n1)
            else:
                n.insert(0, n1)
        else:
            n.append(n1)

    for i in range(0, len(n) - 1):
        p += n[i]

    print("""Promedio: {p}""".format(p=p / 3))
    print("""Nota eliminada: {d}""".format(d=n[len(n)-1]))


if __name__ == '__main__':
    __main__()
