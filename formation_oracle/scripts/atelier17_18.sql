Select ename from scott.emp where numero=7900;

/*recuperer le SCN*/
Select TO_CHAR(SYSDATE, ‘DD/MM/YYYY HH24:MI:SS’) ‘‘ sysdate ’’, dbms_flashback.get_system_change_number ‘‘ SCN’’ From dual; 

/*Faire un UPDATE*/
Update scott.emp set ename=‘jean’ and empno =7900;
Commit;

/*Vérifier le SCN nouvellement attribué*/
Sql>Select TO_CHAR(SYSDATE, ‘DD/MM/YYYY HH24:MI:SS’) ‘‘ sysdate ’’, dbms_flashback.get_system_change_number ‘‘ SCN’’ From dual; 

Select ename from scott.emp where numero=7900;

alter table scott.emp enable row movement;
flashback table scott.emp to scn 25800093;

Select ename from scott.emp where numero=7900;

/* flasback après une suppression d'une table*/
drop table scott.emp;
flashback table scott.emp to before drop;

