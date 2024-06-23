#imports
import pandas as pd
from sqlalchemy import create_engine 
from dotenv import load_dotenv
import os

load_dotenv()

# Obter as variáveis do arquivo .env
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

# função que faz a leitura e e salva os dados em dataframes mensais
def ler_e_salvar_dataframes(urls):
    dataframes = []

    for url in urls:
        try:
            df = pd.read_csv(url,sep=';')
            dataframes.append(df)
        except Exception as e:
            print(f'Erro ao ler a URL {url}: {e}')

    return dataframes

# função que filtra por uma coluna os dados das bases de dados mensais e concatena
def filtrar_nordeste_e_concatena(dataframes,nome_coluna,valor_para_filtrar):
    dataframes_filtrados = []
    for df in dataframes:
        df_filtrado = df[df[nome_coluna] == valor_para_filtrar]
        dataframes_filtrados.append(df_filtrado)
    
    df_final = pd.concat(dataframes_filtrados, ignore_index=True)

    return df_final

#função que salva em postgre a base de dados filtrada e concatenada
def salvar_no_postgres(df,schema='public'):
    df.to_sql('geracao', engine, if_exists ='replace',schema=schema)


if __name__ == "__main__":
    # Lista de URLs 
    urls = ['https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_01.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_02.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_03.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_04.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_05.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_06.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_07.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_08.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_09.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_10.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_11.csv',
            'https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2023_12.csv'
            ]
    #le as urls passadas disponiveis no site da ons
    dataframes = ler_e_salvar_dataframes(urls)
    # pega a coluna que sera filtrada
    nome_coluna = 'id_estado'
    # o valor para ser filtrado
    valor_para_filtrar = 'BA'
    # chama a função que filtra e concatena pelas condições dadas
    base_bahia = filtrar_nordeste_e_concatena(dataframes,nome_coluna,valor_para_filtrar)
    # salva em postgre
    salvar_no_postgres(base_bahia,schema='public')


