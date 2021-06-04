import pymysql
import sys
import json
def main(event, context):
    conn = pymysql.connect(host='40.122.204.90', database='regdb', user='MySql', password='')
    cr = conn.cursor()
    cr.execute('SELECT * from reg_tbl')
    rows = cr.fetchall()
    values = "<html><head><style>table, th, td {border: 1px solid black;padding: 15px;}</style></head><body style='background-color:azure;'><center><h2>Welcome to the User Registration System</h2></br></br><table>"
    values = values + '<tr><th>RID</th><th>NAME</th><th>CONTACT NO</th><th>EMAIL ID</th><th>ADDRESS</th><th></th><th></th></tr>'
    for row in rows:
		values = values + '<tr><td>'+ str(row[0]) + '</td><td>' + str(row[1]) + '</td><td>' + str(row[2]) + '</td><td>' + str(row[3]) + '</td><td>' + str(row[4]) + "</td><td><a href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/delete?id="+str(row[0])+"'>Delete</a></td><td><a href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/update?id="+str(row[0])+"'>Update</a></td></tr>"
    values = values + "</table></br></br><a href='https://dblambdatst.s3.us-east-1.amazonaws.com/index.html'><h3>Insert New Record</h3></a></center></body></html>"
    conn.commit()
    return values