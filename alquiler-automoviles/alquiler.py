def __main__():
    d = int(input('Ingrese km recorridos: '))
    if d < 301:
        p = d * 30
    elif d < 1001:
        p = d * 30 + (d - 300) * 0.15
    else:
        p = d * 30 + (d - 300) * 0.10

    i = p * 0.18
    p = p - i
    print(
        """Distancia recorrida: {distancia} \nDistancia: ${valor} \nImpuestos: ${imp} \nTotal:{t}""".format(
            distancia=d, valor=p,imp=i, t=p + i))


if __name__ == '__main__':
    __main__()
