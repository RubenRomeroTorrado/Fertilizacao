def main():
    print("Análises do solo")
    print("Inserir valores abaixo:")
    ph = float(input("pH:"))
    fosforo_extraivel = float(input("Fósforo Extraível:"))
    potassio_extraivel = float(input("Potássio Extraível:"))
    magnesio = float(input("Magnésio:"))
    materia_organica = float(input("materia_organica:"))

    classe_fertilidade_magnesio(magnesio)
    classe_fertilidade_fosforo(fosforo_extraivel) 
    classe_fertilidade_potassio(potassio_extraivel)

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
    resultado_classe_K = classe_fertilidade_potassio(potassio_extraivel)
    class cultura:
        def __init__(self, nome, ph_min, ph_max, prod1, prod2, prod3, prod4, N1, N2, N3, N4, PMB1, PMB2, PMB3, PMB4, PB1, PB2, PB3, PB4, PM1, PM2, PM3, PM4, PA1, PA2, PA3, PA4, PMA1, PMA2, PMA3, PMA4, PE1, PE2, PE3, PE4, KMB1, KMB2, KMB3, KMB4, KB1, KB2, KB3, KB4, KM1, KM2, KM3, KM4, KA1, KA2, KA3, KA4, KMA1, KMA2, KMA3, KMA4, KE1, KE2, KE3, KE4, MgMb, MgB, MgM, MgA):
            self.nome = nome
            self.ph_min = ph_min
            self.ph_max = ph_max
            self.prod1 = prod1
            self.prod2 = prod2
            self.prod3 = prod3
            self.prod4 = prod4
            self.N1 = N1
            self.N2 = N2
            self.N3 = N3
            self.N4 = N4
            self.PMB1 = PMB1
            self.PMB2 = PMB2
            self.PMB3 = PMB3
            self.PMB4 = PMB4
            self.PB1 = PB1
            self.PB2 = PB2
            self.PB3 = PB3
            self.PB4 = PB4
            self.PM1 = PM1
            self.PM2 = PM2
            self.PM3 = PM3
            self.PM4 = PM4
            self.PA1 = PA1
            self.PA2 = PA2
            self.PA3 = PA3
            self.PA4 = PA4
            self.PMA1 = PMA1
            self.PMA2 = PMA2
            self.PMA3 = PMA3
            self.PMA4 = PMA4
            self.PE1 = PE1
            self.PE2 = PE2
            self.PE3 = PE3
            self.PE4 = PE4
            self.KMB1 = KMB1
            self.KMB2 = KMB2
            self.KMB3 = KMB3
            self.KMB4 = KMB4
            self.KB1 = KB1
            self.KB2 = KB2
            self.KB3 = KB3
            self.KB4 = KB4
            self.KM1 = KM1
            self.KM2 = KM2
            self.KM3 = KM3
            self.KM4 = KM4
            self.KA1 = KA1
            self.KA2 = KA2
            self.KA3 = KA3
            self.KA4 = KA4
            self.KMA1 = KMA1
            self.KMA2 = KMA2
            self.KMA3 = KMA3
            self.KMA4 = KMA4
            self.KE1 = KE1
            self.KE2 = KE2
            self.KE3 = KE3
            self.KE4 = KE4
            self.MgMb = MgMb
            self.MgB = MgB
            self.MgM = MgM
            self.MgA = MgA
            
        def checkar_ph(self):
            if ph<= self.ph_max and ph >= self.ph_min:
                print("ph do solo adequado")
            else:
                print("ph do solo não adequado")
                
        def necessidades_de_nutrientes(self):
            prod_escolhida = input(f"Escolha a produção desejada em Ton/ha (Opções disponíveis: {self.prod1, self.prod2, self.prod3, self.prod4}): ")
            prod_escolhida = str(prod_escolhida)
            if prod_escolhida == str(self.prod1):
                azoto_necessario=self.N1
                if resultado_classe_Mg == "MB":
                    magnesio_necessario= self.MgMb
                elif resultado_classe_Mg == "B":
                    magnesio_necessario= self.MgB
                elif resultado_classe_Mg == "M":
                    magnesio_necessario= self.MgM
                else:
                    magnesio_necessario= self.MgA
                if resultado_classe_P == "MB":
                    fosforo_necessario = self.PMB1
                elif resultado_classe_P == "B":
                    fosforo_necessario = self.PB1
                elif resultado_classe_P == "M":
                    fosforo_necessario = self.PM1
                elif resultado_classe_P == "A":
                    fosforo_necessario = self.PA1
                elif resultado_classe_P == "MA":
                    fosforo_necessario = self.PMA1
                elif resultado_classe_P == "E":
                    fosforo_necessario = self.PE1
                if resultado_classe_K == "MB": #potassio
                    potassio_necessario = self.KMB1
                elif resultado_classe_K == "B":
                    potassio_necessario = self.KB1
                elif resultado_classe_K == "M":
                    potassio_necessario = self.KM1
                elif resultado_classe_K == "A":
                    potassio_necessario = self.KA1
                elif resultado_classe_K == "MA":
                    potassio_necessario = self.KMA1
                elif resultado_classe_K == "E":
                    potassio_necessario = self.KE1
                return azoto_necessario, magnesio_necessario, fosforo_necessario, potassio_necessario
            elif prod_escolhida == str(self.prod2):
                azoto_necessario=self.N2
                if resultado_classe_Mg == "MB":
                    magnesio_necessario= self.MgMb
                elif resultado_classe_Mg == "B":
                    magnesio_necessario= self.MgB
                elif resultado_classe_Mg == "M":
                    magnesio_necessario= self.MgM
                else:
                    magnesio_necessario= self.MgA
                if resultado_classe_P == "MB":
                    fosforo_necessario = self.PMB2
                elif resultado_classe_P == "B":
                    fosforo_necessario = self.PB2
                elif resultado_classe_P == "M":
                    fosforo_necessario = self.PM2
                elif resultado_classe_P == "A":
                    fosforo_necessario = self.PA2
                elif resultado_classe_P == "MA":
                    fosforo_necessario = self.PMA2
                elif resultado_classe_P == "E":
                    fosforo_necessario = self.PE2
                if resultado_classe_K == "MB": #potassio
                    potassio_necessario = self.KMB2
                elif resultado_classe_K == "B":
                    potassio_necessario = self.KB2
                elif resultado_classe_K == "M":
                    potassio_necessario = self.KM2
                elif resultado_classe_K == "A":
                    potassio_necessario = self.KA2
                elif resultado_classe_K == "MA":
                    potassio_necessario = self.KMA2
                elif resultado_classe_K == "E":
                    potassio_necessario = self.KE2
                return azoto_necessario, magnesio_necessario, fosforo_necessario, potassio_necessario
            elif prod_escolhida == str(self.prod3):
                azoto_necessario=self.N3
                if resultado_classe_Mg == "MB":
                    magnesio_necessario= self.MgMb
                elif resultado_classe_Mg == "B":
                    magnesio_necessario= self.MgB
                elif resultado_classe_Mg == "M":
                    magnesio_necessario= self.MgM
                else:
                    magnesio_necessario= self.MgA
                if resultado_classe_P == "MB":
                    fosforo_necessario = self.PMB3
                elif resultado_classe_P == "B":
                    fosforo_necessario = self.PB3
                elif resultado_classe_P == "M":
                    fosforo_necessario = self.PM3
                elif resultado_classe_P == "A":
                    fosforo_necessario = self.PA3
                elif resultado_classe_P == "MA":
                    fosforo_necessario = self.PMA3
                elif resultado_classe_P == "E":
                    fosforo_necessario = self.PE3
                if resultado_classe_K == "MB": #potassio
                    potassio_necessario = self.KMB3
                elif resultado_classe_K == "B":
                    potassio_necessario = self.KB3
                elif resultado_classe_K == "M":
                    potassio_necessario = self.KM3
                elif resultado_classe_K == "A":
                    potassio_necessario = self.KA3
                elif resultado_classe_K == "MA":
                    potassio_necessario = self.KMA3
                elif resultado_classe_K == "E":
                    potassio_necessario = self.KE3
                return azoto_necessario, magnesio_necessario, fosforo_necessario, potassio_necessario
            elif prod_escolhida == str(self.prod4):
                print(f"Azoto Necessario em kg/ha: {self.N4}")
                azoto_necessario=self.N4
                if resultado_classe_Mg == "MB":
                    magnesio_necessario= self.MgMb
                elif resultado_classe_Mg == "B":
                    magnesio_necessario= self.MgB
                elif resultado_classe_Mg == "M":
                    magnesio_necessario= self.MgM
                else:
                    magnesio_necessario= self.MgA
                if resultado_classe_P == "MB":
                    fosforo_necessario = self.PMB4
                elif resultado_classe_P == "B":
                    fosforo_necessario = self.PB4
                elif resultado_classe_P == "M":
                    fosforo_necessario = self.PM4
                elif resultado_classe_P == "A":
                    fosforo_necessario = self.PA4
                elif resultado_classe_P == "MA":
                    fosforo_necessario = self.PMA4
                elif resultado_classe_P == "E":
                    fosforo_necessario = self.PE4
                if resultado_classe_K == "MB": #potassio
                    potassio_necessario = self.KMB4
                elif resultado_classe_K == "B":
                    potassio_necessario = self.KB4
                elif resultado_classe_K == "M":
                    potassio_necessario = self.KM4
                elif resultado_classe_K == "A":
                    potassio_necessario = self.KA4
                elif resultado_classe_K == "MA":
                    potassio_necessario = self.KMA4
                elif resultado_classe_K == "E":
                    potassio_necessario = self.KE4
            
                return azoto_necessario, magnesio_necessario, fosforo_necessario, potassio_necessario   
            
        
    #now for P and K we need to create all the possible outcomes which are a combination of fertility class and wanted production
    #example: P_MB_1 Potassio necessario para solo com classe de fertilidade muito baixa e produção desejada 1  
                
    Culturas = [        
    cultura(nome="Ervilha Fresca",ph_min=6, ph_max=7.5, prod1 = 7, prod2= 8, prod3 = 10, prod4 = 0, N1= 0, N2=10 , N3=40, N4=0,PMB1=120, PMB2=140, PMB3=150, PMB4=0, PB1=100, PB2=120, PB3=140, PB4=0, PM1=80, PM2=100, PM3=120, PM4=0, PA1=60, PA2=80, PA3=100, PA4=0, PMA1=40, PMA2=60, PMA3=80, PMA4=0, PE1=0, PE2=0, PE3=60, PE4=0, KMB1=100, KMB2=120, KMB3=140, KMB4=0, KB1=80, KB2=100, KB3=120, KB4=0, KM1=60, KM2=80, KM3=100, KM4=0, KA1=40, KA2=60, KA3=80, KA4=0, KMA1=40, KMA2=60, KMA3=80, KMA4=0, KE1=0, KE2=0, KE3=0, KE4=0, MgMb=35, MgB=25, MgM=10, MgA=0), 
    cultura(nome="Beringela",ph_min=6.5, ph_max=7.5, prod1 =25 , prod2=35 , prod3 = 45, prod4 = 55, N1=100 , N2=130 , N3=160 , N4=180, PMB1=125, PMB2=150, PMB3=180, PMB4=220, PB1=100, PB2=125, PB3=150, PB4=190, PM1=75, PM2=100, PM3=120, PM4=160, PA1=50, PA2=75, PA3=100, PA4=130, PMA1=40, PMA2=50, PMA3=60, PMA4=90, PE1=0, PE2=0, PE3=0, PE4=0, KMB1=140, KMB2=180, KMB3=220, KMB4=240, KB1=120, KB2=150, KB3=180, KB4=200, KM1=100, KM2=120, KM3=140, KM4=160, KA1=80, KA2=100, KA3=120, KA4=140, KMA1=60, KMA2=80, KMA3=100, KMA4=120, KE1=30, KE2=40, KE3=50, KE4=80, MgMb=50, MgB=35, MgM=25, MgA=20),
    cultura(nome="Melancia",ph_min=6.5, ph_max=7.5, prod1 = 20, prod2=25 , prod3 =35 , prod4 = 0, N1=70, N2=90 , N3=135 , N4= 0, PMB1=120, PMB2=160, PMB3=220, PMB4=0, PB1=80, PB2=120, PB3=160, PB4=0, PM1=60, PM2=80, PM3=120, PM4=0, PA1=40, PA2=60, PA3=80, PA4=0, PMA1=0, PMA2=40, PMA3=60, PMA4=0, PE1=0, PE2=0, PE3=0, PE4=0, KMB1=140, KMB2=160, KMB3=220, KMB4=0, KB1=100, KB2=140, KB3=160, KB4=0, KM1=80, KM2=120, KM3=140, KM4=0, KA1=60, KA2=100, KA3=120, KA4=0, KMA1=40, KMA2=60, KMA3=80, KMA4=0, KE1=0, KE2=0, KE3=0, KE4=0, MgMb=35, MgB=25, MgM=10, MgA=0),
    cultura(nome="Beterraba de mesa",ph_min=6, ph_max=7, prod1 = 30, prod2=40 , prod3 = 50, prod4 = 0, N1= 90, N2= 120 , N3=150 , N4= 0, PMB1=130, PMB2=150, PMB3=170, PMB4=0, PB1=110, PB2=130, PB3=150, PB4=0, PM1=90, PM2=110, PM3=130, PM4=0, PA1=70, PA2=90, PA3=110, PA4=0, PMA1=30, PMA2=40, PMA3=50, PMA4=0, PE1=0, PE2=0, PE3=0, PE4=0, KMB1=160, KMB2=180, KMB3=210, KMB4=0, KB1=125, KB2=140, KB3= 180, KB4=0, KM1=95, KM2=110, KM3=140, KM4=0, KA1=70, KA2=90, KA3=110, KA4=0, KMA1=40, KMA2=40, KMA3=50, KMA4=0, KE1=0, KE2=0, KE3=0, KE4=0, MgMb=50, MgB=35, MgM=25, MgA=20 )
    ]


    resultados_nutrientes_dict = {}

    for cultura_instancia in Culturas:
        print(cultura_instancia.nome)
        cultura_instancia.checkar_ph()
        resultados_nutrientes = cultura_instancia.necessidades_de_nutrientes()
        azoto_necessario, magnesio_necessario, fosforo_necessario, potassio_necessario = resultados_nutrientes

        # Armazenar as variáveis no dicionário usando o nome da cultura como chave
        resultados_nutrientes_dict[cultura_instancia.nome] = {
            'azoto_necessario': azoto_necessario,
            'magnesio_necessario': magnesio_necessario,
            'fosforo_necessario': fosforo_necessario,
            'potassio_necessario': potassio_necessario
        }

    nome_cultura_desejada = input("Selecione a seguinte Cultura: (Ervilha Fresca, Beringela, Melancia, Beterraba de mesa) ")

    if nome_cultura_desejada in resultados_nutrientes_dict:
        variaveis_cultura_desejada = resultados_nutrientes_dict[nome_cultura_desejada]

        azoto_necessario_cultura = variaveis_cultura_desejada['azoto_necessario']
        magnesio_necessario_cultura = variaveis_cultura_desejada['magnesio_necessario']
        fosforo_necessario_cultura = variaveis_cultura_desejada['fosforo_necessario']
        potassio_necessario_cultura = variaveis_cultura_desejada['potassio_necessario']
        


    #recomendar tipo de fertilizante para N e P

    nutrientes_sujeitos_a_tipo  = ["N", "P"]

    Tipo_de_fertilizantes=[]

    cultura_instalada = input("A cultura já está instalada? (Responda: Sim ou Não) ").lower()

    Notas=[]


    for nutriente in nutrientes_sujeitos_a_tipo:
        if nutriente == "N":
            if cultura_instalada == "não":
                Tipo_de_fertilizantes.append("NH4")
            elif cultura_instalada == "sim":
                Chuva = input("É provavel ocorrer chuva neste mês? (Responda: Sim ou Não) ").lower()
                if Chuva == "sim":
                    if ph < 5.5:
                        Tipo_de_fertilizantes.append("NH4")
                    else:
                        Tipo_de_fertilizantes.append("NH4")
                        Notas.append("Enterrar fertilizante para evitar volatilização do NH3")
                elif Chuva == "não":
                    falta_oxigenio = input("A sua cultura sofre alagamento? (Responda: Sim ou Não) ").lower()
                    if falta_oxigenio == "sim":
                        Tipo_de_fertilizantes.append("NH4")
                    elif falta_oxigenio == "não":
                        Tipo_de_fertilizantes.append("NO3")
                        Tipo_de_fertilizantes.append("Ureia")
        elif nutriente == "P":
            if cultura_instalada == "não":
                Tipo_de_fertilizantes.append("Fosfatos Naturais Moídos")
            elif cultura_instalada == "sim":
                Tipo_de_fertilizantes.append("Fosforo_soluvel")
                            

                    
                #recomendar formula de fertilizante para N,P,K,Ca,Mg

    nutrientes_formula  = ["N", "P", "K", "Ca", "Mg"]
    fertilizantes_recomendados = []

    for nutriente in nutrientes_formula:
        if nutriente == "N":
            if "NH4" in Tipo_de_fertilizantes:
                if 4<ph < 6.1:
                    fertilizantes_recomendados.append("Sulfato_Amonio")
            elif "NO3" or "Ureia" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("Nitrato_Amonio")
                fertilizantes_recomendados.append("Ureia")
        elif nutriente == "P":
            if "Fosfatos Naturais Moídos" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("rocha_fosfatada")
            elif "Fosforo_soluvel" in Tipo_de_fertilizantes: 
                fertilizantes_recomendados.append("Superfosfato_Normal")
                fertilizantes_recomendados.append("Superfosfato_triplo")
        elif nutriente == "K":
            fertilizantes_recomendados.append("Sulfato_potassio")
            if "NO3" or "Ureia" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("Nitrato_potassio")
        elif nutriente == "Ca":
            fertilizantes_recomendados.append("Nitrato_Calcio")
        elif nutriente == "Mg":
            fertilizantes_recomendados.append("Sulfato_magnesio")
            if "NO3" or "Ureia" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("Nitrato_magnesio")
            


    class Fertilizante:
        def __init__(self, nome, N, P2O5, K2O, CaO, MgO, SO3, preco):
            self.nome = nome
            self.N = N
            self.P2O5 = P2O5
            self.K2O = K2O
            self.CaO = CaO
            self.MgO = MgO
            self.SO3 = SO3
            self.preco = preco

    Fertilizantes= [
        
    Fertilizante(nome="Sulfato_Amonio", N = 21.2, P2O5= 0, K2O= 0, CaO=0, MgO=0, SO3=60.6, preco=0.276 ),

    Fertilizante(nome="Nitrato_Calcio", N = 15.6, P2O5= 0, K2O= 0, CaO=26, MgO=0, SO3=0, preco= 0.326),

    Fertilizante(nome="Nitrato_Amonio", N = 32.4, P2O5= 0, K2O= 0, CaO=0, MgO=0, SO3=0, preco= 0.43),

    Fertilizante(nome="Sulfato_magnesio", N = 0, P2O5= 0, K2O= 0, CaO=0, MgO=15.9/1.66, SO3=31.8, preco=0.6 ),

    Fertilizante(nome="Nitrato_magnesio", N = 11, P2O5= 0, K2O= 0, CaO=0, MgO=15.77/1.66, SO3=0, preco=  0.6),

    Fertilizante(nome="Nitrato_potassio", N = 13.8, P2O5= 0, K2O= 46.5, CaO=0, MgO=0, SO3=0, preco= 0.9),

    Fertilizante(nome="Sulfato_potassio", N = 0, P2O5= 0, K2O= 52.1, CaO=0, MgO=0, SO3=44.1, preco=0.718 ),

    Fertilizante(nome="Ureia", N = 46, P2O5= 0, K2O= 0, CaO=0, MgO=0, SO3=0, preco=0.48 ),

    Fertilizante(nome="Superfosfato_Normal", N = 0, P2O5= 18, K2O= 0, CaO=32.2, MgO=0, SO3=30, preco= 0.23),

    Fertilizante(nome="Superfosfato_triplo", N = 0, P2O5= 42, K2O= 0, CaO=22.4, MgO=0, SO3=5, preco=0.428 ),

    Fertilizante(nome="rocha_fosfatada", N = 0, P2O5= 33.4, K2O= 0, CaO=45.4, MgO=0, SO3=0, preco= 0.345)

    ]

    quantidade_aplicar_azoto = (azoto_necessario_cultura + azoto_deduzido_cultura_anterior(cultura_anterior) - azoto_deduzido)

    # Criar uma lista de instâncias de fertilizantes que estejam incluídos na lista de fertilizantes recomendados para poder ter acesso aos atributos dos objetos
    fertilizantes_selecionados = [Fertilizante for Fertilizante in Fertilizantes if Fertilizante.nome in fertilizantes_recomendados]

    fertilizante_max_nutriente_N = max(fertilizantes_selecionados, key=lambda x: getattr(x, "N"))
    fertilizante_max_nutriente_P = max(fertilizantes_selecionados, key=lambda x: getattr(x, "P2O5"))
    fertilizante_max_nutriente_K = max(fertilizantes_selecionados, key=lambda x: getattr(x, "K2O"))
    fertilizante_max_nutriente_Mg = max(fertilizantes_selecionados, key=lambda x: getattr(x, "MgO"))
    #obter percentagem e quantidade de fertilizantes com maior taxa de cada nutriente 
    percentagem_mg = getattr(fertilizante_max_nutriente_Mg, "MgO")
    quantidade_de_fertilizante_mg = (magnesio_necessario_cultura * 100) / percentagem_mg

    percentagem_k20 = getattr(fertilizante_max_nutriente_K, "K2O")
    quantidade_de_fertilizante_k2O = (potassio_necessario_cultura * 100) / percentagem_k20

    percentagem_p205 = getattr(fertilizante_max_nutriente_P, "P2O5")
    quantidade_de_fertilizante_p2o5 = (fosforo_necessario_cultura * 100) / percentagem_p205

    percentagem_N = getattr(fertilizante_max_nutriente_N, "N")
    quantidade_de_fertilizante_N = (quantidade_aplicar_azoto * 100) / percentagem_N



    print(f"Deve adubar com {fertilizante_max_nutriente_N.nome}, a seguinte quantidade: {round(quantidade_de_fertilizante_N)} kg/ha")
    print(f"Deve adubar com {fertilizante_max_nutriente_P.nome}, a seguinte quantidade: {round(quantidade_de_fertilizante_p2o5)} kg/ha")
    print(f"Deve adubar com {fertilizante_max_nutriente_K.nome}, a seguinte quantidade: {round(quantidade_de_fertilizante_k2O)} kg/ha")
    print(f"Deve adubar com {fertilizante_max_nutriente_Mg.nome}, a seguinte quantidade: {round(quantidade_de_fertilizante_mg)} kg/ha")
    
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
    if fosforo_extraível < 25:
        return "MB"  # Muito Baixa
    elif 25 <= fosforo_extraível < 50:
        return "B"   # Baixa
    elif 50 <= fosforo_extraível < 80:
        return "M"   # Média
    elif 80 <= fosforo_extraível < 120:
        return "A"   # Alta
    elif 120 <= fosforo_extraível < 150:
        return "MA"  # Muito Alta
    elif fosforo_extraível>= 150:
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
        
def classe_fertilidade_potassio(potassio_extraivel):
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

    
if __name__ == "__main__":
    main()
