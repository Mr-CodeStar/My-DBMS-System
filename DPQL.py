#my own database
import sqlite3
import getpass
from prettytable import PrettyTable
import os
from colorama import Fore,Style
###################################################Login Part######################################
if os.path.exists("DQL/DQL_user/user_information_.db"):
    user_login_password=getpass.getpass("enter password: ")
    conn=sqlite3.connect("DQL/DQL_user/user_information_.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM user_information")
    for i in cursor:
        if user_login_password in i:
            conn.close()
            print(Fore.GREEN+Style.BRIGHT+"Welcome\n"+Style.RESET_ALL)
            break
        else:
            print(Fore.RED+Style.BRIGHT+"Wrong Password! UnAuthorised Entry Caught-----> Entry Denied!"+Style.RESET_ALL)
            conn.close()
            exit()
else:
    user_login_password=getpass.getpass("Enter Password To Create An Account: ")
    os.mkdir("DQL")
    os.mkdir("DQL/DQL_user")
    conn=sqlite3.connect("DQL/DQL_user/user_information_.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE user_information(username text,password text)")
    conn.commit()
    query=(user_login_password,user_login_password)
    cursor.execute("""INSERT INTO user_information VALUES(?,?)""",query)
    conn.commit()
    conn.close()
    nodb=sqlite3.connect("DQL/DQL_user/no_of_db.db")
    cursor=nodb.cursor()
    cursor.execute("""create table noofdb(name text)""")
    nodb.commit()
    nodb.close()
    print(Fore.BLUE+Style.BRIGHT+"Account Created!Thanks for choosing DQL\nDQL is Ready to GO!------- ;)\n"+Style.RESET_ALL)
####################################Database Part##################################################
####################################Pretty table display part######################################
def PT(label,lst):
    table=PrettyTable(label)
    for i in lst:
        table.add_row(i)
    print(table)
######################################Function Part################################################
connected_db=""
def Creater_info():
    VERSION="1.0.0.0"
    Creater_name="Dev Barma"
    print("Programe Version={}".format(VERSION))
    print("Hey! i am {}!. Thanks for using DPQL.\nUpdates will be available for new version at:-\nhttps://github.com/Mr-CodeStar\nDo check it out for any updates!".format(Creater_name))
def consdb(db_name):
    conn=sqlite3.connect("DQL/"+db_name+".db")
    print("database created!")
    conn.close()
    nodb=sqlite3.connect("DQL/DQL_user/no_of_db.db")
    cursor=nodb.cursor()
    db_name="\""+db_name+"\""
    cursor.execute("""insert into noofdb values({})""".format(db_name))
    nodb.commit()
    nodb.close()
def usedb(db_name):
    nodb=sqlite3.connect("DQL/DQL_user/no_of_db.db")
    cursor=nodb.cursor()
    cursor.execute("""select * from noofdb""")
    lst=cursor.fetchall()
    for i in lst:
        if db_name in i:
            break
    else:
        print(Fore.RED+Style.BRIGHT+"no such database found------------->Database Not Found Error!"+Style.RESET_ALL)
        return
    nodb.commit()
    nodb.close()
    conn=sqlite3.connect("DQL/"+db_name+".db")
    print(Fore.GREEN+Style.BRIGHT+"database connected"+Style.RESET_ALL)
    conn.close()
    return db_name+".db"
def showdb():
    nodb=sqlite3.connect("DQL/DQL_user/no_of_db.db")
    cursor=nodb.cursor()
    try:
        cursor.execute("""select * from noofdb""")
        lst=cursor.fetchall()
        nodb.close()
        PT(["All_Databases"],lst)
        nodb.close()
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"invalid command--------------------->not valid commmand to show databases"+Style.RESET_ALL)
        nodb.close()
def dropdb(query):
    conn=sqlite3.connect("DQL/DQL_user/no_of_db.db")
    cursor=conn.cursor()
    try:
        lst=query.split()
        os.remove("DQL/{}.db".format(lst[-1]))
        cursor.execute("""delete from noofdb where name='{}'""".format(lst[-1]))
        print(Fore.GREEN+Style.BRIGHT+"database removed!"+Style.RESET_ALL)
        conn.commit()
        conn.close()
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"invalid command-------------------->dabase was deleted from the system\nbut not from the memory of the software\nPlease reinstall the software or the database will be not accessable even after the name is showing!"+Style.RESET_ALL)
        conn.close()
def constb(loc,query):
    conn=sqlite3.connect("DQL/"+loc)
    cursor=conn.cursor()
    try:
        cursor.execute(query)
        print(Fore.GREEN+Style.BRIGHT+"table created"+Style.RESET_ALL)
        conn.commit()
        conn.close()
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"invalid command----------------------->Table not created"+Style.RESET_ALL)
        conn.close()
