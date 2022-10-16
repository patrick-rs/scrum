from crypt import methods
import sys
from flask import Flask
from src.resources.company import Company
from src.resources.sprint import Sprint
from src.db.db import DB
import os

app = Flask(__name__)

db = DB()

company = Company(db)
sprint = Sprint(db)

app.add_url_rule("/company", "get_company", view_func=company.get, methods=["GET"])
app.add_url_rule("/company", "post_company", view_func=company.post, methods=["POST"])
app.add_url_rule("/sprint", "sprint", view_func=sprint.get)

if __name__ == "__main__":
    app.run(debug=True, port=4040)
