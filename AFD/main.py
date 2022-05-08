from random import randint

states = input().split(" ");  # pegando os estados
alfabeth = input().split(" ")  # pegando o alfabeto

stateOfError = randint(0, len(states) * 100)
while (stateOfError in states): stateOfError = randint(0, len(states) * 100)


def gerar_matriz(n_linhas, n_colunas):
    return [[stateOfError] * n_colunas for _ in range(n_linhas)]

matriz = gerar_matriz(len(states), len(alfabeth))  # criando a matriz estado/ações

trasaction = int(input())  # pegando o numero de transações

for i in range(trasaction):
    tripla = input().split(" ");  # pegando a tripla
    stateFrom = tripla[0];
    letra = tripla[1];
    stateTo = tripla[2];
    matriz[states.index(stateFrom)][alfabeth.index(letra)] = stateTo;  # populando a matriz com os estados

initialState = input();
finalState = input().split(" ");

words = input().split(" ")

for word in words:
    atualState = initialState;
    for y in word:
        if(atualState != stateOfError):
            atualState = matriz[states.index(atualState)][alfabeth.index(y)];  # pegando o estado futuro na matriz de estado/ações
    if (atualState in finalState):
        print('S')
    else:
        print('N')