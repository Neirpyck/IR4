	Drop user metier1 cascade;

	Drop user metier2 cascade;

	Drop user metier3 cascade;

	Drop user metier4 cascade;

	Drop user metier5 cascade;

	Drop user metier6 cascade;

	Drop role admin_metier;

	Drop role user_metier1;
	
Drop role user_metier2;

revoke all privileges from admin_metier;

revoke all privileges on scott.emp from user_metier1;
/* create profile*/
create profile metier 
limit PASSWORD_REUSE_TIME 60 
PASSWORD_REUSE_MAX 5 
CONNECT_TIME 30 
SESSIONS_PER_USER 20 
PRIVATE_SGA 30;

/* affecter le profile aux utilisateurs*/
ALTER USER metier1 PROFILE metier;
ALTER USER metier2 PROFILE metier;
ALTER USER metier3 PROFILE metier;
ALTER USER metier4 PROFILE metier;
