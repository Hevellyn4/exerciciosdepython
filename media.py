nota1 = float(input("Informe a 1º nota: "))
nota2 = float(input("Informe a 2º nota: "))

media = (nota1 + nota2) / 2

if media<7 and media>4:
    print("A média é: %.1f - Final"% media)
elif media>7:
    print("A média é: %.1f - Aprovado"% media)
else:
    print("A média é: %.1f - Reprovado"& media)