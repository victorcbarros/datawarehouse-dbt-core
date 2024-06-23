# Projeto de Datawarehouse com Python, Postgree e Dbt-core

Este projeto é inspirado no workshop aberto do Luciano Galvão (link nas referencias) sobre Datawarehouse onde realiza um processo ELT (Extract,Load, Transform) sequencial utilizando Python, PostgreSQL, dbt core, SQL e Streamlit. O objetivo é ler dados de URLs, filtrar e concatenar esses dados, salvar no PostgreSQL, realizar análises e visualizar os resultados em um dashboard Streamlit.

No caso deste projeto usaremos dados abertos da ONS a respeito do fator de capacidade de Usinas de geração eollica e solar para os meses de 2023(disponivel nas referencias no final). Filtraremos apenas as usinas da Bahia e realizaremos as analises dos dados atraves do SQL.

## Passos do Workflow


![alt text](figures\image.png)


1. **Iniciar**
    - Representa o início do processo.

2. **Ler URLs e Salvar DataFrames**
    - Nesta etapa, as URLs são lidas e os DataFrames são criados a partir dos arquivos CSV.

3. **Filtrar DataFrames para BA**
    - Os DataFrames são filtrados para incluir apenas os dados relacionados ao estado da Bahia (BA).

4. **Concatenar DataFrames**
    - Os DataFrames filtrados são combinados em um único DataFrame.

5. **Salvar no PostgreSQL**
    - O DataFrame final é salvo no PostgreSQL.

6. **Salvar a base no dbt core**
    - A base de dados é salva no dbt core para gerenciamento e versionamento.

7. **Fazer as análises em SQL**
    - As análises em SQL são realizadas utilizando o dbt core.

8. **Importar para visualização no dashboard em Streamlit**
    - Os dados são importados para visualização em um dashboard utilizando Streamlit.


## Referencias

Link do workshop do Luciano: https://github.com/lvgalvao/workshop-aberto-dw-do-zero-aovivo

Link dos dados abertos da ONS utilizados: https://dados.ons.org.br/dataset/fator-capacidade-2