def inserttb(loc,query):
    conn=sqlite3.connect("DQL/"+loc)
    cursor=conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print(Fore.GREEN+Style.BRIGHT+"value inserted!"+Style.RESET_ALL)
        conn.close()
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"insertion was not done!-------->invalid insertion command"+Style.RESET_ALL)
        conn.close()
def selecttb(loc,query):
    conn=sqlite3.connect("DQL/"+loc)
    cursor=conn.cursor()
    try:
        if query.startswith("select * from"):
            lst=query.split()
            cursor.execute("""pragma table_info({})""".format(lst[3]))
            lst=cursor.fetchall()
            lst1=[]
            for i in range(0,len(lst)):
                k=lst[i]
                lst1.append(k[1])
            cursor.execute(query)
            lst=cursor.fetchall()
            PT(lst1,lst)
        else:
            name=query.split()
            fields=name[1].split(",")
            cursor.execute(query)
            lst=cursor.fetchall()
            PT(fields,lst)
        conn.commit()
        conn.close()
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"invalid command has being given---------->not a valid command"+Style.RESET_ALL)
        conn.close()
def tbstut(loc,query):
    conn=sqlite3.connect("DQL/"+loc)
    cursor=conn.cursor()
    try:
        lst=query.split()
        cursor.execute("""pragma table_info({})""".format(lst[-1]))
        lst=cursor.fetchall()
        feild_name=["cid","name","type","notnull","dflt_value","pk"]
        PT(feild_name,lst)
        conn.commit()
        conn.close()
    except Exception as e:
        conn.close()
        print(Fore.RED+Style.BRIGHT+"invalid syntax to display table structure------------>Structure not showed!"+Style.RESET_ALL)
def generalq(loc,query):
    conn=sqlite3.connect("DQL/"+loc)
    cursor=conn.cursor()
    if query.lower()=="show tables":
        cursor.execute("""select name from sqlite_master where type='table'""")
        lst=cursor.fetchall()
        PT(["Tables"],lst)
    else:
        try:
            cursor.execute(query)
            print(Fore.GREEN+Style.BRIGHT+"command executed"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid command--------------->command not executed!"+Style.RESET_ALL)
    conn.commit()
    conn.close()
################# how to display table structure to user? #####################
while True:
    command=input(Fore.BLUE+"@-> "+Style.RESET_ALL)
    if command.lower().startswith("create database"):
        ls=command.split()
        if len(ls)==3:
            consdb(ls[-1])
        else:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to create a database------------>Database Not Created!"+Style.RESET_ALL)
    elif command.lower()=="show databases":
        showdb()
    elif command.lower().startswith("use "):
        ls=command.split()
        if len(ls)==2:
            connected_db=usedb(ls[-1])
        else:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to use a database------------>Database Not Used!"+Style.RESET_ALL)
    elif command.lower().startswith("create table"):
        if connected_db=="":
            print(Fore.RED+Style.BRIGHT+"No Database Selected----------->Please Select a Database First!"+Style.RESET_ALL)
            continue
        try:
            constb(connected_db,command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to create a table------------>Table Not Created!"+Style.RESET_ALL)
    elif command.lower().startswith("insert into"):
        if connected_db=="":
            print(Fore.RED+Style.BRIGHT+"No Database Selected----------->Please Select a Database First!"+Style.RESET_ALL)
            continue
        try:
            inserttb(connected_db,command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to work on a table------------>Work Not Done!"+Style.RESET_ALL)
    elif command.lower().startswith("select"):
        if connected_db=="":
            print(Fore.RED+Style.BRIGHT+"No Database Selected----------->Please Select a Database First!"+Style.RESET_ALL)
            continue
        try:
            selecttb(connected_db,command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to fetch value from the table------------>value not fetched!"+Style.RESET_ALL)
    elif command.lower().startswith("drop database"):
        try:
            dropdb(command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"An error has occured"+Style.RESET_ALL)
    elif command.lower() in ["quit","exit","end","terminate"]:
        exit()
    elif command == "DPQL_Creater_info":
        Creater_info()
    elif command.lower().startswith("show structure for"):
        if connected_db=="":
            print(Fore.RED+Style.BRIGHT+"No Database Selected----------->Please Select a Database First!"+Style.RESET_ALL)
            continue
        try:
            tbstut(connected_db,command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to display table structure------------>Structure not showed!"+Style.RESET_ALL)
    else:
        if "+" in command or "-" in command or "*" in command or "/" in command or "%" in command:
            try:
                print(Fore.GREEN+str(eval(command))+Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED+Style.BRIGHT+"Wrong expression please correct your expression----------------->Invalid Expression"+Style.RESET_ALL)
            continue
        if connected_db=="":
            print(Fore.RED+Style.BRIGHT+"No Database Selected----------->Please Select a Database First!"+Style.RESET_ALL)
            continue
        try:
            generalq(connected_db,command)
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+"invalid syntax to work on a table------------>Work Not Done!"+Style.RESET_ALL)
