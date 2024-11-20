# Pedir pelo valor do saque...

saque = float(input("Insira o valor do saque:"))

# Checar se é um valor positivo...

if saque <0:
    print("O valor deve ser positivo.")

# Exibir caso o valor seja menor do que 1 centavo. Não é necessário, mas decidi colocar ainda assim...

elif saque <0.01:
     print("O valor é muito pequeno para ser calculado.")

else:
     # Converter o valor para centavos, pois fazer "direto" estava resultando em problemas nas últimas casas decimais... Acredite, foram muitas tentativas.
     
     saque_centavos = saque * 100

     nota100 = saque_centavos // 10000
     nota50  = saque_centavos % 10000 // 5000
     nota20  = saque_centavos % 10000 % 5000 // 2000
     nota10  = saque_centavos % 10000 % 5000 % 2000 // 1000
     nota5   = saque_centavos % 10000 % 5000 % 2000 % 1000 // 500
     nota2   = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 // 200
     moeda1  = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 // 100

     moeda50 = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 // 50
     moeda25 = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 // 25
     moeda10 = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 // 10
     moeda5  = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10 // 5
     moeda01 = saque_centavos % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10 % 5 // 1

     # Exibir as devidas notas e moedas...

     print(f"O saque apresentará {nota100:.0f} notas de 100 reais.")
     print(f"{nota50:.0f} notas de 50 reais.")
     print(f"{nota20:.0f} notas de 20 reais.")
     print(f"{nota10:.0f} notas de 10 reais.")
     print(f"{nota5:.0f} notas de 5 reais.")
     print(f"{nota2:.0f} notas de 2 reais.")
     print(f"{moeda1:.0f} moedas de 1 real.")
     print(f"{moeda50:.0f} moedas de 50 centavos.")
     print(f"{moeda25:.0f} moedas de 25 centavos.")
     print(f"{moeda10:.0f} moedas de 10 centavos.")
     print(f"{moeda5:.0f} moedas de 5 centavos.")
     print(f"{moeda01:.0f} moedas de 1 centavo.")

# Tempo Total: Cerca de duas horas e vinte minutos. E eu já tinha feito uma base no Pycode, pra celular.