# 📊 Sistema de Análise de Vendas com Interface Gráfica

Projeto desenvolvido em Python com interface moderna utilizando `CustomTkinter` para realizar a leitura e análise de dados de uma planilha Excel.

O sistema agrupa os produtos vendidos e exibe as quantidades totais de maneira organizada e visual.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- CustomTkinter
- OpenPyXL
- Excel (.xlsx)

---

## 🖥️ Interface do Sistema

O sistema possui uma interface gráfica moderna com:

- Tema escuro
- Botões personalizados
- Exibição organizada dos resultados
- Leitura automática da planilha Excel

---

## 📁 Estrutura do projeto

```bash
📂 projeto
 ├── vendas.xlsx
 ├── analise_vendas.py
 └── README.md
```

---

## 📌 Funcionalidades

- Leitura de arquivos Excel
- Interface gráfica moderna
- Agrupamento de dados por:
  - ID do Produto
  - Nome do Produto
- Soma total das quantidades vendidas
- Exibição formatada dos resultados na tela
- Tratamento de erros durante a leitura da planilha

---

## 🧠 Código principal

```python
# Ler planilha
planilha = pd.read_excel("vendas.xlsx")

# Agrupar dados
resultado = planilha.groupby(
    ["ID_Produto", "Nome_Produto"]
)["Quantidade_Vendida"].sum()

# Exibir resultados
for (produto, nome), quantidade in resultado.items():
    print(produto, nome, quantidade)
```

---

## ▶️ Como executar o projeto

### 1️⃣ Instale o Python

https://www.python.org

---

### 2️⃣ Instale as bibliotecas necessárias

```bash
pip install pandas openpyxl customtkinter
```

---

### 3️⃣ Execute o sistema

```bash
python analise_vendas.py
```

---

## 📊 Exemplo de funcionamento

```bash
Produto: 101
Nome: Mouse Gamer
Quantidade Vendida: 25
----------------------------------------

Produto: 102
Nome: Teclado Mecânico
Quantidade Vendida: 18
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- Manipulação de dados com Pandas
- Leitura de arquivos Excel
- Desenvolvimento de interfaces gráficas em Python
- Organização e apresentação de dados

---

## 👨‍💻 Autor

Desenvolvido por **Elcio Mello**  
