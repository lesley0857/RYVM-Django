import mysql.connector as sqlconn
import psycopg2

class sql_query():
    def __init__(self,queryy) -> None:
        self.query = queryy
        

    def makequery(self):
        self.conn = psycopg2.connect(database='railway',user = "postgres",password = "2253cA4ACd1G*cb6D*B25Ade*C46b3e4",host = "monorail.proxy.rlwy.net",port = "13728")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query)#("SELECT datname FROM pg_database")
        print('Connected')
        self.conn.commit()
        result = self.cursor.fetchall()
        self.conn.close()
        self.cursor.close()
        return result
    

# def makequery(query):
#     conn = sqlconn.connect(host='localhost',password='',user='root',database='django')
#     cursor = conn.cursor()
#     if conn.is_connected():
#         print('Connected')
#         cursor.execute(str(query))
#         return cursor.fetchall()
        
    
#     else:
#         print('Diconnected')
    
#     cursor.close()
#     conn.close()
