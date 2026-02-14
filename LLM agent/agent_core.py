import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ---------------------------
# Local LLM
# ---------------------------
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto"
)
model.eval()

# ---------------------------
# Rule-Based Intent Detection
# ---------------------------
def rule_based_intent(query: str):
    q = query.lower()

    if "cheap stay" in q or "budget stay" in q:
        return "get_budget_stays"
    if "hotel" in q or "stay" in q:
        return "get_hotels"
    if "restaurant" in q or "food" in q or "eat" in q:
        return "get_restaurants"
    if "cheap food" in q:
        return "get_budget_food"
    if "cheapest travel" in q or "cheap travel" in q:
        return "get_cheapest_travel"
    if "transport" in q or "bus" in q or "train" in q:
        return "get_local_transport"
    if "flight" in q or "airport" in q:
        return "get_flights"

    return None

# ---------------------------
# LLM-Based Intent Inference
# ---------------------------
def llm_intent_inference(query: str):
    prompt = f"""
User query: "{query}"

Classify the user's intent into ONE of the following labels:
- hotels
- budget_stays
- restaurants
- budget_food
- cheapest_travel
- local_transport
- flights
- info

Respond with ONLY the label.
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=20,
            do_sample=False
        )

    label = tokenizer.decode(output[0], skip_special_tokens=True).strip().lower()

    mapping = {
        "hotels": "get_hotels",
        "budget_stays": "get_budget_stays",
        "restaurants": "get_restaurants",
        "budget_food": "get_budget_food",
        "cheapest_travel": "get_cheapest_travel",
        "local_transport": "get_local_transport",
        "flights": "get_flights",
        "info": "info"
    }

    return mapping.get(label, "info")

# ---------------------------
# Final Agent Decision
# ---------------------------
def agent_decision(monument_name: str, user_query: str):

    # Step 1: Try rule-based
    intent = rule_based_intent(user_query)

    # Step 2: If not found, infer via LLM
    if intent is None:
        intent = llm_intent_inference(user_query)

    # Step 3: Tool or info
    if intent != "info":
        return {
            "type": "tool_call",
            "action": intent,
            "parameters": {
                "location": monument_name
            }
        }

    # Step 4: Info response via LLM
    prompt = f"""
Provide clear information.

Monument: {monument_name}
User Question: {user_query}
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=False
        )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return {
        "type": "text",
        "content": response
    }
