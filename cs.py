import json

MODEL_FILE = "merged_modelfile.jsonl"

def load_responses():
    responses = []
    with open(MODEL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                responses.append(json.loads(line))
            except Exception:
                continue
    return responses

def find_response(prompt, responses):
    prompt_lower = prompt.strip().lower()
    for entry in responses:

        if "prompt" in entry:
            if isinstance(entry["prompt"], list):
                if any(prompt_lower == p.lower() for p in entry["prompt"]):
                    return entry["response"]
            elif prompt_lower == entry["prompt"].lower():
                return entry["response"]
        elif "prompts" in entry:
            if any(prompt_lower == p.lower() for p in entry["prompts"]):
                return entry["response"]

    return "I'm here to help with customer support only. Please ask about your order or account."

if __name__ == "__main__":
    responses = load_responses()
    print("Customer Support Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = find_response(user_input, responses)
        print("Bot:", response)