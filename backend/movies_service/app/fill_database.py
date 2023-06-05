import pandas as pd

# Ler a planilha "Filmes" do arquivo Excel
df = pd.read_excel(r'backend\movies_service\app\planilha-dos-cinefilos-original-2-2.xlsx', sheet_name='Filmes')

# Converter para um dicionário
data_dict = df.to_dict(orient='list')
df["Ano"] = df["Ano"].astype(int)
df = df.drop(columns=['Assisti', 'Meu rank', 'Título original', 'Franquia', "AFI", 'Rada+', 'ICM', "Total"])
df = df.fillna(0)

df = df.rename(columns = {
    'Título em português': 'nome',
    'Diretor': 'diretor',
    'Ano': 'ano_lancamento',
    'País': 'pais',
    'Gênero': 'genero',
    'Oscar': 'oscar',
    'Globo de Ouro': 'globo_ouro',
    'IMDB': 'nota'
})

# Exibir o dicionário
import pandas as pd
from sqlalchemy import create_engine

# Configuração de conexão com o banco de dados PostgreSQL
db_host = 'localhost'
db_port = '5432'
db_user = 'dpr_user'
db_password = 'dpr2023'
db_name = 'postgres'

# Criação do DataFrame com os dados

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Inserção dos dados na tabela do PostgreSQL
table_name = 'app_movie'
df.to_sql(table_name, con=engine, if_exists='append', index=False)

