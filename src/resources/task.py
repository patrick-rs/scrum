from flask import request
from schema import Schema, Or, And, SchemaError, Optional
from flask import make_response
from src.db import DB
from typing import Type


class Task:
    # add a type hint for the db variable so the editor can help us with function signatures
    def __init__(self, db: Type[DB]):
        self.db = db

    def get(self):
        schema = Schema(
            {
                "action": Or("GetTaskFromId"),
                "parameters": {
                    "taskId": int,
                    "companyId": int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        task_id = req_body["parameters"]["taskId"]
        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "GetTaskFromId":
                res = self.db.get_task_from_id(company_id, task_id)
                # if res is none then no rows have that company id and task id, so return 404
                if res == "null":
                    return make_response("task not found", 404)
                return res

    def delete(self):
        schema = Schema(
            {
                "action": Or("DeleteTaskFromId"),
                "parameters": {
                    "taskId": int,
                    "companyId": int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        task_id = req_body["parameters"]["taskId"]
        company_id = req_body["parameters"]["companyId"]

        match req_body["action"]:
            case "DeleteTaskFromId":
                return self.db.delete_task_from_id(company_id, task_id)

    def post(self):
        schema = Schema(
            {
                "action": Or("CreateTask"),
                "parameters": {
                    "taskName": And(str, len),
                    "companyId": int,
                    Optional("sprintId"): int,
                    Optional("taskDescription"): And(str, len),
                    Optional("storyPoints"): int,
                },
            }
        )

        req_body = request.json

        try:
            schema.validate(req_body)
        except SchemaError as error:
            return make_response(str(error), 400)

        task_name = req_body["parameters"]["taskName"]
        company_id = req_body["parameters"]["companyId"]

        # use the get method to retrieve optional parameters or set the variable to a default value
        sprint_id = req_body["parameters"].get("sprintId", None)
        task_description = req_body["parameters"].get("taskDescription", "")
        story_points = req_body["parameters"].get("storyPoints", 0)

        match req_body["action"]:
            case "CreateTask":
                return self.db.create_task(
                    company_id, task_name, sprint_id, task_description, story_points
                )
