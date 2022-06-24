states = input().split(" ");  # pegando os estados
alfabeth = input().split(" ")  # pegando o alfabeto

trasaction = int(input())  # pegando o numero de transações

dicionarioDeEstadosFuturos = {};

for state in states:
    dicionarioDeEstadosFuturos[state] = {}  # criando um dicionario para cada estado

for i in range(0, trasaction):
    tripla = input().split(" ");  # pegando a tripla
    stateFrom = tripla[0];
    letra = tripla[1];
    stateTo = tripla[2];

    if (letra in dicionarioDeEstadosFuturos[stateFrom]):  # adiciona um estado a lista de estados futuros
        dicionarioDeEstadosFuturos[stateFrom][letra].append(stateTo)
    else:  # ou cria a lista caso essa ainda não exista
        dicionarioDeEstadosFuturos[stateFrom][letra] = [stateTo]

stack_of_atualStates = []

initialState = input()
finalStates = input().split(" ");

words = input().split(" ")

for word in words:
    stack_of_atualStates = [initialState]
    for letter in word:
        stack_of_futureStates = []
        for state in stack_of_atualStates:
            if (dicionarioDeEstadosFuturos[state].get(letter)):
                futureStates = dicionarioDeEstadosFuturos[state].get(letter)
                for futureState in futureStates:
                    if (futureState not in stack_of_futureStates):
                        stack_of_futureStates.append(futureState)
        stack_of_atualStates = stack_of_futureStates

    flag = 0
    for state in stack_of_atualStates:
        if (state in finalStates):
            flag = 1
    if (flag):
        print('S')
    else:
        print('N')