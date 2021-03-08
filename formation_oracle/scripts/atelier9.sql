exec dbms_stats.gather_table_stats ('SCOTT', 'EMP')
desc dba_tables;
select blocks,num_rows, LAST_ANALYZED,AVG_ROW_LEN,SAMPLE_SIZE  FROM DBA_TABLES where table_name ='EMP' 
and owner='SCOTT';