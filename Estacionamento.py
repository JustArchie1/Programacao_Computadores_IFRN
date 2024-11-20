tempo_minutos = int(input("Informe o número de minutos no qual o veículo ocupou o estacionamento:"))

# Converter minutos para horas...

horas = tempo_minutos // 60

# Checar se ainda restam minutos, para então considerar na taxa...

if tempo_minutos % 60 !=0:
    horas += 1

if horas < 0:
    print("O valor inserido é inválido. Tente novamente.")

elif horas <= 2:
    pagamento = 8 * horas
    print(f"O valor a ser pago é de {pagamento:.2f}R$.")

elif horas <= 4:
    pagamento = 16 + (5 * (horas - 2))
    print(f"O valor a ser pago é de {pagamento:.2f}R$.")

elif horas <= 12:
    pagamento = 16 + 10 + (3 * (horas - 4))
    print(f"O valor a ser pago é de {pagamento:.2f}R$.")

elif horas > 12:
    print(f"O valor a ser pago é de 80,00R$.")