CREATE TABLE adherent
(
  Code_adherent NUMBER(6)
  Nom     VARCHAR2(40)
  Prenom-1    VARCHAR2(40)
  Prenom-2    VARCHAR2(40)
  Adresse   VARCHAR2(40)
  Code_postal   NUMBER(5)
  Ville     VARCHAR2(40)
  Pays      VARCHAR2(40)
  Date_entree   DATE
  Date_fin    DATE
  PRIMARY KEY (Code_adherent)
)
TABLESPACE adherents
STORAGE (INITIAL 10M)
PCTFREE 30
PCTUSED 70 ;

CREATE INDEX identity ON adherent (Nom, Prenom-1) ;
