import os
import psycopg2
import json
import psycopg2.extras


class DB:
    db_env_var_password = "POSTGRES_SCRUM_ADMIN_PASSWORD"
    db_env_var_host = "POSTGRES_SCRUM_HOST"
    db_env_var_port = "POSTGRES_SCRUM_PORT"

    def __init__(self):

        password = "password"
        if self.db_env_var_password in os.environ:
            password = os.getenv(self.db_env_var_password)

        host = "localhost"
        if self.db_env_var_host in os.environ:
            password = os.getenv(self.db_env_var_host)

        port = "5432"
        if self.db_env_var_port in os.environ:
            password = os.getenv(self.db_env_var_port)

        conn = psycopg2.connect(
            host=host,
            port=port,
            database="scrum",
            user="scrum_admin",
            password=password,
        )

        self.conn = conn

    def get_sprint_from_id(self, company_id, sprint_id):
        query = "select * from sprint where company_id = %s and id = %s"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
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

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            query,
            (
                company_id,
                sprint_id,
            ),
        )
        cur.close()
        self.conn.commit()
        return "Successfully deleted sprint"

    def create_sprint(self, company_id, sprint_name):
        query = "insert into sprint (name, company_id) values (%s, %s) returning *"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query, (sprint_name, company_id))
        data = cur.fetchone()
        cur.close()
        self.conn.commit()
        return json.dumps(data, default=str)

    def create_company(self, company_name):
        query = "insert into company (name) values (%s) returning *"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query, (company_name,))
        data = cur.fetchone()
        cur.close()
        self.conn.commit()
        return json.dumps(data, default=str)

    def get_company_from_id(self, company_id):
        query = "select * from company where id = %s"

        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query, (company_id,))
        data = cur.fetchone()
        cur.close()
        return json.dumps(data, default=str)
