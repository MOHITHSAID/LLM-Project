def format_response(agent_result, tool_result=None):

    if agent_result["type"] == "text":
        return agent_result["content"]

    action = agent_result["action"]

    if action == "get_hotels":
        return "\n".join(
            [f"🏨 {h['name']} ⭐ {h['rating']}" for h in tool_result]
        )

    if action == "get_budget_stays":
        return "\n".join(
            [f"💰 {h['name']} – ₹{h['price']}/night" for h in tool_result]
        )

    if action == "get_restaurants":
        return "\n".join(
            [f"🍽️ {r['name']} ⭐ {r['rating']}" for r in tool_result]
        )

    if action == "get_budget_food":
        return "\n".join(
            [f"🥘 {f['name']} – ₹{f['price']}" for f in tool_result]
        )

    if action == "get_cheapest_travel":
        return (
            f"🚍 Cheapest Travel:\n"
            f"Mode: {tool_result['mode']}\n"
            f"Cost: ₹{tool_result['cost']}\n"
            f"Time: {tool_result['time']}"
        )

    if action == "get_local_transport":
        return (
            f"🚕 Local Transport:\n"
            f"Bus: {tool_result['bus']}\n"
            f"Auto: {tool_result['auto']}\n"
            f"Taxi: {tool_result['taxi']}"
        )

    if action == "get_flights":
        return (
            f"✈️ Flights:\n"
            f"Airport: {tool_result['airport']}\n"
            f"Price: ₹{tool_result['price']}\n"
            f"Duration: {tool_result['duration']}\n"
            f"Next Flight: {tool_result['next_flight']}"
        )

    return "No information available"
