import json


bad_request = json.dumps(
    {
        "status": 400,
        "result": False,
        "addition": {},
        "description": {}
    }
)

ping_request = json.dumps(
    {
        "status": 200,
        "result": True,
        "addition": {},
        "description": {}
    }
)

not_exist = json.dumps(
            {
                "status": 404,
                "result": False,
                "addition": {},
                "description":
                    {'info': 'Account does not exist'}
            }
        )

def closed(account):
    return json.dumps(
            {
                "status": 412,
                "result": False,
                "addition": account.get_json(),
                "description":
                    {'info': 'Account closed'}
            }
        )

def invalid_value(account):
    return json.dumps(
            {
                "status": 400,
                "result": False,
                "addition": account.get_json(),
                "description": {}
            }
        )

def ok(account):
    return json.dumps(
            {
                "status": 200,
                "result": True,
                "addition": account.get_json(),
                "description": {}
            }
        )

def negative(account):
    return json.dumps(
            {
                "status": 412,
                "result": False,
                "addition": account.get_json(),
                "description": {}
            }
    )