def __main__():
    d = int(input('Ingrese km recorridos: '))
    if d < 300:
        p = d * 30
    elif d < 1001:
        p = d * 30 + (d - 300) * 0.15
    else:
        p = d * 30 + (d - 300) * 0.10

    print("""Distancia recorrida: {distancia} \nValor a pagar: ${valor}""".format(distancia=d, valor=p))


if __name__ == '__main__':
    __main__()