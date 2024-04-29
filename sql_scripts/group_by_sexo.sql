select "SEXO", count(*) as candidatos 
	from chamada_regular_2022_1
 where "CODIGO_CURSO" = 95104 group by "SEXO"
order by candidatos desc