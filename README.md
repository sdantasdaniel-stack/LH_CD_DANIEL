# Projeto de Previsão de Notas do IMDB

Este projeto foi desenvolvido como parte de um desafio de Ciência de Dados.  
O objetivo é analisar um banco de dados de filmes e construir um modelo preditivo capaz de estimar a **nota IMDB** de novos filmes, com base em suas características.

---

## Estrutura do repositório

├── data/                # Bases de dados originais e externas  
│   ├── desafio_indicium_imdb.csv  
│   └── orcamentos_filmes.csv  
├── models/              # Modelos treinados (salvos com joblib)  
│   └── model_imdb_pipeline.pkl  
├── notebooks/           # Notebooks de exploração e modelagem  
│   └── notebook.ipynb  
├── src/                 # Código fonte  
│   └── predict.py       # Script para previsões  
├── requirements.txt     # Dependências do projeto  
└── README.md            # Documentação  

---

## Configuração do ambiente

1. **Clonar o repositório**  
   git clone https://github.com/sdantasdaniel-stack/LH_CD_DANIEL.git  
   cd LH_CD_DANIEL  

2. **Criar o ambiente virtual**  
   python -m venv venv  

3. **Ativar o ambiente virtual**  
   - Windows (PowerShell):  
     .\venv\Scripts\Activate.ps1  
   - Linux/Mac:  
     source venv/bin/activate  

4. **Instalar as dependências**  
   pip install -r requirements.txt  

---

## Análise e modelagem

A análise exploratória e o processo de modelagem estão documentados em:

`notebooks/notebook.ipynb`

Nele você encontrará:  
- Tratamento de dados  
- Criação de variáveis derivadas  
- Análises exploratórias  
- Comparação de modelos de machine learning  
- Salvamento do pipeline completo em `models/model_imdb_pipeline.pkl`  

---

## Fazer previsões

O script `predict.py` permite prever a **nota IMDB** para novos filmes.

Exemplo de uso:  
python src/predict.py  

Saída esperada:  
Previsão de IMDB_Rating para 'The Shawshank Redemption': 8.12  

Dentro do `predict.py`, você pode alterar o dicionário `novo_filme` para inserir as informações do filme que deseja testar.

---

## Tecnologias utilizadas

- Python 3.12  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Joblib  

---

## Observações

- O modelo foi treinado com base em dados de filmes do IMDB e informações adicionais de orçamento.  
- O objetivo principal é **demonstrar o processo de análise e modelagem preditiva**, não necessariamente atingir a nota mais precisa possível.  
- Os gráficos e análises estão descritos no notebook, e comentários adicionais explicam cada etapa do pipeline.  
