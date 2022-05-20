states = input().split(" ");  # pegando os estados
alfabeth = input().split(" ")  # pegando o alfabeto

dicionarioDeEstadosFuturos = {};

trasaction = int(input())  # pegando o numero de transações

for state in states:
    dicionarioDeEstadosFuturos[state] = {}

for i in range(0, trasaction):
    tripla = input().split(" ");  # pegando a tripla
    stateFrom = tripla[0];
    letra = tripla[1];
    stateTo = tripla[2];

    if(letra not in dicionarioDeEstadosFuturos[stateFrom]):
        dicionarioDeEstadosFuturos[stateFrom][letra] = [stateTo]
    else:
        dicionarioDeEstadosFuturos[stateFrom][letra].append(stateTo)

stack_of_atualStates = []

initialState = input()
finalStates = input().split(" ");

words = input().split(" ")

for word in words:
    stack_of_atualStates = [initialState]
    flag = 0
    for letter in word:
        stack_of_futureStates = []
        for state in stack_of_atualStates:
            if(dicionarioDeEstadosFuturos[state].get(letter)):
                futureStates = dicionarioDeEstadosFuturos[state].get(letter)
                for futureState in futureStates:
                    if(futureState not in stack_of_futureStates):
                        stack_of_futureStates.append(futureState)
        stack_of_atualStates = stack_of_futureStates

    for state in stack_of_atualStates:
        if(state in finalStates):
            flag = 1
    if(flag):
        print('S')
    else:
        print('N')