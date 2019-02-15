def ddg(lista, oca):
    if oca < len(lista):
        print('La oca es:', lista[oca-1])
    else:
        print('Este jugador no esta participando')

lista = []
flag = True
while flag:
    jugador = input('Introduce el nombre de tu jugador y cuando quieras terrminar pulsa 0:')
    if jugador == '0':
        flag = False
    else:
        lista.append(jugador)
ddg(lista,4)
