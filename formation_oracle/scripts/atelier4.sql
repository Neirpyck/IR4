/* création de la tablespace pour l'objet index */
create tablespace tbs_index 
datafile '/ora01/oracle/app/oracle/oradata/orcl/tbs_index.dbf' size 40M;

/* création de la tablespace pour l'objet utilisateur */
create tablespace tbs_users1 
datafile '/ora01/oracle/app/oracle/oradata/orcl/tbs_user1.dbf' size 30M;

/*Passer le tablespace en OFFLINE*/
alter tablespace tbs_index offline;


/*Modifier le TABLESPACE , le dossier de stockage*/

ALTER TABLESPACE tbs_users1 
  RENAME DATAFILE '/ora01/oracle/app/oracle/oradata/orcl/tbs_users1.dbf'
  TO              '/ora01/oracle/app/oracle/oradata/orcl/tbs_users2.dbf'; 
/*Passer le tablespace en lecture ou lecture/ecriture*/

ALTER TABLESPACE tbs_data READ ONLY;
ALTER TABLESPACE tbs_data READ WRITE;

/*Supprimer les tablespaces créés au dessus*/
drop tablespace tbs_index;
drop tablespace tbs_users1;

/*les tables et vues pour vérifier*/
/*Tablespaces : DBA_TABLESPACES, V$TABLESPACE*/
/*Data files : DBA_DATA_FILES, V$DATAFILE*/

COL tablespace_name CLEAR
COL tablespace_name FOR A20
COL file_name FOR A55
SELECT
  *
FROM 
  (
    SELECT
      tablespace_name,
      file_name,
      status,
      autoextensible,
      blocks,
      user_blocks,
      maxblocks
    FROM
      dba_data_files 
  UNION ALL 
    SELECT
      tablespace_name,
      file_name,
      status,
      autoextensible,
      blocks,
      user_blocks,
      maxblocks
    FROM
      dba_temp_files
  )
/
