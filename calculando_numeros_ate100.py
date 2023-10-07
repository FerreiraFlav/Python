# sourcery skip: simplify-generator, sum-comprehension
soma = 0

# Use um loop for para somar os números de 1 a 100
for numero in range(1, 101):
    soma += numero

# Imprima o resultado
print("A soma de todos os números de 1 a 100 é:", soma)


#or 

#soma = sum(range(1, 101))
# Imprima o resultado
#print("A soma de todos os números de 1 a 100 é:", soma)