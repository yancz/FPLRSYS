# coding=utf-8
import psycopg2
#conn = psycopg2.connect(database="postgres", user="postgres", password="23726744", host="127.0.0.1", port="5433")
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="192.168.1.225", port="5432")
cur = conn.cursor()

#file_object = open('xiangmu.csv')
#line = file_object.readline()
#line = file_object.readline()
#while line:
#    print line;
#    s = line.split(',')
#    print s[7]
#    #cur.execute("INSERT INTO project(project_name,financial_id,budget,begin_date,end_date,project_org,remarks,rgf1,rgf2,sbf1,sbf2,sbf3,sbf4,ywf1,ywf2,ywf3,ywf4,ywf5,ywf6,ywf7,cdf1,cdf2,zjf,jjf,wwzcf1,wwzcf2,wwzcf3,sj)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26],s[27]))
#    cur.execute("INSERT INTO project(project_name,financial_id,budget,begin_date,end_date,project_org,remarks,rgf1,rgf2,sbf1,sbf2,sbf3,sbf4,ywf1,ywf2,ywf3,ywf4,ywf5,ywf6,ywf7,cdf1,cdf2,zjf,jjf,wwzcf1,wwzcf2,wwzcf3,sj)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (unicode(s[0],'gbk'),s[1],s[2],s[3],s[4],unicode(s[5],'gbk'),unicode(s[6],'gbk'),s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26],s[27]))
#    line = file_object.readline();
#file_object.close()

file_object = open('fp1.csv')
line = file_object.readline()
while line:
    print line;
    s = line.split(',')
    print s[0]
    print s[1]
    print s[2]
    print s[3]
    print s[4]
    print s[5]
    print s[6]
    print s[7]
    cur.execute("INSERT INTO invoices(project_id,type,type_id,time,account,name,remarks,submittime)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(s[0],unicode(s[1],'gbk'),s[2],s[3],s[4],unicode(s[5],'gbk'),unicode(s[6],'gbk'),s[7]))
    line = file_object.readline();
file_object.close()

#cur.execute("CREATE TABLE invoices(id serial PRIMARY KEY,project_id integer,type varchar,type_id integer,time date,account real,name varchar,remarks varchar,submittime varchar);")
#cur.execute("CREATE TABLE project(id serial PRIMARY KEY,project_name varchar,financial_id varchar,budget real,begin_date date,end_date date,project_org varchar,remarks varchar,rgf1 real,rgf2 real,sbf1 real,sbf2 real,sbf3 real,sbf4 real,ywf1 real,ywf2 real,ywf3 real,ywf4 real,ywf5 real,ywf6 real,ywf7 real,cdf1 real,cdf2 real,zjf real,jjf real,wwzcf1 real,wwzcf2 real,wwzcf3 real,sj real);")
#cur.execute("INSERT INTO project(project_name,financial_id,budget,begin_date,end_date,project_org,remarks,rgf1,rgf2,sbf1,sbf2,sbf3,sbf4,ywf1,ywf2,ywf3,ywf4,ywf5,ywf6,ywf7,cdf1,cdf2,zzf,jjf,wwzcf1,wwzcf2,wwzcf3,sj)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (0,2,20000.123,'2010-01-02','2010-02-03',6,7,1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0,0,0,0,0,0))
conn.commit()
cur.close()
conn.close()