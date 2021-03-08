/*sauvegarde à froid base fermée*/
/*Lancer l'outil RMAN*/
RMAN target/
/*stopper la base*/
Rman> shutdown immediate

/*passer la base en mode mount*/
RMAN >startup mount;

/*Sauvegarde */

RMAN>backup database

/*sauvegarde à chaud base ouverte*/
/*Lancer l'outil RMAN*/
RMAN target/
/*passage de la base en archivelog*/
RMAN>shutdown immediate;
RMAN>startup mount;
RMAN>ALTER DATABASE ARCHIVELOG;
RMAN>ALTER DATABASE open;
RMAN>backup database;
RMAN>LIST BACKUP OF DATABASE;


