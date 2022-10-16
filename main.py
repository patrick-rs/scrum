from flask import Flask

app = Flask(__name__)


def echo():
    return "Echo"

app.add_url_rule("/", view_func=echo)

if __name__ == "__main__":
    app.run(debug=True)
