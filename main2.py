#-*- coding:utf-8 -*-
import web
import psycopg2
urls = ('/', 'Index','/project','Project','/invoices','Invoices','/addinvoices','AddInvoices',
'/addproject','AddProject','/addprojectpage','AddProjectPage')
render=web.template.render('templates')
name = "postgres"
password = "123456"
port = "5432"
host="127.0.0.1"
class Index:
    def GET(self):
        conn = psycopg2.connect(database="postgres", user=name, password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute("SELECT project_name,id FROM project;")
        rows = cur.fetchall()
        s=''
        for row in rows:
            s+='<a href=\"#\" class=\"list-group-item\" onclick=\"parent.location=\'project?project='+row[0]+'&id='+str(row[1])+'\'\">'+row[0]+'</a>'
        conn.commit()
        cur.close()
        conn.close()
        return render.index(s)
class Project:
    def GET(self):
        i=web.input(data=[])
        conn = psycopg2.connect(database="postgres", user=name, password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute("SELECT * FROM invoices WHERE project_id="+str(i.id)+";")
        rows = cur.fetchall()
        s=''
        acc=0
        fy=[0.0]*22
        for row in rows:
            s+='<tr><th>'+str(row[8])+'</th><th>'+row[2]+'</th><th>'+row[6]+'</th><th>'+str(row[5])+'</th><th>'+row[7]+'</th><th>'+str(row[4])+'</th></tr>'
            acc+=row[5]
            fy[row[3]]+=row[5]
        if s.strip():
           s='<table class=\"table table-bordered table-hover\"><thead><tr><th class=\"col-sm-2\">填表时间</th><th class=\"col-sm-1\">报销类型</th><th class=\"col-sm-1\">报销人</th><th class=\"col-sm-1\">报销金额</th><th class=\"col-sm-6\">报销明细</th><th class=\"col-sm-1\">出差时间</th></tr></thead><tbody>'+s+'</tbody></table>'
        conn.commit()
        cur.execute("SELECT * FROM project WHERE id="+str(i.id)+";")
        rows = cur.fetchall()
        for row in rows:
            s+='<tr><li style="list-style-type:none;">项目预算：'+str(row[3])+'</li><li style="list-style-type:none;">项目花费：'+str(acc)+'</li><li style="list-style-type:none;">项目剩余：'+str(row[3]-acc)+'</li></tr>'
            #s+='<h4><tr><li>项目预算：'+str(row[3])+'</li><li>项目花费：'+str(acc)+'</li><li>项目剩余：'+str(row[3]-acc)+'</li></tr></h4>'
        s+='<table class="table table-bordered table-hover" align="left"><thead><tr><th>费用名称</th><th>费用预算</th><th>支出（花费）</th><th>剩余</th></tr></thead><tbody>'
        s+='<tr><th>专职研究人员人工费</th><th>'+str(row[8])+'</th><th>'+str(fy[1])+'</th><th>'+str(row[8]-fy[1])+'</th></tr>'
        s+='<tr><th>临时性研究人员人工费</th><th>'+str(row[9])+'</th><th>'+str(fy[2])+'</th><th>'+str(row[9]-fy[2])+'</th></tr>'
        s+='<tr><th>仪器、设备购置费</th><th>'+str(row[10])+'</th><th>'+str(fy[3])+'</th><th>'+str(row[10]-fy[3])+'</th></tr>'
        s+='<tr><th>仪器、设备试制费</th><th>'+str(row[11])+'</th><th>'+str(fy[4])+'</th><th>'+str(row[11]-fy[4])+'</th></tr>'
        s+='<tr><th>软件购置费</th><th>'+str(row[12])+'</th><th>'+str(fy[5])+'</th><th>'+str(row[12]-fy[5])+'</th></tr>'
        s+='<tr><th>现有仪器设备使用费</th><th>'+str(row[13])+'</th><th>'+str(fy[6])+'</th><th>'+str(row[13]-fy[6])+'</th></tr>'
        s+='<tr><th>材料费</th><th>'+str(row[14])+'</th><th>'+str(fy[7])+'</th><th>'+str(row[14]-fy[7])+'</th></tr>'
        s+='<tr><th>资料费</th><th>'+str(row[15])+'</th><th>'+str(fy[8])+'</th><th>'+str(row[15]-fy[8])+'</th></tr>'
        s+='<tr><th>印刷出版费</th><th>'+str(row[16])+'</th><th>'+str(fy[9])+'</th><th>'+str(row[16]-fy[9])+'</th></tr>'
        s+='<tr><th>知识产权费</th><th>'+str(row[17])+'</th><th>'+str(fy[10])+'</th><th>'+str(row[17]-fy[10])+'</th></tr>'
        s+='<tr><th>会议费</th><th>'+str(row[18])+'</th><th>'+str(fy[11])+'</th><th>'+str(row[18]-fy[11])+'</th></tr>'
        s+='<tr><th>差旅费</th><th>'+str(row[19])+'</th><th>'+str(fy[12])+'</th><th>'+str(row[19]-fy[12])+'</th></tr>'
        s+='<tr><th>培训费</th><th>'+str(row[20])+'</th><th>'+str(fy[13])+'</th><th>'+str(row[20]-fy[13])+'</th></tr>'
        s+='<tr><th>场地物业费</th><th>'+str(row[21])+'</th><th>'+str(fy[14])+'</th><th>'+str(row[21]-fy[14])+'</th></tr>'
        s+='<tr><th>场地租金</th><th>'+str(row[22])+'</th><th>'+str(fy[15])+'</th><th>'+str(row[22]-fy[15])+'</th></tr>'
        s+='<tr><th>专家咨询费</th><th>'+str(row[23])+'</th><th>'+str(fy[16])+'</th><th>'+str(row[24]-fy[16])+'</th></tr>'
        s+='<tr><th>间接费</th><th>'+str(row[24])+'</th><th>'+str(fy[17])+'</th><th>'+str(row[24]-fy[17])+'</th></tr>'
        s+='<tr><th>外委研究支出费</th><th>'+str(row[25])+'</th><th>'+str(fy[18])+'</th><th>'+str(row[25]-fy[18])+'</th></tr>'
        s+='<tr><th>仪器设备租赁费</th><th>'+str(row[26])+'</th><th>'+str(fy[19])+'</th><th>'+str(row[26]-fy[19])+'</th></tr>'
        s+='<tr><th>外协测试试验与加工费</th><th>'+str(row[27])+'</th><th>'+str(fy[20])+'</th><th>'+str(row[27]-fy[20])+'</th></tr>'
        s+='<tr><th>税金</th><th>'+str(row[28])+'</th><th>'+str(fy[21])+'</th><th>'+str(row[28]-fy[21])+'</th></tr>'
        s+='</tbody></table>'
        conn.commit()
        cur.close()
        conn.close()
        return  render.project(s)
class Invoices:
    def GET(self):
        i=web.input(data=[])
        return  render.invoices('a')
class AddProjectPage:
    def GET(self):
        return  render.addproject()
class AddProject:
    def POST(self):
        i=web.input(data=[])
        conn = psycopg2.connect(database="postgres", user=name, password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute("INSERT INTO project(project_name,financial_id,budget,begin_date,end_date,project_org,remarks,rgf1,rgf2,sbf1,sbf2,sbf3,sbf4,ywf1,ywf2,ywf3,ywf4,ywf5,ywf6,ywf7,cdf1,cdf2,zjf,jjf,wwzcf1,wwzcf2,wwzcf3,sj)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (i.data[0],i.data[1],i.data[2],i.data[3],i.data[4],i.data[5],i.data[6],i.data[7],i.data[8],i.data[9],i.data[10],i.data[11],i.data[12],i.data[13],i.data[14],i.data[15],i.data[16],i.data[17],i.data[18],i.data[19],i.data[20],i.data[21],i.data[22],i.data[23],i.data[24],i.data[25],i.data[26],i.data[27]))
        conn.commit()
        cur.close()
        conn.close()
        return  render.correction('a')
class AddInvoices:
     def POST(self):
        i=web.input(data=[])
        conn = psycopg2.connect(database="postgres", user=name, password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute("INSERT INTO invoices(project_id,type,type_id,time,account,name,remarks,submittime)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(i.data[0],i.data[1],i.data[2],i.data[3],i.data[4],i.data[5],i.data[6],i.data[7]))
        conn.commit()
        cur.close()
        conn.close()
        return  render.correction('a')
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()