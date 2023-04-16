import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    user_input = req.get("handler", {}).get("intent", {}).get("query", "")
    intent_name = req.get("handler", {}).get("intent", {}).get("displayName", "")
    
    response = generate_response(intent_name, user_input)
    return jsonify(response)

def generate_response(intent_name, prompt):
    # ここでインテントを処理して、適切な応答を生成します。
    if intent_name == "your_intent_name":
        response_text = "your_response"
    elif intent_name == "another_intent_name":
        response_text = "another_response"
    else:
        response_text = "I'm not sure how to help with that."
        
    return {
        "session": {
            "id": req["session"]["id"],
            "params": req["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": response_text,
                "text": response_text
            }
        }
    }

if __name__ == "__main__":
    app.run(debug=True)
