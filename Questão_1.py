import sys

massa_inicial = float(input("Informe a massa inicial em gramas: "))

massa_original = massa_inicial

tempo_segundos = 0

contador_ciclos = 0

if massa_inicial < 0:
    sys.exit('Informe um valor positivo. Ajuda ai, por gentileza.')

else:
    
    while massa_inicial >= 0.5:
        
        massa_inicial /= 2
        
        massa_final = massa_inicial
        
        tempo_segundos += 50
        
        contador_ciclos += 1
    
    horas = tempo_segundos // 3600
    
    minutos = (tempo_segundos % 3600) // 60
    
    segundos = (tempo_segundos % 60) % 60
    
    print(f'A massa inicial era de {massa_original} gramas.')
    print(f'A massa final foi de {massa_final} gramas.')
    print(f'O tempo decorrido foi de {horas}:{minutos}:{segundos}')
    print(f'Ocorreram {contador_ciclos} ciclos.')
