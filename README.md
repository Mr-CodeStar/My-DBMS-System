# My-DBMS-System
AurorexDB a DBMS system create completly on python using sqlite3 module.
Other modules which you need to install are:
Getpass:-  pip install getpass
PrettyTable:-  pip install prettytable
Colorama:-  pip install colorama
you don't have to install Sqlite3, OS module as it's apart of the python standard library which comes when python is installed. 
To use this database you jus need to copy the code and run it in your system...

Commands Syntax use in this system:-

1) To create a database write:
     create database database-name
2) To show all the Databases in the system:
     show databases
3) To use a Perticular Database:
     use database-name
4) To drop a database:
     drop database database-name
#Note please first select a database to work/create a table
5) To create a table:
     create table table-name (field, type)
   #Note you can create as many fields as you want but all will be written in a single line!
6) To insert into a table:
     insert into table-name values (items)
     You can also pass multiple parameters in the insert command by seperating it by ','
7) To show the structure of the table:
     show structure for table-name
8) To print the table values or say using the Select command:
     select * from table-name
     or
     select parameters from table-name where condition
9) To show all tables present inside a database:
      show tables
The rest of the commnads like update,alter,etc are done by using the general syntax of the sqlite only.
10) To exit from the system you can use:
      exit, end, terminate, quit commands.

({[ Please note that two .db files will be created when you will be using the system for the first time which are
no_of_db.db, user_information.db which holds the user credentials and the total number of databases u have created till now. IF those files got removed from the system ny any means you will lost all the database files info from the system. The system will then again will ask for a new pasword and a will create those files again but the previous data records will be lost and will not be accessible from this system. ]})


More Updates will be available soon!!!!!
