/* créer un utilisateur spécifique pour l export*/
CREATE user dba_export identified by oracle2018;
/* Donner des Privilèges à l'utilisateur*/

GRANT EXP_FULL_DATABASE TO dba_export;

alter user dba_export quota 100M on tbs_export;


/* création du répertoire et privilèges sur le répertoire : */

create directory dir_export as '/home/oracle/dir_export';

grant read,write on directory dir_export to dba_export;

/7.1* Export 100% SCOTT */

$expdp dba_export/oracle2018@orcl DIRECTORY=dir_export SCHEMAS=SCOTT DUMPFILE=export_full.dmp LOGFILE=export_full.log;




/7.2* Export 20% de la table emp de Scott*/

expdp dba_export/oracle2018@orcl DIRECTORY=dir_export TABLES=scott.emp SAMPLE=20 DUMPFILE=export20_emp.dmp LOGFILE=export20_emp.log;