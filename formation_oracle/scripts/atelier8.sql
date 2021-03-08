drop table scott.formation;
CREATE TABLE scott.formation
(ID_ent	NUMBER(6) primary key,
Nom 	VARCHAR2(40),
Prenom VARCHAR2(40),
Demande_form Varchar2(60))
TABLESPACE tbs_data
STORAGE (INITIAL 1M)
PCTFREE 30
PCTUSED 40;
/* visualiser la création de la table*/
desc dba_tables;
select table_name, tablespace_name, pct_free, pct_used, num_rows 
from dba_tables where owner='SCOTT';