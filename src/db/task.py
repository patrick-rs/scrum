import json
from psycopg2.extras import RealDictCursor


def get_task_from_id(self, company_id, task_id):
    query = "select * from task where company_id = %s and id = %s"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        query,
        (
            company_id,
            task_id,
        ),
    )
    data = cur.fetchone()
    cur.close()
    self.conn.commit()
    return json.dumps(data, default=str)


def delete_task_from_id(self, company_id, task_id):
    query = "delete from task where company_id = %s and id = %s"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        query,
        (
            company_id,
            task_id,
        ),
    )
    cur.close()
    self.conn.commit()
    return "successfully deleted task"


def create_task(self, company_id, task_name, sprint_id, description, story_points):
    query = "insert into task (company_id, name, sprint_id, description, story_points) values (%s, %s, %s, %s, %s) returning *"

    cur = self.conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, (company_id, task_name, sprint_id, description, story_points))
    data = cur.fetchone()
    cur.close()
    self.conn.commit()
    return json.dumps(data, default=str)
