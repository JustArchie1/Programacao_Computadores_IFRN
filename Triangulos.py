import math

# Pedir pela medida dos lados...
lado_a = float(input("Informe a medida do primeiro lado do triângulo: "))
lado_b = float(input("Informe a medida do segundo lado do triângulo: "))
lado_c = float(input("Informe a medida do terceiro lado do triângulo: "))

# Verificar se os lados podem formar um triângulo...

if lado_a + lado_b <= lado_c or lado_c + lado_b <= lado_a or lado_c + lado_a <= lado_b:
    print("As medidas informadas não podem formar um triângulo.")
    
else:
    # Calcular os ângulos usando a fórmula do cosseno...

    angulo_a = math.acos((lado_b**2 + lado_c**2 - lado_a**2) / (2 * lado_b * lado_c))
    angulo_b = math.acos((lado_a**2 + lado_c**2 - lado_b**2) / (2 * lado_a * lado_c))
    angulo_c = math.acos((lado_b**2 + lado_a**2 - lado_c**2) / (2 * lado_a * lado_b))

    # Converter os ângulos de radianos para graus...

    angulo_a = math.degrees(angulo_a)
    angulo_b = math.degrees(angulo_b)
    angulo_c = math.degrees(angulo_c)

    # Classificação quanto aos lados...

    if lado_a == lado_b == lado_c:
        classificacao_lado = "Equilátero"

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        classificacao_lado = "Isósceles"

    else:
        classificacao_lado = "Escaleno"

    # Classificação quanto aos ângulos...

    if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
        classificacao_angulo = "Retângulo"

    elif angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
        classificacao_angulo = "Obtuso"

    else:
        classificacao_angulo = "Agudo"

    # Exibir os resultados...

    print("Classificação quanto aos lados:", classificacao_lado)
    print("Classificação quanto aos ângulos:", classificacao_angulo)
    print(f"Ângulos do triângulo: {angulo_a:.2f}°, {angulo_b:.2f}°, {angulo_c:.2f}°")
