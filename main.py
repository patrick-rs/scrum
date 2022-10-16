from flask import Flask
from src.resources.company import Company
from src.resources.sprint import Sprint
from src.db.db import DB

app = Flask(__name__)

db = DB()

company = Company(db)
sprint = Sprint(db)

app.add_url_rule("/company", "company", view_func=company.get)
app.add_url_rule("/sprint", "sprint", view_func=sprint.get)

if __name__ == "__main__":
    app.run(debug=True, port=4040)
