-- quantidade de inscritos para cada curso
select "NOME_CURSO", count(*) as inscritos 
	from (
		select distinct on 
			("INSCRITO", "INSCRICAO_ENEM", "DATA_NASCIMENTO", "NOME_CURSO", "OPCAO") *
		from regular_2022
		where "OPCAO" = 1
			and "SIGLA_IES" = 'IFPB'
			--and "UF_IES" = 'PB'
	)
	group by "NOME_CURSO"
order by inscritos desc
