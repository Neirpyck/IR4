/*Lancer l'outil RMAN*/
RMAN target/
/*Visualisation des paramètres RMAN*/
Rman> Show all;

Modification des paramètres RMAN
RMAN >CONFIGURE …….;

/*Modifier le chemin de la sauvegarde*/

RMAN>CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT   '/home/oracle/sauvegarde/ora_df%t_s%s_s%p';
