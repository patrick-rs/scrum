import psycopg2
import json
import psycopg2.extras


class DB:
    def __init__(self):
        conn = psycopg2.connect(
            host="localhost", database="scrum", user="scrum_admin", password="password"
        )

        self.conn = conn

    def get_sprints_for_company(self, company_id):
        query = "select * from sprint where company_id = %s"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query, (company_id,))
        data = cur.fetchall()
        cur.close()
        return json.dumps(data, default=str)

    def create_company(self, company_name):
        query = "insert into company (name) values (%s) returning *"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query, (company_name,))
        data = cur.fetchone()
        cur.close()
        return json.dumps(data, default=str)
