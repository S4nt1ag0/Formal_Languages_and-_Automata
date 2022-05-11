from random import randint

states = input().split(" ");  # pegando os estados
alfabeth = input().split(" ")  # pegando o alfabeto

stateOfError = randint(0, len(states) * 100)
while (stateOfError in states): stateOfError = randint(0, len(states) * 100)

dicionarioDeEstadosFuturos = {};

for i in states:
    dicionarioDeEstadosFuturos[i] = {}
    for j in alfabeth:
        dicionarioDeEstadosFuturos[i][j] = stateOfError;

trasaction = int(input())  # pegando o numero de transações

for i in range(trasaction):
    tripla = input().split(" ");  # pegando a tripla
    stateFrom = tripla[0];
    letra = tripla[1];
    stateTo = tripla[2];
    dicionarioDeEstadosFuturos[stateFrom][letra] = stateTo;  # populando o dicionario com os estados futuros corretos


initialState = input();
finalState = input().split(" ");

words = input().split(" ")

for word in words:
    atualState = initialState;
    for y in word:
        if(atualState != stateOfError):
            atualState = dicionarioDeEstadosFuturos[atualState][y];  # pegando o estado futuro no dicionario de estado/ações
    if (atualState in finalState):
        print('S')
    else:
        print('N')