from datetime import datetime

# Solicita os dados do usuário...
sexo = input("Informe o sexo da pessoa (masculino/feminino): ")
data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
data_inicio_contribuicao = input("Informe a data de início da contribuição (DD/MM/AAAA): ")

# Validação do sexo...
if sexo not in ["masculino", "feminino"]:
    print("Erro: Sexo inválido! Digite 'masculino' ou 'feminino'.")

# Regras de aposentadoria...

if sexo == "masculino":
    idade_aposentadoria = 65
    tempo_contribuicao_aposentadoria = 35

else:  
    idade_aposentadoria = 62
    tempo_contribuicao_aposentadoria = 30

contribuicao_minima = 15

# Data atual para referência...

data_atual = datetime.today()

# Calcula a idade da pessoa...

nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

idade_atual = data_atual.year - nascimento.year

if (data_atual.month, data_atual.day) < (nascimento.month, nascimento.day):
    idade_atual -= 1

# Calcula o tempo de contribuição...

inicio_contribuicao = datetime.strptime(data_inicio_contribuicao, "%d/%m/%Y")

tempo_contribuicao_atual = data_atual.year - inicio_contribuicao.year

if (data_atual.month, data_atual.day) < (inicio_contribuicao.month, inicio_contribuicao.day):
    tempo_contribuicao_atual -= 1

# Calcula a data de aposentadoria por idade...

data_aposentadoria_idade = nascimento.replace(year=nascimento.year + idade_aposentadoria)

# Calcula a data de aposentadoria por tempo de contribuição...

data_aposentadoria_contribuicao = inicio_contribuicao.replace(year=inicio_contribuicao.year + tempo_contribuicao_aposentadoria)

# Avalia se já cumpre os requisitos...

if idade_atual >= idade_aposentadoria and tempo_contribuicao_atual >= contribuicao_minima:
    print("Você já pode se aposentar por idade.")

elif tempo_contribuicao_atual >= tempo_contribuicao_aposentadoria:
    print("Você já pode se aposentar por tempo de contribuição.")

else:
    # Determina a menor data de aposentadoria...

    data_final = min(data_aposentadoria_idade, data_aposentadoria_contribuicao)
    print(f"Você poderá se aposentar em: {data_final.strftime('%d/%m/%Y')}")
