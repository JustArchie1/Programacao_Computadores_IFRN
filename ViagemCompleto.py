# Pedindo pelas infos necessárias...
hora_inicial = int(input("Por favor, informe o número de horas da partida (Ex: 00, 01):"))

minuto_inicial = int(input("Por favor, informe o número de minutos da partida (Ex: 00, 01):"))

hora_final = int(input("Por favor, informe o número de horas da chegada:"))

minuto_final = int(input("Por favor, informe o número de minutos da chegada:"))

descanso = int(input("Informe o número de segundos utilizados para descanso:"))

litros = float(input("Informe a quantidade de combustível gasto em litros:"))

preco = float(input("Informe o preço do litro do combustível em reais:"))

distancia = float(input("Informe a distância percorrida em quilômetros:"))

# Checando os valores...

if minuto_inicial > 59 or minuto_final > 59:
    print("Insira um valor válido para minutos. (0 a 59)")

elif minuto_inicial < 0 or minuto_final < 0:
    print("Insira um valor positivo para minutos.")

elif hora_inicial > 23 or hora_final > 23:
    print("Informe um valor válido para horas. (0 a 23)")

elif hora_inicial < 0 or hora_final < 0:
    print("Insira um valor positivo para horas.")

elif descanso < 0 or litros < 0 or distancia < 0 or preco < 0:
    print("O valor mínimo para descanso, litros de combustível, distância ou preço é 0. Tente novamente. :)")

# Converter o tempo para segundos...

else:
    tempo_inicial = hora_inicial * 3600 + minuto_inicial * 60
    tempo_final = hora_final * 3600 + minuto_final * 60

    # Identificar tempos em dias diferentes...

    if tempo_final < tempo_inicial:
        tempo_final += 24 * 3600
    
    # Calcular tempo total da viagem em segundos...
    tempo_viagem_segundos = (tempo_final - tempo_inicial) + descanso

    # Converter para horas para calcular as velocidades...
    tempo_viagem_horas = tempo_viagem_segundos / 3600

    # Calcular velocidade global (considerando descanso)...
    velocidade_global = distancia / tempo_viagem_horas

    # Calcular velocidade média em movimento (sem descanso)...
    velocidade_movimento = distancia / ((tempo_final - tempo_inicial) / 3600)

    # Calcular o custo total do combustível para a viagem...
    custo = litros * preco

    # Calcular o desempenho do combustível (km/L)...
    desempenho_combustivel = distancia / litros

    # Calcular o custo por quilômetro (R$/km)...
    custo_quilometro = custo / distancia

    # Exibir os resultados
    print("Tempo de viagem (em segundos):", tempo_viagem_segundos)
    print(f"Velocidade global: {velocidade_global:.2f}")
    print(f"Velocidade média em movimento: {velocidade_movimento:.2f}")
    print("Custo total do combustível para a viagem: R$", custo)
    print(f"Desempenho do combustível (km/L): {desempenho_combustivel:.2f}")
    print(f"Custo por quilômetro (R$/km): {custo_quilometro:.2f}")

# Tempo total de código: 3 horas e 15 minutos. Minhas maiores dificuldades foram converter as horas. E eu acabava me perdendo no meio dessa bagunça...