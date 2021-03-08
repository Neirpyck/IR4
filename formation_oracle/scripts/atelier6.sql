/* supprimer les utilisateurs */
	Drop user rh1 cascade;

	Drop user rh2 cascade;

	Drop user rh3 cascade;

	Drop user rh4 cascade;

	Drop user rh5 cascade;

	/* supprimer les roles*/
	Drop role admin_rh;

	Drop role role_metier1;
	Drop role role_metier2;
	

/* supprimer les privilèges*/

	revoke all privileges from admin_rh;

	revoke all privileges on scott.emp from role_metier1;

	revoke all privileges  on scott.emp from role_metier2;

/* creation des utilisateurs*/

	create user rh1 identified by metier1;
	create user rh2 identified by metier2;
	create user rh3 identified by metier3;
	create user rh4 identified by metier4;
	create user rh5 identified by metier5;


	create user rh1 identified by metier1;
	create user rh2 identified by metier2;

/* creation des roles pour regrouper les utilisateurs*/

	create role admin_rh not identified;

/* assigner les privilèges syteme aux roles*/
	
	grant create table, create user to admin_rh;

/* creation des roles pour regrouper les utilisateurs*/

	create role role_metier1 not identified;
	create role role_metier2 not identified;

/* assigner les privilèges objets aux roles*/
	GRANT  UPDATE ( JOB, MGR )ON SCOTT.EMP  TO role_metier2 ;

	grant select,insert, update on SCOTT.emp to role_metier2;

/* insérer les utilisateurs dans les roles*/
	grant role_metier1 to rh1;

	grant role_metier1 to rh2;

	grant role_metier2 to rh3;

	grant role_metier2 to rh4;

	grant admin_rh to rh5;

/* vérifier les privileges sur les tables*/
spool /home/oracle/privs_tables

select grantee, table_name, privilege from dba_tab_privs
where GRANTOR ='SCOTT';

spool off

/* vérifier les privileges sur les colonnes*/
spool /home/oracle/privs_cols;
select grantee nom_du_role, table_name nom_de_la_table,column_name from dba_col_privs
where owner ='SCOTT';
spool off;
	
