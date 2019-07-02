--
-- PostgreSQL database dump
--

-- Dumped from database version 11.4 (Debian 11.4-1.pgdg90+1)
-- Dumped by pg_dump version 11.3

-- Started on 2019-07-02 00:55:02 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- DROP DATABASE "dev_db";
-- --
-- -- TOC entry 2950 (class 1262 OID 16385)
-- -- Name: dev_db; Type: DATABASE; Schema: -; Owner: dev
-- --
--
-- CREATE DATABASE "dev_db" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';


ALTER DATABASE "dev_db" OWNER TO "dev";

\connect "dev_db"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 7 (class 2615 OID 16386)
-- Name: sockem_boppem; Type: SCHEMA; Schema: -; Owner: dev
--

CREATE SCHEMA "sockem_boppem";


ALTER SCHEMA "sockem_boppem" OWNER TO "dev";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 210 (class 1259 OID 16500)
-- Name: game; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."game" (
    "game_id" integer NOT NULL,
    "match_id" integer NOT NULL,
    "winner_id" integer NOT NULL,
    "start_time" timestamp with time zone,
    "end_time" timestamp with time zone
);


ALTER TABLE "sockem_boppem"."game" OWNER TO "dev";

--
-- TOC entry 209 (class 1259 OID 16498)
-- Name: game_game_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."game_game_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."game_game_id_seq" OWNER TO "dev";

--
-- TOC entry 2951 (class 0 OID 0)
-- Dependencies: 209
-- Name: game_game_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."game_game_id_seq" OWNED BY "sockem_boppem"."game"."game_id";


--
-- TOC entry 206 (class 1259 OID 16464)
-- Name: match; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."match" (
    "match_id" integer NOT NULL,
    "tournament_id" integer NOT NULL,
    "judge_id" integer NOT NULL,
    "round" smallint NOT NULL,
    "num_games" smallint NOT NULL
);


ALTER TABLE "sockem_boppem"."match" OWNER TO "dev";

--
-- TOC entry 205 (class 1259 OID 16462)
-- Name: match_match_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."match_match_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."match_match_id_seq" OWNER TO "dev";

--
-- TOC entry 2952 (class 0 OID 0)
-- Dependencies: 205
-- Name: match_match_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."match_match_id_seq" OWNED BY "sockem_boppem"."match"."match_id";


--
-- TOC entry 208 (class 1259 OID 16482)
-- Name: match_user; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."match_user" (
    "match_user_id" integer NOT NULL,
    "user_id" integer NOT NULL,
    "match_id" integer NOT NULL
);


ALTER TABLE "sockem_boppem"."match_user" OWNER TO "dev";

--
-- TOC entry 207 (class 1259 OID 16480)
-- Name: match_user_match_user_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."match_user_match_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."match_user_match_user_id_seq" OWNER TO "dev";

--
-- TOC entry 2953 (class 0 OID 0)
-- Dependencies: 207
-- Name: match_user_match_user_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."match_user_match_user_id_seq" OWNED BY "sockem_boppem"."match_user"."match_user_id";


--
-- TOC entry 200 (class 1259 OID 16400)
-- Name: tournament; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."tournament" (
    "tournament_id" integer NOT NULL,
    "name" character varying(16),
    "start_date" timestamp with time zone NOT NULL,
    "creator_id" integer NOT NULL
);


ALTER TABLE "sockem_boppem"."tournament" OWNER TO "dev";

--
-- TOC entry 202 (class 1259 OID 16428)
-- Name: tournament_judge; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."tournament_judge" (
    "tournament_judge_id" integer NOT NULL,
    "user_id" integer NOT NULL,
    "tournament_id" integer NOT NULL
);


ALTER TABLE "sockem_boppem"."tournament_judge" OWNER TO "dev";

--
-- TOC entry 201 (class 1259 OID 16426)
-- Name: tournament_judge_tournament_judge_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."tournament_judge_tournament_judge_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."tournament_judge_tournament_judge_id_seq" OWNER TO "dev";

--
-- TOC entry 2954 (class 0 OID 0)
-- Dependencies: 201
-- Name: tournament_judge_tournament_judge_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."tournament_judge_tournament_judge_id_seq" OWNED BY "sockem_boppem"."tournament_judge"."tournament_judge_id";


--
-- TOC entry 199 (class 1259 OID 16398)
-- Name: tournament_tournament_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."tournament_tournament_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."tournament_tournament_id_seq" OWNER TO "dev";

--
-- TOC entry 2955 (class 0 OID 0)
-- Dependencies: 199
-- Name: tournament_tournament_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."tournament_tournament_id_seq" OWNED BY "sockem_boppem"."tournament"."tournament_id";


--
-- TOC entry 204 (class 1259 OID 16446)
-- Name: tournament_user; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."tournament_user" (
    "tournament_user_id" integer NOT NULL,
    "user_id" integer NOT NULL,
    "tournament_id" integer NOT NULL
);


