import json
from psycopg2.extras import RealDictCursor


def get_sprint_from_id(self, company_id, sprint_id):
    query = "select * from sprint where company_id = %s and id = %s"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        query,
        (
            company_id,
            sprint_id,
        ),
    )
    data = cur.fetchone()
    cur.close()
    self.conn.commit()
    return json.dumps(data, default=str)


def delete_sprint_from_id(self, company_id, sprint_id):
    query = "delete from sprint where company_id = %s and id = %s"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        query,
        (
            company_id,
            sprint_id,
        ),
    )
    cur.close()
    self.conn.commit()
    return "successfully deleted sprint"


def create_sprint(self, company_id, sprint_name):
    query = "insert into sprint (name, company_id) values (%s, %s) returning *"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, (sprint_name, company_id))
    data = cur.fetchone()
    cur.close()
    self.conn.commit()
    return json.dumps(data, default=str)
