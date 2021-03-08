create user admin_rh
identified by 123
default tablespace tbs_user
quota 10 tbs_user;

create role admin
identified by 123;

grant   create user,
drop user,
lock table,
create table,
create session,
on adherent to admin;

grant admin to adamin_rh;


