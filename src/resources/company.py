from ast import And
from flask import request, make_response
from schema import Schema, Or, And, SchemaError


class Company:
    def __init__(self, db):
        self.db = db

    def get(self):
        schema = Schema(
            {
                "action": Or("GetCompanyFromId"),
                "parameters": {"companyId": int},
            }
        )
        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "GetCompanyFromId":
                res = self.db.get_company_from_id(company_id)
                # if res is none then no rows have that company id, so return 404
                if res is None:
                    return make_response("Company not found", 404)
                return res

    def post(self):
        schema = Schema(
            {
                "action": Or("CreateCompany"),
                "parameters": {"companyName": And(str, len)},
            }
        )
        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        company_name = req_body["parameters"]["companyName"]

        match req_body["action"]:
            case "CreateCompany":
                return self.db.create_company(company_name)
