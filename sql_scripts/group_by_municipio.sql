select "MUNICIPIO_CANDIDATO", count(*) as candidatos 
	from chamada_regular_2022_1
 where "CODIGO_CURSO" = 95104 group by "MUNICIPIO_CANDIDATO"
order by candidatos desc