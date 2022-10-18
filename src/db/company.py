import json
from psycopg2.extras import RealDictCursor


def create_company(self, company_name):
    query = "insert into company (name) values (%s) returning *"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, (company_name,))
    data = cur.fetchone()
    cur.close()
    self.conn.commit()
    return json.dumps(data, default=str)


def get_company_from_id(self, company_id):
    query = "select * from company where id = %s"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, (company_id,))
    data = cur.fetchone()
    cur.close()
    return json.dumps(data, default=str)
