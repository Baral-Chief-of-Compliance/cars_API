import sqlite3


#класс подключения к базе данных
class Conn(object):
    conn : sqlite3.Connection

    def __init__(self):
        try:
            self.conn = sqlite3.connect("src/cars.db")
        except:
            print("подключение не вышло")

    #сделать запрос
    def make_query(
            self, 
            query_text: str, 
            values: tuple = (), 
            commitFlag: bool=False, 
            resultFlag=True,
            resultManyFlag=True
        ) -> bool or tuple:

        try:
            cur = self.conn.cursor()
            cur.execute(query_text, values)
        except:
            return False

        if commitFlag:
           self.conn.commit() 


        if resultFlag:
            if resultManyFlag:
                return cur.fetchall()
            else:
                return cur.fetchone()

        return True
    

    def __del__(self):
        self.conn.close()


#создаем базу данных
def create_db() -> None:
    con = Conn()
    con.make_query(query_text='''CREATE TABLE Cars(
                       c_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       c_brand TEXT NOT NULL,
                       c_model TEXT NOT NUll,
                       c_year_release INTEGER NOT NULL,
                       c_fuel_type TEXT NOT NULL,
                       c_transmission TEXT NOT NULL,
                       c_mileage INTEGER,
                       c_price INTEGER
                       )''', commitFlag=True, resultFlag=False)    
    del con


