import pymysql
import sys
def main(event, context):
    ce = pymysql.connect(host='40.122.204.90', database='regdb', user='MySql', password='')
    query = "INSERT into reg_tbl(name,contact_no,email_id,address) values('%s','%s','%s','%s')" % (event['name'], event['cno'], event['em'], event['add'])
    cr = ce.cursor()
    cr.execute(query)
    ce.commit()
    cr.close()
    ce.close()
    values = "<html><body><center>"
    values = values + '<h3>Data inserted successfully as follows - </h3><br>Name - ' + event['name'] + '<br> Contact No - ' + event['cno'] + '<br> Email ID - ' + event['em'] + '<br> Address  - ' + event['add']
    values = values + "</br></br><a href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/items'><h3>&lt;&lt; Go Back</h3></a></center></body></html>"
    return values