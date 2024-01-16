ph = 6
class cultura:
    def __init__(self, nome, ph_min, ph_max, prod1, prod2, prod3, prod4, N1, N2, N3, N4, PMB1, PMB2, PMB3, PMB4, PB1, PB2, PB3, PB4, PM1, PM2, PM3, PM4, PA1, PA2, PA3, PA4, PMA1, PMA2, PMA3, PMA4, PE1, PE2, PE3, PE4, KMB1, KMB2, KMB3, KMB4, KB1, KB2, KB3, KB4, KM1, KM2, KM3, KM4, KA1, KA2, KA3, KA4, KMA1, KMA2, KMA3, KMA4, KE1, KE2, KE3, KE4):
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
        
    def checkar_ph(self):
        if ph<= self.ph_max and ph >= self.ph_min:
            print("ph do solo adequado")
        else:
            print("ph do solo não adequado")
            
    def necessidades_de_nutrientes(self):
        prod_escolhida = input(f"Escolha a produção desejada em Ton/ha (Opções disponíveis: {self.prod1, self.prod2, self.prod3, self.prod4}): ")
        prod_escolhida = str(prod_escolhida)
        if prod_escolhida == str(self.prod1):
            print(f"Azoto Necessario em kg/ha: {self.N1}")
            if classe == 
        elif prod_escolhida == str(self.prod2):
            print(f"Azoto Necessario em kg/ha: {self.N2}")
        elif prod_escolhida == str(self.prod3):
            print(f"Azoto Necessario em kg/ha: {self.N3}")
        elif prod_escolhida == str(self.prod4):
            print(f"Azoto Necessario em kg/ha: {self.N4}")
        
        
    
#now for P and K we need to create all the possible outcomes which are a combination of fertility class and wanted production
#example: P_MB_1 Potassio necessario para solo com classe de fertilidade muito baixa e produção desejada 1  
            
Culturas= [
        
cultura(nome="Ervilha Fresca",ph_min=6, ph_max=7.5, prod1 = 7, prod2= 8, prod3 = 10, prod4 = 0, N1= 0, N2=10 , N3=40, N4=0 ), 
cultura(nome=" Beringela",ph_min=6.5, ph_max=7.5, prod1 =25 , prod2=35 , prod3 = 45, prod4 = 55, N1=100 , N2=130 , N3=160 , N4=180),
cultura(nome="Melancia",ph_min=6.5, ph_max=7.5, prod1 = 20, prod2=25 , prod3 =35 , prod4 = 0, N1=70, N2=90 , N3=135 , N4= 0),
cultura(nome="Beterraba de mesa",ph_min=6, ph_max=7, prod1 = 30, prod2=40 , prod3 = 50, prod4 = 0, N1= 90, N2= 120 , N3=150 , N4= 0 ),
]

for cultura in Culturas:
    print(cultura.nome)
    cultura.checkar_ph(), 
    cultura.necessidades_de_nutrientes()