
CREATE TABLE IF NOT EXISTS public.chamada_regular_2021_1
(
    "ANO" int,
    "EDICAO" int,
    "ETAPA" int,
    "DS_ETAPA" text COLLATE pg_catalog."default",
    "CODIGO_IES" int,
    "NOME_IES" text COLLATE pg_catalog."default",
    "SIGLA_IES" text COLLATE pg_catalog."default",
    "UF_IES" text COLLATE pg_catalog."default",
    "CODIGO_CAMPUS" int,
    "NOME_CAMPUS" text COLLATE pg_catalog."default",
    "REGIAO_IES" varchar(15) COLLATE pg_catalog."default",
    "UF_CAMPUS" text COLLATE pg_catalog."default",
    "MUNICIPIO_CAMPUS" text COLLATE pg_catalog."default",
    "CODIGO_CURSO" int,
    "NOME_CURSO" text COLLATE pg_catalog."default",
    "GRAU" text COLLATE pg_catalog."default",
    "TURNO" text COLLATE pg_catalog."default",
    "TIPO_MOD_CONCORRENCIA" text COLLATE pg_catalog."default",
    "MOD_CONCORRENCIA" text COLLATE pg_catalog."default",
    -- apenas 2022:
    "QT_VAGAS_CONCORRENCIA" int,
    --
    "PESO_L" double precision,
    "PESO_CH" double precision,
    "PESO_CN" double precision,
    "PESO_M" double precision,
    "PESO_R" double precision,
    "NOTA_MINIMA_L" double precision,
    "NOTA_MINIMA_CH" double precision,
    "NOTA_MINIMA_CN" double precision,
    "NOTA_MINIMA_M" double precision,
    "NOTA_MINIMA_R" double precision,
    "MEDIA_MINIMA" double precision,
    "CPF" text COLLATE pg_catalog."default",
    "INSCRICAO_ENEM" text COLLATE pg_catalog."default",
    "INSCRITO" text COLLATE pg_catalog."default",
    "SEXO" text COLLATE pg_catalog."default",
    "DATA_NASCIMENTO" text COLLATE pg_catalog."default",
    "UF_CANDIDATO" text COLLATE pg_catalog."default",
    "MUNICIPIO_CANDIDATO" text COLLATE pg_catalog."default",
    "OPCAO" int,
    "NOTA_L" double precision,
    "NOTA_CH" double precision,
    "NOTA_CN" double precision,
    "NOTA_M" double precision,
    "NOTA_R" double precision,
    "NOTA_L_COM_PESO" double precision,
    "NOTA_CH_COM_PESO" double precision,
    "NOTA_CN_COM_PESO" double precision,
    "NOTA_M_COM_PESO" double precision,
    "NOTA_R_COM_PESO" double precision,
    "NOTA_CANDIDATO" double precision,
    "NOTA_CORTE" double precision,
    "CLASSIFICACAO" int,
    "APROVADO" text COLLATE pg_catalog."default",
    "MATRICULA" text COLLATE pg_catalog."default"
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.chamada_regular_2021_1
    OWNER to postgres;