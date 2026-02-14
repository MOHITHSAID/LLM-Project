def execute_tool(tool_data: dict):
    action = tool_data["action"]
    location = tool_data["parameters"]["location"]

    MOCK_DATA = {
        "get_hotels": [
            {"name": "Oberoi Amarvilas", "rating": 4.8},
            {"name": "Taj View Hotel", "rating": 4.5}
        ],
        "get_budget_stays": [
            {"name": "Hotel Saniya", "price": 1200},
            {"name": "Zostel Agra", "price": 900}
        ],
        "get_restaurants": [
            {"name": "Pinch of Spice", "rating": 4.6},
            {"name": "Joney’s Place", "rating": 4.4}
        ],
        "get_budget_food": [
            {"name": "Sharma Chaat", "price": 80},
            {"name": "Local Dhaba", "price": 120}
        ],
        "get_cheapest_travel": {
            "mode": "Train",
            "cost": 120,
            "time": "2.5 hrs"
        },
        "get_local_transport": {
            "bus": "Every 15 mins",
            "auto": "₹50",
            "taxi": "₹250"
        },
        "get_flights": {
            "airport": "Agra Airport",
            "price": 3200,
            "duration": "1.2 hrs",
            "next_flight": "18:30"
        }
    }

    return MOCK_DATA.get(action, {"error": "No data"})
