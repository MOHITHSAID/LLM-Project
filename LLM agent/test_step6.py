from agent_core import agent_decision
from tool_executor import execute_tool
from response_formatter import format_response

# Simulate user query
agent_result = agent_decision("Taj Mahal", "Suggest hotels nearby")

print("Agent Result:")
print(agent_result)

# Tool-based flow
if agent_result["type"] == "tool_call":
    tool_result = execute_tool(agent_result)
    final_answer = format_response(agent_result, tool_result)
else:
    final_answer = format_response(agent_result)

print("\nFINAL ANSWER:")
print(final_answer)
