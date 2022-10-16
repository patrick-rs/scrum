from flask import Flask
from src.resources.company import Company
from src.db.db import DB

app = Flask(__name__)

def echo():
    return "Echo"

db = DB()
company = Company(db)

app.add_url_rule("/", "company_get", view_func=company.get)

if __name__ == "__main__":
    app.run(debug=True)
