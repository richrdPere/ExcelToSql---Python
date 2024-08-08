import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="energias_egemsa",
    port=3306
)

cursor = database.cursor(buffered=True)


class Modelo_Energias:
    def __init__(self, local_time, timestam, KWh_del, KWh_rec, KVARh_Q1, KVARh_Q2, KVARh_Q3, KVARh_Q4, VII_prom):
        self.local_time = local_time
        self.timestam = timestam
        self.KWh_del = KWh_del
        self.KWh_rec = KWh_rec
        self.KVARh_Q1 = KVARh_Q1
        self.KVARh_Q2 = KVARh_Q2
        self.KVARh_Q3 = KVARh_Q3
        self.KVARh_Q4 = KVARh_Q4
        self.VII_prom = VII_prom
        
    def registrar(self):
       fecha = datetime.datetime.now()

       sql = "INSERT INTO energias VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
       energias = (self.local_time,self.timestam,self.KWh_del,self.KWh_rec,self.KVARh_Q1,self.KVARh_Q2,self.KVARh_Q3,self.KVARh_Q4,self.VII_prom)

       try:
            cursor.execute(sql, energias)
            database.commit()
            result = [cursor.rowcount, self]
       except:
            result = [0, self]
            
       return result

    def identificar(self):
        return self.local_time