ALTER TABLE "sockem_boppem"."tournament_user" OWNER TO "dev";

--
-- TOC entry 203 (class 1259 OID 16444)
-- Name: tournament_user_tournament_user_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."tournament_user_tournament_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."tournament_user_tournament_user_id_seq" OWNER TO "dev";

--
-- TOC entry 2956 (class 0 OID 0)
-- Dependencies: 203
-- Name: tournament_user_tournament_user_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."tournament_user_tournament_user_id_seq" OWNED BY "sockem_boppem"."tournament_user"."tournament_user_id";


--
-- TOC entry 198 (class 1259 OID 16389)
-- Name: user; Type: TABLE; Schema: sockem_boppem; Owner: dev
--

CREATE TABLE "sockem_boppem"."user" (
    "user_id" integer NOT NULL,
    "email" character varying NOT NULL,
    "username" character varying(16) NOT NULL,
    "password" character(16) NOT NULL,
    "avatar" character varying
);


ALTER TABLE "sockem_boppem"."user" OWNER TO "dev";

--
-- TOC entry 197 (class 1259 OID 16387)
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: sockem_boppem; Owner: dev
--

CREATE SEQUENCE "sockem_boppem"."user_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sockem_boppem"."user_user_id_seq" OWNER TO "dev";

--
-- TOC entry 2957 (class 0 OID 0)
-- Dependencies: 197
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: sockem_boppem; Owner: dev
--

ALTER SEQUENCE "sockem_boppem"."user_user_id_seq" OWNED BY "sockem_boppem"."user"."user_id";


--
-- TOC entry 2784 (class 2604 OID 16503)
-- Name: game game_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."game" ALTER COLUMN "game_id" SET DEFAULT "nextval"('"sockem_boppem"."game_game_id_seq"'::"regclass");


--
-- TOC entry 2782 (class 2604 OID 16467)
-- Name: match match_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match" ALTER COLUMN "match_id" SET DEFAULT "nextval"('"sockem_boppem"."match_match_id_seq"'::"regclass");


--
-- TOC entry 2783 (class 2604 OID 16485)
-- Name: match_user match_user_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match_user" ALTER COLUMN "match_user_id" SET DEFAULT "nextval"('"sockem_boppem"."match_user_match_user_id_seq"'::"regclass");


--
-- TOC entry 2779 (class 2604 OID 16403)
-- Name: tournament tournament_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament" ALTER COLUMN "tournament_id" SET DEFAULT "nextval"('"sockem_boppem"."tournament_tournament_id_seq"'::"regclass");


--
-- TOC entry 2780 (class 2604 OID 16431)
-- Name: tournament_judge tournament_judge_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_judge" ALTER COLUMN "tournament_judge_id" SET DEFAULT "nextval"('"sockem_boppem"."tournament_judge_tournament_judge_id_seq"'::"regclass");


--
-- TOC entry 2781 (class 2604 OID 16449)
-- Name: tournament_user tournament_user_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_user" ALTER COLUMN "tournament_user_id" SET DEFAULT "nextval"('"sockem_boppem"."tournament_user_tournament_user_id_seq"'::"regclass");


--
-- TOC entry 2778 (class 2604 OID 16392)
-- Name: user user_id; Type: DEFAULT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."user" ALTER COLUMN "user_id" SET DEFAULT "nextval"('"sockem_boppem"."user_user_id_seq"'::"regclass");


--
-- TOC entry 2944 (class 0 OID 16500)
-- Dependencies: 210
-- Data for Name: game; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2940 (class 0 OID 16464)
-- Dependencies: 206
-- Data for Name: match; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2942 (class 0 OID 16482)
-- Dependencies: 208
-- Data for Name: match_user; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2934 (class 0 OID 16400)
-- Dependencies: 200
-- Data for Name: tournament; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2936 (class 0 OID 16428)
-- Dependencies: 202
-- Data for Name: tournament_judge; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2938 (class 0 OID 16446)
-- Dependencies: 204
-- Data for Name: tournament_user; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2932 (class 0 OID 16389)
-- Dependencies: 198
-- Data for Name: user; Type: TABLE DATA; Schema: sockem_boppem; Owner: dev
--



--
-- TOC entry 2958 (class 0 OID 0)
-- Dependencies: 209
-- Name: game_game_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."game_game_id_seq"', 1, false);


--
-- TOC entry 2959 (class 0 OID 0)
-- Dependencies: 205
-- Name: match_match_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."match_match_id_seq"', 1, false);


--
-- TOC entry 2960 (class 0 OID 0)
-- Dependencies: 207
-- Name: match_user_match_user_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."match_user_match_user_id_seq"', 1, false);


--
-- TOC entry 2961 (class 0 OID 0)
-- Dependencies: 201
-- Name: tournament_judge_tournament_judge_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."tournament_judge_tournament_judge_id_seq"', 1, false);


--
-- TOC entry 2962 (class 0 OID 0)
-- Dependencies: 199
-- Name: tournament_tournament_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."tournament_tournament_id_seq"', 1, false);


