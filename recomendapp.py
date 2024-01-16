import tkinter as tk
from tkinter import simpledialog, scrolledtext

# Função para calcular recomendações e exibir resultados
def calcular_recomendacoes():
    # Coletar respostas do usuário
    cultura_instalada = simpledialog.askstring("Pergunta", "A cultura já está instalada? (Responda: Sim ou Não)")
    chuva = simpledialog.askstring("Pergunta", "É provável ocorrer chuva neste mês? (Responda: Sim ou Não)")
    falta_oxigenio = simpledialog.askstring("Pergunta", "A sua cultura sofre alagamento? (Responda: Sim ou Não)")

    Tipo_de_fertilizantes = []
    Notas = []

    ph = 5

    for nutriente in nutrientes_sujeitos_a_tipo:
        if nutriente == "N":
            if cultura_instalada == "Não":
                Tipo_de_fertilizantes.append("NH4")
            elif cultura_instalada == "Sim":
                if chuva == "Sim":
                    if ph < 5.5:
                        Tipo_de_fertilizantes.append("NH4")
                    else:
                        Tipo_de_fertilizantes.append("NH4")
                        Notas.append("Enterrar fertilizante para evitar volatilização do NH3")
                elif chuva == "Não":
                    if falta_oxigenio == "Sim":
                        Tipo_de_fertilizantes.append("NH4")
                    elif falta_oxigenio == "Não":
                        Tipo_de_fertilizantes.append("NO3")
                        Tipo_de_fertilizantes.append("Ureia")
        elif nutriente == "P":
            if cultura_instalada == "Não":
                Tipo_de_fertilizantes.append("Fosfatos Naturais Moídos")
            elif cultura_instalada == "Sim":
                Tipo_de_fertilizantes.append("Fosforo_soluvel")
    nutrientes_formula  = ["N", "P", "K", "Ca", "Mg"]
    fertilizantes_recomendados = []

    for nutriente in nutrientes_formula:
        if nutriente == "N":
            if "NH4" in Tipo_de_fertilizantes:
                if ph < 5.5:
                    fertilizantes_recomendados.append("Sulfato_Amonio")
                else:
                    fertilizantes_recomendados.append("Cloreto_Amonio")
            elif "NO3" or "Ureia" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("Nitrato_Amonio")
                fertilizantes_recomendados.append("Nitrato_Calcio")
                fertilizantes_recomendados.append("Ureia")
        elif nutriente == "P":
            if "Fosfatos Naturais Moídos" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("rocha_fosfatada")
            elif "Fosforo_soluvel" in Tipo_de_fertilizantes: 
                fertilizantes_recomendados.append("Superfosfato_Normal")
                fertilizantes_recomendados.append("Superfosfato_triplo")
        elif nutriente == "K":
            fertilizantes_recomendados.append("Sulfato_potassio")
        elif nutriente == "Ca":
            fertilizantes_recomendados.append("Sulfato_calcio")
        elif nutriente == "Mg":
            fertilizantes_recomendados.append("Sulfato_magnesio")
            if "NO3" or "Ureia" in Tipo_de_fertilizantes:
                fertilizantes_recomendados.append("Nitrato_magnesio")
            
    # Limpar a caixa de texto de resultados
    resultado_texto.delete(1.0, tk.END)

    # Adicionar recomendações à caixa de texto de resultados
    resultado_texto.insert(tk.INSERT, "Fertilizantes Recomendados:\n")
    for fertilizante in fertilizantes_recomendados:
        resultado_texto.insert(tk.INSERT, f"- {fertilizante}\n")

    # Se houver notas, adicionar as notas à caixa de texto de resultados
    if Notas:
        resultado_texto.insert(tk.INSERT, "\nNotas:\n")
        for nota in Notas:
            resultado_texto.insert(tk.INSERT, f"- {nota}\n")

# Criar a janela principal
janela = tk.Tk()
janela.title("Questionário sobre Fertilizantes")

# Adicionar caixa de texto para exibir resultados
resultado_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=40, height=10)
resultado_texto.pack()

# Definir nutrientes_sujeitos_a_tipo e Notas aqui fora da função
nutrientes_sujeitos_a_tipo = ["N", "P"]
Notas = []

# Adicionar botão para calcular recomendações
botao_calcular = tk.Button(janela, text="Calcular Recomendações", command=calcular_recomendacoes)
botao_calcular.pack()

# Definir cor de fundo verde
janela.configure(bg="green")

# Adicionar cor branca ao texto
resultado_texto.configure(bg="green", fg="white")

# Iniciar o loop principal do tkinter
janela.mainloop()

