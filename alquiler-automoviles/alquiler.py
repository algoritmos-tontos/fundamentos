def __main__():
    d = int(input('Ingrese km recorridos: '))
    if d > 1000:
        p = 30 + (d - 300) * 0.10
    elif d > 300:
        p = 30 + (d - 300) * 0.15
    else:
        p = 30

    i = p * 0.18
    p = p - i
    print(
        """Distancia recorrida: {distancia} \nDistancia: ${valor} \nImpuestos: ${imp} \nTotal:{t}""".format(
            distancia=d, valor=p,imp=i, t=p + i))


if __name__ == '__main__':
    __main__()
