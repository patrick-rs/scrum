from flask import request
class Company:
    def __init__(self, db):
        self.db = db

    def get(self):
        print(request.json)
        res = self.db.echo()
        return res
