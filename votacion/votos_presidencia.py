def __main__():
    v1 = int(input('Ingrese votos candidato Juan: '))
    v2 = int(input('Ingrese votos candidato Pedro: '))
    v3 = int(input('Ingrese votos candidato Maria: '))
    s = (v1 + v2 + v3) / 2
    if v1 > s:
        print('Gandor es Juan')
    elif v2 > s:
        print('Gandor es Pedro')
    elif v3 > s:
        print('Gandor es Maria')
    else:
        if v1 == v2 == v3:
            print('Empate tripe, reelección')
        elif v1 > v2 > v3:
            print('Elecciones entre Juan y Pedro')
        elif v1 > v3 > v2:
            print('Elecciones entre Juan y Maria')
        elif v1 > v2 == v3:
            print('Elecciones entre Pedro y Maria para elegir quien se enfrenta a Juan')
        elif v2 > v1 > v3:
            print('Elecciones entre Pedro y Juan')
        elif v2 > v3 > v1:
            print('Elecciones entre Pedro y Maria')
        elif v2 > v1 == v3:
            print('Elecciones entre Juan y Maria para elegir quien se enfrenta a Pedro')
        elif v3 > v1 > v2:
            print('Elecciones entre Maria y Juan')
        elif v3 > v2 > v1:
            print('Elecciones entre Maria y Pedro')
        elif v3 > v1 == v2:
            print('Elecciones entre Juan y Pedro para elegir quien se enfrenta a Maria')


if __name__ == '__main__':
    __main__()
