import requests

def call_tool(tool_name, args):

    if tool_name == "get_hotels":
        return requests.post(
            "http://127.0.0.1:8000/hotels",
            json=args
        ).json()

    elif tool_name == "get_transport":
        return requests.post(
            "http://127.0.0.1:8000/transport",
            json=args
        ).json()

    elif tool_name == "get_traffic":
        return requests.post(
            "http://127.0.0.1:8000/traffic",
            json=args
        ).json()

    return {"error": "Tool not found"}
