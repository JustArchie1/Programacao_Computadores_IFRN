# Inserir o número...

numero = int(input("Insira um número de até quatro algarismos: "))

# Conferir se tem mais de 4 algarismos...

if numero > 9999:
    print("O número possui mais de 4 algarismos.")
elif numero < -9999:
    print("O número possui mais de 4 algarismos.")
    
else:
    
    # Transformar número negativo em positivo...

    numero = abs(numero)
    
    # Pegar o número de cada casa decimal...

    milhar = numero // 1000
    centena = numero % 1000 // 100
    dezena = numero % 100 // 10
    unidade = numero % 10
    
    # Definir a soma dos algarismos...

    soma = milhar + centena + dezena + unidade
    print("A soma dos algarismos é:", soma)