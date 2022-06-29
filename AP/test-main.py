dicionarioDeEstadosFuturos = {
    "0":{
        "a":[['*','0','A']],
        "b":[['A','1','*']]
    },
    "1":{
        "b":[['A','1','*']]
    }
}

estadoInicial = "0"
estadosFinais = ["1"]

wa = 'a'
wb = 'b'

palavras = []

for i in range(5):
   w = wa+wb
   palavras.append(w)
   wa = wa*5
   wb = wb*5

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
                    for element in empilha:
                        pilhaTemporaria.append(element)

                pilhaEstadosAtuais.append([estadoTo, pilhaTemporaria, palavraTemp])

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
                    for element in empilha:
                        pilhaTemporaria.append(element)

                pilhaEstadosAtuais.append([estadoTo, pilhaTemporaria, palavraTemp2])

    if flag:
        print('S')
    else:
        print('N')
