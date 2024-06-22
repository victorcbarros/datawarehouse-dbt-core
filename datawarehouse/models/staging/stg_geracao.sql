-- import 


with source as (
    select 
        "id_subsistema",
        "nom_subsistema",
        "id_estado",
        "nom_estado",
        "nom_pontoconexao",
        "nom_localizacao",
        "val_latitudesecoletora",
        "val_longitudesecoletora",
        "val_latitudepontoconexao",
        "val_longitudepontoconexao",
        "nom_modalidadeoperacao",
        "nom_tipousina",
        "nom_usina_conjunto",
        "din_instante",
        "id_ons",
        "ceg",
        "val_geracaoprogramada",
        "val_geracaoverificada",
        "val_capacidadeinstalada",
        "val_fatorcapacidade"
    from 
        {{ source ('geracaobahia','geracao') }}
),

renamed as (

    select 
        cast("din_instante" as date) as data,
        "nom_subsistema" as regiao,
        "nom_estado" as estado,
        "nom_pontoconexao" as conexao,
        "nom_localizacao" as localizacao,
        "nom_tipousina" as tipo,
        "nom_usina_conjunto" as conjunto,
        "id_ons" as codigo_conjunto,
        "val_geracaoprogramada" as geracao_programada,
        "val_geracaoverificada" as geracao_verificada,
        "val_capacidadeinstalada" as capacidade_instalada,
        "val_fatorcapacidade" as fator_capacidade

    from 
        source
            )

select * from renamed

