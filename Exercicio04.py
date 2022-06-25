#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

cont = 0

for c in range(1,5):
    nota = int(input(f'Digite a nota {c}: '))
    cont += nota
    
media = cont / 4

print(
    f'A média deste aluno é {media}'
    )