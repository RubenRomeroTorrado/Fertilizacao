print("Análises do solo")
print("Inserir valores abaixo:")
ph = float(input("pH:"))
fosforo_extraivel = float(input("Fósforo Extraível:"))
potassio_extraivel = float(input("Potássio Extraível:"))
magnesio = float(input("Magnésio:"))
materia_organica = float(input("materia_organica:"))

def classe_fertilidade_magnesio(magnesio):
    if magnesio < 30:
        return "MB"  # Muito Baixa
    elif 30 <= magnesio < 60:
        return "B"   # Baixa
    elif 60 <= magnesio < 90:
        return "M"   # Média
    elif 91 <= magnesio < 125:
        return "A"   # Alta
    elif magnesio >= 125:
        return "MA"  # Muito Alta




def classe_fertilidade_fosforo(fosforo_extraível):
    if fosforo_extraivel < 25:
        return "MB"  # Muito Baixa
    elif 25 <= fosforo_extraivel < 50:
        return "B"   # Baixa
    elif 50 <= fosforo_extraivel < 80:
        return "M"   # Média
    elif 80 <= fosforo_extraivel < 120:
        return "A"   # Alta
    elif 120 <= fosforo_extraivel < 150:
        return "MA"  # Muito Alta
    elif fosforo_extraivel>= 150:
        return "E"  # excesso

    
def classe_fertilidade_magnesio(magnesio):
    if magnesio < 30:
        return "MB"  # Muito Baixa
    elif 30 <= magnesio < 60:
        return "B"   # Baixa
    elif 60 <= magnesio < 90:
        return "M"   # Média
    elif 91 <= magnesio < 125:
        return "A"   # Alta
    elif magnesio >= 125:
        return "MA"  # Muito Alta
    
def classe_fertilidade_potassio():
    if potassio_extraivel < 25:
        return "MB"  # Muito Baixa
    elif 25 <= potassio_extraivel < 50:
        return "B"   # Baixa
    elif 50 <= potassio_extraivel < 80:
        return "M"   # Média
    elif 80 <= potassio_extraivel< 120:
        return "A"   # Alta
    elif 120 <= potassio_extraivel < 150:
        return "MA"  # Muito Alta
    elif potassio_extraivel >= 150:
        return "E"  # excesso

cultura_anterior = input("Qual foi a cultura anterior? 1-Beterraba sacarina com folhas incorporadas, 2- Cereais com palha incorporada, 3 - Couve-flor, brócolis ou bruxelas, 4- Prados temporários, 5- Prado luzerna, 6- Nenhuma das anteriores: ")

def azoto_deduzido_cultura_anterior(cultura_anterior):
    if cultura_anterior == '1':
        return -20
    elif cultura_anterior == '2':
        return +20
    elif cultura_anterior == '3':
        return -20
    elif cultura_anterior == '4':
        return -20
    elif cultura_anterior == '5':
        return -40
    elif cultura_anterior == '6':
        return 0
    else:
        return 0


def calcular_azoto_deduzido(materia_organica):
    if materia_organica <= 2.5:
        return 0
    elif 2.51 <= materia_organica <= 5.99:
        reducao_kgs = int((materia_organica - 2.5) / 0.5) * 10
        return reducao_kgs
    else:
        return 60

azoto_deduzido = calcular_azoto_deduzido(materia_organica)
print(azoto_deduzido)


resultado_classe_Mg = classe_fertilidade_magnesio(magnesio)
resultado_classe_P = classe_fertilidade_fosforo(fosforo_extraivel)
resultado_classe_K = classe_fertilidade_magnesio(potassio_extraivel)

print(resultado_classe_K, resultado_classe_Mg, resultado_classe_P)