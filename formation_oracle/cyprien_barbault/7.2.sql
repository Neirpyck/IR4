CREATE USER dba_exp
IDENTIFIED BY dba_exp;

CREATE DIRECTORY export_full as 'location’;
GREAT READ,WRITE ON DIRECTORY export_full TO dba_exp;

expdp dba_exp/dba_exp DIRECTORY=export_full DUMPFILE=\home_oracle\export\dump\requete LOGFILE=\home_oracle\export\log\requete_ TABLE=adherent QUERY=""WHERE ville = 'ANGERS"'
