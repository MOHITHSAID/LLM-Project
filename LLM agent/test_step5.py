from agent_core import agent_decision
from tool_executor import execute_tool

result = agent_decision("Taj Mahal", "Suggest hotels nearby")

print("Agent Decision:")
print(result)

if result["type"] == "tool_call":
    tool_output = execute_tool(result)
    print("\nTool Output:")
    print(tool_output)
else:
    print("\nText Response:")
    print(result["content"])
