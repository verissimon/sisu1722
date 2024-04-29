
delete FROM public.lista_espera_2022_2
where "ANO" != 2022 and "EDICAO" != 2

select count(*) from chamada_regular_2022_2
where "ANO" != 2022 and "EDICAO" != 2


select count(*) from lista_espera_2022_1
where "ANO" != 2022 and "EDICAO" != 2
