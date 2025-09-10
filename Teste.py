# Soma dos números pares de 1 a 50

soma = 0

for numero in range(1, 51):
    if numero % 2 == 0:   # Verifica se o número é par
        soma += numero

print("A soma dos números pares de 1 a 50 é:", soma)
