import psycopg2

class DB:
    def __init__(self):
        conn = psycopg2.connect( host="localhost", database="pat", user="read_only", password="password")

        self.conn = conn

    def echo(self):
        cur = self.conn.cursor()
        cur.execute("select 1 = 1")
        res = cur.fetchall()
        return res
        cur.close()

