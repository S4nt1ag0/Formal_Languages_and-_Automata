estados = input().split(" ") # pegando os estados
alfabeto = input().split(" ")  # pegando o alfabeto
pilhaAlfabeto = input().split(" ")  # pegando o alfabeto da pilha
transacoes = int(input())  # pegando o numero de transações

dicionarioDeEstadosFuturos = {}

for estado in estados:
    dicionarioDeEstadosFuturos[estado] = {}  # criando um dicionario para cada estado

for i in range(0, transacoes):
    quintupla = input().split(" ") # pegando a tripla
    estadoFrom = quintupla[0]
    letra = quintupla[1]
    desempilha = quintupla[2]
    estadoTo = quintupla[3]
    empilha = quintupla[4]

    if letra not in dicionarioDeEstadosFuturos[estadoFrom]:  # adiciona um estado a lista de estados futuros
        dicionarioDeEstadosFuturos[estadoFrom][letra] = []

    dicionarioDeEstadosFuturos[estadoFrom][letra].append([desempilha, estadoTo, empilha])

estadoInicial = input()
estadosFinais = input().split(" ")

palavras = input().split(" ")

for palavra in palavras:
    pilhaEstadosAtuais = [(estadoInicial, [], palavra)]
    flag = 0

    while flag == 0 and len(palavra) > 0 and len(pilhaEstadosAtuais) > 0:
        estado, pilha, palavraTemp = pilhaEstadosAtuais.pop()

        if dicionarioDeEstadosFuturos[estado].get('*') and palavraTemp != '*':
            triplas = dicionarioDeEstadosFuturos[estado].get('*')
            for desempilha, estadoTo, empilha in triplas:
                pilhaTemporaria = pilha.copy()

                if desempilha != '*':
                    if len(pilhaTemporaria) == 0:
                        break
                    else:
                        topo = pilhaTemporaria.pop()
                        if desempilha != topo:
                            continue

                if empilha != '*':
                    pilhaTemporaria.append(empilha)

                pilhaEstadosAtuais.append([estadoTo, pilhaTemporaria,palavraTemp])

        if len(palavraTemp) == 0:
            if estado in estadosFinais and len(pilha) == 0:
                flag = 1
                break
            else:
                continue

        palavraTemp2 = palavraTemp[1:]

        if dicionarioDeEstadosFuturos[estado].get(palavraTemp[0]):
            triplas = dicionarioDeEstadosFuturos[estado].get(palavraTemp[0])
            for desempilha, estadoTo, empilha in triplas:
                pilhaTemporaria = pilha.copy()

                if desempilha != '*':
                    if len(pilhaTemporaria) == 0:
                        break
                    else:
                        topo = pilhaTemporaria.pop()
                        if desempilha != topo:
                            continue

                if empilha != '*':
                    pilhaTemporaria.append(empilha)

                pilhaEstadosAtuais.append([estadoTo, pilhaTemporaria, palavraTemp2])

    if flag:
        print('S')
    else:
        print('N')
