# Lista no número de dias para cada mês...

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dia_inicial = int(input("Insira um dia inicial:"))
mes_inicial = int(input("Insira um mês inicial:"))

dia_final = int(input("Insira um dia final:"))
mes_final = int(input("Insira um mês final:"))

# Verificar valores...

if dia_inicial <= 0 or mes_inicial <= 0 or dia_final <= 0 or mes_final <=0 or mes_inicial > 12 or mes_final > 12:
    print("Os valores inseridos são invalidos. Confira os números inseridos e tente novamente.")

else:

    # Converter as meses para dias...

    data_inicial = sum(dias_por_mes[:mes_inicial - 1]) + dia_inicial
    data_final = sum(dias_por_mes[:mes_final - 1]) + dia_final

    if data_inicial == data_final:
        print("A data inicial é igual á data final. Tente novamente.")

    else:
        
        # Reconhecer que, se a data final for inferior á inicial, um ano se passou...

        if data_final < data_inicial:
            data_final += 365
            
        diasdecorridos = data_final - data_inicial
        
        print(diasdecorridos)