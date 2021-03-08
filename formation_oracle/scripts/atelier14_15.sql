/*sauvegarde incremental à froid base fermée*/
/*Lancer l'outil RMAN*/
RMAN target/
/*stopper la base*/
Rman> shutdown immediate

/*passer la base en mode mount*/
RMAN >startup mount;

/*Dimanche : sauvegarde incrémentale niveau 0 */

RMAN> Backup INCREMENTAL LEVEL 0 DATABASE;


/*Dimanche : sauvegarde incrémentale niveau 0 */

RMAN> Backup INCREMENTAL LEVEL 0 DATABASE;

/*Lundi au samedi : sauvegarde incrémentale niveau 1 */

RMAN> Backup INCREMENTAL LEVEL 1 DATABASE;

RMAN>LIST BACKUP OF DATABASE;
RMAN>LIST BACKUPSET 8;



