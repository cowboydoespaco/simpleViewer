--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: imagem; Type: TABLE; Schema: public; Owner: userTeste; Tablespace: 
--

CREATE TABLE imagem (
    id integer NOT NULL,
    titulo character varying(50),
    descricao character varying(50),
    "nomeArquivo" character varying(50)
);


ALTER TABLE public.imagem OWNER TO "userTeste";

--
-- Name: imagem_id_seq; Type: SEQUENCE; Schema: public; Owner: userTeste
--

CREATE SEQUENCE imagem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.imagem_id_seq OWNER TO "userTeste";

--
-- Name: imagem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: userTeste
--

ALTER SEQUENCE imagem_id_seq OWNED BY imagem.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: userTeste
--

ALTER TABLE ONLY imagem ALTER COLUMN id SET DEFAULT nextval('imagem_id_seq'::regclass);


--
-- Name: imagem_pkey; Type: CONSTRAINT; Schema: public; Owner: userTeste; Tablespace: 
--

ALTER TABLE ONLY imagem
    ADD CONSTRAINT imagem_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

