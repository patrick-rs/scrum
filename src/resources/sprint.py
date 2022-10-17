from flask import request
from schema import Schema, Or, And, SchemaError
from flask import make_response


class Sprint:
    def __init__(self, db):
        self.db = db

    def get(self):
        schema = Schema(
            {
                "action": Or("GetSprintFromId"),
                "parameters": {
                    "sprintId": int,
                    "companyId": int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        sprint_id = req_body["parameters"]["sprintId"]
        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "GetSprintFromId":
                return self.db.get_sprint_from_id(company_id, sprint_id)

    def delete(self):
        schema = Schema(
            {
                "action": Or("DeleteSprintFromId"),
                "parameters": {
                    "sprintId": int,
                    "companyId": int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        sprint_id = req_body["parameters"]["sprintId"]
        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "DeleteSprintFromId":
                return self.db.delete_sprint_from_id(company_id, sprint_id)

    def post(self):
        schema = Schema(
            {
                "action": Or("CreateSprint"),
                "parameters": {
                    "sprintName": And(str, len),
                    "companyId": int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        sprint_name = req_body["parameters"]["sprintName"]
        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "CreateSprint":
                return self.db.create_sprint(company_id, sprint_name)
