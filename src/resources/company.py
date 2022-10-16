from ast import And
from flask import request
from schema import Schema, Or, And
from src.validator import ValidateDictionary


class Company:
    def __init__(self, db):
        self.db = db

    def get(self):
        return "get request"

    def post(self):
        schema = Schema(
            {
                "action": Or("CreateCompany"),
                "parameters": {"companyName": And(str, len)},
            }
        )
        req_body = request.json

        if not ValidateDictionary(schema, req_body):
            return ("Invalid request body", 400)

        company_name = req_body["parameters"]["companyName"]
        match req_body["action"]:
            case "CreateCompany":
                return self.db.create_company(company_name)

        return "post request"
