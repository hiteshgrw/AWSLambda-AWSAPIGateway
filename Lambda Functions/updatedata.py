import pymysql
import sys
def main(event, context):
    ce = pymysql.connect(host='40.122.204.90', database='regdb', user='MySql', password='')
    query = "update reg_tbl set name = '%s', contact_no = %s, email_id = '%s', address = '%s' where rid = %s" % (event['name'], event['cno'], event['em'], event['add'], event['id'])
    cr = ce.cursor()
    cr.execute(query)
    ce.commit()
    cr.close()
    ce.close()
    values = "<html><body><center>"
    values = values + '<h3>Data updated successfully as follows - </h3><br>Name - ' + event['name'] + '<br> Contact No - ' + event['cno'] + '<br> Email ID - ' + event['em'] + '<br> Address  - ' + event['add']
    values = values + "</br></br><a href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/items'><h3>&lt;&lt; Go Back</h3></a></center></body></html>"
    return values