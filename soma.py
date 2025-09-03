#Responsabilidade da variável ----> guardar valor
#Responsabilidade do for ----> repetir ---> iterar

numeros = [1,2,3,4,5,6,7,8,9,10]
nome = "Rosiane"
#// ---> pegar somente a parte inteira
#round ----> serve para arredondar os valores
# Somando os números pares de 1 a 10
#range----> gerador de intervalos 
soma = 0 #variável acumuladora
for i in range(1, 11):  # de 1 até 10
    if i % 2 == 0:  # verifica se o número é par
        soma += i

print(f'A soma dos números pares de 1 a 10 é {soma}')

#