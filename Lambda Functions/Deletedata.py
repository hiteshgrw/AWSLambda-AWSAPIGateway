import pymysql
import sys
def main(event, context):
    conn = pymysql.connect(host='40.122.204.90', database='regdb', user='MySql', password='')
    cr = conn.cursor()
    cr.execute('SELECT * from reg_tbl where rid = ' + str(event['id']))
    rows = cr.fetchall()
    values = "<html><body><center><h3>Data delete is: </h3>"
    for row in rows:
		values = values + '<br> RID - '+ str(row[0]) + '<br> Name - ' + str(row[1]) + '<br> Contact No - ' + str(row[2]) + '<br> Email ID - ' + str(row[3]) + '<br> Address - ' + str(row[4])
    values = values + "</br></br><a href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/items'><h3>&lt;&lt; Go Back</h3></a></center></body></html>"
    cr.execute('delete from reg_tbl where rid = '+ str(event['id']))
    conn.commit()
    return values