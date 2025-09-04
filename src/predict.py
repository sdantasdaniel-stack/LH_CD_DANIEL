import pandas as pd
import re, joblib, numpy as np, pandas as pd, sklearn
from copy import deepcopy


## Arquivo para gerar a previsao do filme informado (explicar no readme.md)

# carregar modelo treinado
model = joblib.load("../models/model_imdb_pipeline.pkl")

# filme de exemplo
novo_filme = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}

# criar dataframe com uma linha
df_novo = pd.DataFrame([novo_filme])

# aplicar as mesmas transformações que no treino
from copy import deepcopy

def parse_runtime_to_min(x):
    if pd.isna(x): return np.nan
    m = re.search(r"(\d+)", str(x))
    return float(m.group(1)) if m else np.nan

def parse_gross_to_usd(x):
    if pd.isna(x): return np.nan
    s = re.sub(r"[^\d]", "", str(x))
    return float(s) if s else np.nan

##Funcao que nao existe nesse arquivo, preciso importar de algum lugar
def build_features(df):
    d = df.copy()
    if "Runtime" in d: d["Runtime_min"] = d["Runtime"].apply(parse_runtime_to_min)
    if "Gross" in d:   d["Gross_USD"]   = d["Gross"].apply(parse_gross_to_usd)
    if "Released_Year" in d: d["Released_Year"] = pd.to_numeric(d["Released_Year"], errors="coerce")
    if "Genre" in d:
        d["Primary_Genre"] = d["Genre"].fillna("").apply(lambda x: str(x).split(",")[0].strip() if x else np.nan)
    if "No_of_Votes" in d: d["log_votes"] = np.log1p(d["No_of_Votes"])
    if "Gross_USD" in d:   d["log_gross"] = np.log1p(d["Gross_USD"])
    return d

df_novo_proc = build_features(df_novo)

# prever nota
pred = model.predict(df_novo_proc)[0]
print(f"Previsão de IMDB_Rating para '{novo_filme['Series_Title']}': {pred:.2f}")
