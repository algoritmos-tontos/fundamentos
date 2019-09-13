def __main__():
    n = []
    # This only works for three values.
    for i in range(1, 4):
        n1 = int(input('Ingrese numero {i}: '.format(i=i)))
        if i > 1:
            if n[i - 2] >= n1:
                n.append(n1)
            else:
                n.insert(0, n1)
        else:
            n.append(n1)
    print("""Números ascendentes: {n1}-{n2}-{n3}""".format(n1=n[2], n2=n[1], n3=n[0]))
    print("""Números descendentes: {n3}-{n2}-{n1}""".format(n3=n[0], n2=n[1], n1=n[2]))


if __name__ == '__main__':
    __main__()
