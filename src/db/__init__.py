import os
import psycopg2


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

    from .company import create_company, get_company_from_id
    from .sprint import create_sprint, delete_sprint_from_id, get_sprint_from_id
    from .task import create_task, delete_task_from_id, get_task_from_id
