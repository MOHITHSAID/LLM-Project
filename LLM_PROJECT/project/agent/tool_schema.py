# agent/tool_schema.py

tools = [
    {
        "name": "get_hotels",
        "description": "Find hotels near a monument location",
        "parameters": {
            "location": {
                "type": "string",
                "description": "City or location name"
            }
        }
    },
    {
        "name": "get_transport",
        "description": "Get transport options between two cities",
        "parameters": {
            "source": {
                "type": "string",
                "description": "Starting city"
            },
            "destination": {
                "type": "string",
                "description": "Destination city"
            }
        }
    }
]
