from flask import request


class Sprint:
    def __init__(self, db):
        self.db = db

    def get(self):
        request_json = request.json
        match request_json["action"]:
            case "GetAllSprintsForCompany":
                return self.db.get_sprints_for_company(
                    company_id=request_json["parameters"]["companyId"]
                )
