/* création de l'utilisateur metier */
CREATE USER metier
IDENTIFIED BY psswdmetier
DEFAULT TABLESPACE tbs_users
 QUOTA 10M ON tbs_users
 PASSWORD EXPIRE; 

/*Modification du mot de passe*/
alter user sys identified by oracle2018;

/*Bloquer un compte*/
alter user metier account lock;

/*Débloquer un compte*/
alter user metier account unlock;

/*Appliquer un quota*/
alter user metier
quota 15M on tbs_users;

/*vérifier dans les tables dba_users*/
COL username CLEAR
COL username FOR A20
COL account_status FOR A20
COL default_tablespace FOR A20
COL profile FOR A20
COL create FOR A20
select username, account_status, default_tablespace,profile, created from dba_users;










