select "ANO", count(*) as inscritos 
	from (
		select distinct on 
			("INSCRITO", "INSCRICAO_ENEM", "DATA_NASCIMENTO") "ANO"
		from chamada_regular_2022_2)
	group by "ANO"