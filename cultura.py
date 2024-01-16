ph = 6
class cultura:
    def __init__(self, nome, ph_min, ph_max, prod1, prod2, prod3, prod4, N1, N2, N3, N4):
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
        elif prod_escolhida == str(self.prod2):
            print(f"Azoto Necessario em kg/ha: {self.N2}")
        elif prod_escolhida == str(self.prod3):
            print(f"Azoto Necessario em kg/ha: {self.N3}")
        elif prod_escolhida == str(self.prod4):
            print(f"Azoto Necessario em kg/ha: {self.N4}")
    

            
Culturas= [
        
cultura(nome="Ervilha Fresca",ph_min=6, ph_max=7.5, prod1 = 7, prod2= 8, prod3 = 10, prod4 = 0, N1= 0, N2=10 , N3=40, N4=0 ), 
cultura(nome=" Beringela",ph_min=6.5, ph_max=7.5, prod1 =25 , prod2=35 , prod3 = 45, prod4 = 55, N1=100 , N2=130 , N3=160 , N4=180),
cultura(nome="Melancia",ph_min=6.5, ph_max=7.5, prod1 = 20, prod2=25 , prod3 =35 , prod4 = 0, N1=70, N2=90 , N3=135 , N4= 0),
cultura(nome="Beterraba de mesa",ph_min=6, ph_max=7, prod1 = 30, prod2=40 , prod3 = 50, prod4 = 0, N1= 90, N2= 120 , N3=150 , N4= 0 ),
]

for cultura in Culturas:
    cultura.checkar_ph(), 
    cultura.necessidades_de_nutrientes()