import mysql.connector as mc
try:
    dbc=mc.connect(host="localhost",user="root",passwd="hellyeah11",database="project")
    cursor=dbc.cursor()
except Exception as e:
    print(e)
