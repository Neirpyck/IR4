CREATE ROLE rh IDENTIFIED BY rh;
GRANT INSERT, UPDATE ON Adherent TO rh;
GRANT RH TO rh1, rh2;