--
-- TOC entry 2963 (class 0 OID 0)
-- Dependencies: 203
-- Name: tournament_user_tournament_user_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."tournament_user_tournament_user_id_seq"', 1, false);


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 197
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: sockem_boppem; Owner: dev
--

SELECT pg_catalog.setval('"sockem_boppem"."user_user_id_seq"', 1, false);


--
-- TOC entry 2798 (class 2606 OID 16505)
-- Name: game game_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."game"
    ADD CONSTRAINT "game_pkey" PRIMARY KEY ("game_id");


--
-- TOC entry 2794 (class 2606 OID 16469)
-- Name: match match_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match"
    ADD CONSTRAINT "match_pkey" PRIMARY KEY ("match_id");


--
-- TOC entry 2796 (class 2606 OID 16487)
-- Name: match_user match_user_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match_user"
    ADD CONSTRAINT "match_user_pkey" PRIMARY KEY ("match_user_id");


--
-- TOC entry 2790 (class 2606 OID 16433)
-- Name: tournament_judge tournament_judge_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_judge"
    ADD CONSTRAINT "tournament_judge_pkey" PRIMARY KEY ("tournament_judge_id");


--
-- TOC entry 2788 (class 2606 OID 16405)
-- Name: tournament tournament_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament"
    ADD CONSTRAINT "tournament_pkey" PRIMARY KEY ("tournament_id");


--
-- TOC entry 2792 (class 2606 OID 16451)
-- Name: tournament_user tournament_user_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_user"
    ADD CONSTRAINT "tournament_user_pkey" PRIMARY KEY ("tournament_user_id");


--
-- TOC entry 2786 (class 2606 OID 16397)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."user"
    ADD CONSTRAINT "user_pkey" PRIMARY KEY ("user_id");


--
-- TOC entry 2808 (class 2606 OID 16506)
-- Name: game game_match_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."game"
    ADD CONSTRAINT "game_match_id_fkey" FOREIGN KEY ("match_id") REFERENCES "sockem_boppem"."match"("match_id");


--
-- TOC entry 2809 (class 2606 OID 16511)
-- Name: game game_winner_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."game"
    ADD CONSTRAINT "game_winner_id_fkey" FOREIGN KEY ("winner_id") REFERENCES "sockem_boppem"."user"("user_id");


--
-- TOC entry 2805 (class 2606 OID 16475)
-- Name: match match_judge_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match"
    ADD CONSTRAINT "match_judge_id_fkey" FOREIGN KEY ("judge_id") REFERENCES "sockem_boppem"."user"("user_id");


--
-- TOC entry 2804 (class 2606 OID 16470)
-- Name: match match_tournament_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match"
    ADD CONSTRAINT "match_tournament_id_fkey" FOREIGN KEY ("tournament_id") REFERENCES "sockem_boppem"."tournament"("tournament_id");


--
-- TOC entry 2807 (class 2606 OID 16493)
-- Name: match_user match_user_match_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match_user"
    ADD CONSTRAINT "match_user_match_id_fkey" FOREIGN KEY ("match_id") REFERENCES "sockem_boppem"."match"("match_id");


--
-- TOC entry 2806 (class 2606 OID 16488)
-- Name: match_user match_user_user_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."match_user"
    ADD CONSTRAINT "match_user_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "sockem_boppem"."user"("user_id");


--
-- TOC entry 2799 (class 2606 OID 16406)
-- Name: tournament tournament_creator_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament"
    ADD CONSTRAINT "tournament_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "sockem_boppem"."user"("user_id");


--
-- TOC entry 2801 (class 2606 OID 16439)
-- Name: tournament_judge tournament_judge_tournament_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_judge"
    ADD CONSTRAINT "tournament_judge_tournament_id_fkey" FOREIGN KEY ("tournament_id") REFERENCES "sockem_boppem"."tournament"("tournament_id");


--
-- TOC entry 2800 (class 2606 OID 16434)
-- Name: tournament_judge tournament_judge_user_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_judge"
    ADD CONSTRAINT "tournament_judge_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "sockem_boppem"."user"("user_id");


--
-- TOC entry 2803 (class 2606 OID 16457)
-- Name: tournament_user tournament_user_tournament_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_user"
    ADD CONSTRAINT "tournament_user_tournament_id_fkey" FOREIGN KEY ("tournament_id") REFERENCES "sockem_boppem"."tournament"("tournament_id");


--
-- TOC entry 2802 (class 2606 OID 16452)
-- Name: tournament_user tournament_user_user_id_fkey; Type: FK CONSTRAINT; Schema: sockem_boppem; Owner: dev
--

ALTER TABLE ONLY "sockem_boppem"."tournament_user"
    ADD CONSTRAINT "tournament_user_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "sockem_boppem"."user"("user_id");


-- Completed on 2019-07-02 00:55:02 UTC

--
-- PostgreSQL database dump complete
--

