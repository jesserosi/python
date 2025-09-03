# Desafio
# fazer o fatorial de um número-------> fatorial é multiplicar a sequencia de numeros até o 1 exemplo fatorial de 5 (5! 5*4*3*2*1)

# passo 1 --> receber um NUMERO através do input
# passo2 ---> fazer um contador deste número ate 1 
# passo3 ---> multiplicar os valores em uma variável()

numero = int(input("Digite um número:"))
fatorial = 1
for i in range(numero,1,-1):  # de numero até -1
    fatorial *= i
    print(fatorial)



    #para armazenar um valor, precisa criar uma variável. no caso acima a variavel criada chama-se numero