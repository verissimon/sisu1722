SELECT "NOME_CURSO", "ANO", sum("INSCRICOES") FROM public.inscricoes_por_curso
	where "NOME_CURSO" = 'ABI - CIÊNCIA DA COMPUTAÇÃO'
group by "NOME_CURSO", "ANO"
order by "NOME_CURSO", "ANO"