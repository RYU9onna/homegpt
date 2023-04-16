import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    user_input = req["handler"]["intent"]["query"]
    response = generate_response(req, user_input)
    return jsonify(response)

def generate_response(req, prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return {
        "session": {
            "id": req["session"]["id"],
            "params": req["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": message,
                "text": message
            }
        }
    }

if __name__ == "__main__":
    app.run(debug=True)
