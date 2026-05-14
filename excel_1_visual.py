# Autor: Elcio Mello
# Projeto: Análise de Dados de Excel

# Bibliotecas
import customtkinter as ctk
import pandas as pd

# Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela
app = ctk.CTk()
app.title("Análise de Vendas")
app.geometry("800x600")

# Função
def analisar_vendas():
    try:
        # Ler planilha
        planilha = pd.read_excel("vendas.xlsx")

        # Agrupar dados
        resultado = planilha.groupby(
            ["ID_Produto", "Nome_Produto"]
        )["Quantidade_Vendida"].sum()

        # Texto final
        texto = ""

        for (produto, nome), quantidade in resultado.items():
            texto += (
                f"Produto: {produto}\n"
                f"Nome: {nome}\n"
                f"Quantidade Vendida: {quantidade}\n"
                f"{'-'*40}\n"
            )

        resultado_label.configure(text=texto)

    except Exception as erro:
        resultado_label.configure(
            text=f"Erro ao ler a planilha:\n{erro}"
        )

# Título
titulo = ctk.CTkLabel(
    app,
    text="Análise de Vendas Excel",
    font=("Arial", 24),
    text_color="#D60031"
)

titulo.pack(pady=20)

# Botão
botao = ctk.CTkButton(
    app,
    text="Analisar Planilha",
    width=300,
    height=40,
    fg_color="#1f7fa5",
    hover_color="#702314",
    corner_radius=10,
    command=analisar_vendas
)

botao.pack(pady=20)

# Resultado
resultado_label = ctk.CTkLabel(
    app,
    text="Os resultados aparecerão aqui",
    font=("Arial", 16),
    justify="left"
)

resultado_label.pack(pady=20)

# Executar
app.mainloop()