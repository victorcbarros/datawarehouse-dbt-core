
SELECT 
	tipo,
	EXTRACT(MONTH FROM data_hora) as mes,
	AVG(fator_capacidade) as media_fator_capacidade
FROM 
	{{ref ('stg_geracao') }}
GROUP BY 
	tipo,
	EXTRACT(MONTH FROM data_hora)
ORDER BY
	tipo,
	mes