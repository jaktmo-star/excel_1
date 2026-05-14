# 📊 Análise de Dados de Vendas com Python

Projeto desenvolvido em Python para realizar a leitura de uma planilha Excel e gerar um resumo das quantidades vendidas por produto utilizando a biblioteca `pandas`.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- Excel (.xlsx)

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
- Agrupamento de dados por:
  - ID do Produto
  - Nome do Produto
- Soma total da quantidade vendida
- Exibição formatada dos resultados no terminal

---

## 🧠 Código utilizado

```python
# Autor: Elcio Mello
# Projeto: Análise de dados de Excel

# Import do pandas
import pandas as pd

# Ler a planilha do Excel
planilha = pd.read_excel('vendas.xlsx')

# Agrupar os registros por nome
resultado = planilha.groupby(["ID_Produto", "Nome_Produto"])["Quantidade_Vendida"].sum()

# Loop para exibir os resultados
for (produto, nome), quantidade in resultado.items():
    print(f"Produto: {produto} | Nome do Produto: {nome} | Quantidade Vendida: {quantidade}")
```

---

## ▶️ Como executar o projeto

### 1️⃣ Instale o Python

Baixe em: https://www.python.org

---

### 2️⃣ Instale as bibliotecas necessárias

```bash
pip install pandas openpyxl
```

---

### 3️⃣ Execute o projeto

```bash
python analise_vendas.py
```

---

## 📊 Exemplo de saída

```bash
Produto: 101 | Nome do Produto: Mouse Gamer | Quantidade Vendida: 25
Produto: 102 | Nome do Produto: Teclado Mecânico | Quantidade Vendida: 18
Produto: 103 | Nome do Produto: Headset | Quantidade Vendida: 12
```

---

## 👨‍💻 Autor

Desenvolvido por **Elcio Mello**  
