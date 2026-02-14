import json

def parse_agent_output(agent_output: str):
    """
    Parses agent output and determines whether it is:
    - A tool call (valid JSON)
    - A normal text response
    """

    agent_output = agent_output.strip()

    try:
        parsed = json.loads(agent_output)

        # Validate required structure
        if (
            isinstance(parsed, dict)
            and "action" in parsed
            and "parameters" in parsed
            and isinstance(parsed["parameters"], dict)
            and "location" in parsed["parameters"]
        ):
            return {
                "type": "tool_call",
                "action": parsed["action"],
                "parameters": parsed["parameters"]
            }

    except json.JSONDecodeError:
        pass

    # Fallback: treat as text
    return {
        "type": "text",
        "content": agent_output
    }
