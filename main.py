from crypt import methods
import sys
from flask import Flask
from src.resources.company import Company
from src.resources.sprint import Sprint
from src.resources.task import Task
from src.db import DB

app = Flask(__name__)

db = DB()

company = Company(db)
sprint = Sprint(db)
task = Task(db)

app.add_url_rule("/company", "get_company", view_func=company.get, methods=["GET"])
app.add_url_rule("/company", "post_company", view_func=company.post, methods=["POST"])

app.add_url_rule("/sprint", "post_sprint", view_func=sprint.post, methods=["POST"])
app.add_url_rule("/sprint", "get_sprint", view_func=sprint.get, methods=["GET"])
app.add_url_rule(
    "/sprint", "delete_sprint", view_func=sprint.delete, methods=["DELETE"]
)

app.add_url_rule("/task", "post_task", view_func=task.post, methods=["POST"])
app.add_url_rule("/task", "get_task", view_func=task.get, methods=["GET"])
app.add_url_rule("/task", "delete_task", view_func=task.delete, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True, port=4040)
