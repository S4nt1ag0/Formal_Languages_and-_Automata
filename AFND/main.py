states = input().split(" ");  # pegando os estados
alfabeth = input().split(" ")  # pegando o alfabeto

dicionarioDeEstadosFuturos = dict();

trasaction = int(input())  # pegando o numero de transações


for i in range(trasaction):
    tripla = input().split(" ");  # pegando a tripla
    stateFrom = tripla[0];
    letra = tripla[1];
    stateTo = tripla[2];
    dicionarioDeEstadosFuturos[stateFrom, letra] = dicionarioDeEstadosFuturos.get((stateFrom, letra)) or []
    dicionarioDeEstadosFuturos[stateFrom, letra].append(stateTo);  # populando o dicionario com os estados futuros corretos

stack_of_atualStates = []

initialStates = input().split(" ");
finalStates = input().split(" ");

words = input().split(" ")

stack_of_futureStates = []
for word in words:
    for initialState in initialStates:
        stack_of_atualStates.append(initialState)
    for y in word:
        while stack_of_atualStates:
            atualState = stack_of_atualStates.pop()
            futureStates = dicionarioDeEstadosFuturos.get((atualState,y))
            if(y=="*"):
                if(futureStates):
                    futureStates.append(atualState)
                else:
                    futureStates = [atualState]
            if(futureStates):
                for futureState in futureStates:
                    stack_of_futureStates.append(futureState)
        while stack_of_futureStates:
            stack_of_atualStates.append(stack_of_futureStates.pop())
    flag = 0
    for finalState in finalStates:
        if(finalState in stack_of_atualStates):
            flag = 1
    if (flag):
        print('S')
    else:
        print('N')