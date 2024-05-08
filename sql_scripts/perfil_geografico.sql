-- quantidade de inscritos por UF para determinada uf_campus
select "UF_CANDIDATO", count(*) as inscritos 
	from (
		select distinct on 
			("INSCRITO", "INSCRICAO_ENEM", "DATA_NASCIMENTO") *
		from regular_2022
		where --"OPCAO" = 1 and
			"UF_CAMPUS" = 'PB'
	)
	group by "UF_CANDIDATO"
order by inscritos desc

-- qtd de inscritos de determinado municipio
select "MUNICIPIO_CANDIDATO", count(*) as inscritos 
	from (
		select distinct on 
			("INSCRITO", "INSCRICAO_ENEM", "DATA_NASCIMENTO") *
		from regular_2022
		where "SIGLA_IES" = 'IFPB'
			and "MUNICIPIO_CAMPUS" = 'Cajazeiras'
			and "NOME_CURSO" = 'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS'
	)
	group by "MUNICIPIO_CANDIDATO"
order by inscritos desc