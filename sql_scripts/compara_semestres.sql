SELECT * FROM public.chamada_regular_2021_1
LIMIT 100

select count(*) from(
 
)	
	
SELECT t1."CPF", t2."CPF",
	t1."ETAPA", t1."EDICAO",
	t1."OPCAO", t1."APROVADO",
	t2."ETAPA", t2."EDICAO",
	t2."OPCAO", t2."APROVADO" 
FROM chamada_regular_2021_1 t1
INNER JOIN chamada_regular_2021_2 t2
ON t1."INSCRITO" = t2."INSCRITO"
	AND t1."INSCRICAO_ENEM" = t2."INSCRICAO_ENEM"
	AND t1."DATA_NASCIMENTO" = t2."DATA_NASCIMENTO"
	and t1."APROVADO" = 'S'

	
select count(*) from chamada_regular_2021_1


SELECT t1."CPF", t2."CPF"
FROM chamada_regular_2022_1 t1
INNER JOIN chamada_regular_2022_2 t2
ON t1."INSCRITO" = t2."INSCRITO"
	AND t1."INSCRICAO_ENEM" = t2."INSCRICAO_ENEM"
	AND t1."DATA_NASCIMENTO" = t2."DATA_NASCIMENTO"
	and t1."APROVADO" = 'S'
