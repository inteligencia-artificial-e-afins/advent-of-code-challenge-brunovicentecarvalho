with open("sample.in", "r") as f:
    data = f.read().splitlines()

prioridades = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
               'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


grupos = [data[i:i+3] for i in range(0, len(data), 3)]

soma_prioridades = 0
for grupo in grupos:
    sacos = [set(saco) for saco in grupo]
    distintivo = sacos[0].intersection(sacos[1], sacos[2]).pop()
    print(f'Tipo prioridades[distintivo] : {type(prioridades[distintivo])})')
    print(f'Prioridades: {prioridades}')
    print(f'Distintivo: {distintivo}')
    print(f'Prioridades[distintivo]: {prioridades[distintivo]}')
    print(f'Tipo soma_prioridades : {type(soma_prioridades)}')
    print(f'Soma Prioridades : {soma_prioridades}')
    soma_prioridades += prioridades[distintivo]

print(soma_prioridades)


