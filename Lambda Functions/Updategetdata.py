import pymysql
import sys
def main(event, context):
    conn = pymysql.connect(host='40.122.204.90', database='regdb', user='MySql', password='')
    cr = conn.cursor()
    cr.execute('SELECT * from reg_tbl where rid = ' + str(event['id']))
    rows = cr.fetchall()
    values = "<html><head><script>function fn(){var name=document.getElementById('nm').value;var cno=document.getElementById('cno').value;var em=document.getElementById('em').value;var add=document.getElementById('add').value;window.location.href='https://td2mm97dl2.execute-api.us-east-1.amazonaws.com/teststg/dblambda/updateit?id="+ str(event['id']) + "&name='+name+'&cno='+cno+'&em='+em+'&add='+add;}</script></head><body><h3>Update Data: </h3><form>"
    for row in rows:
		values = values + "<br><br> Name - <input type='text' name='nm' value='"+ str(row[1]) + "' id='nm'><br><br> Contact No - <input type='text' name='cno' value='" + str(row[2]) + "' id='cno'><br><br> Email ID - <input type='text' name='em' value='" + str(row[3]) + "' id='em'><br><br> Address - <input type='text' name='add' value='" + str(row[4]) + "' id='add'><br><br><input type='button' value='Update' onclick='fn()'>"
    values = values + "</form></body></html>"
    conn.commit()
    return values