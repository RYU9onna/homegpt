from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)

    # リクエストデータをログに出力
    print("Request data:")
    print(json.dumps(req, indent=2))

    # 'inputs'キーが存在しない場合のデフォルト値を設定
    user_input = "default_value"

    # 'inputs'キーが存在する場合にのみ、値を取得
    if "inputs" in req:
        user_input = req["inputs"][0]["intent"]["query"]

    # 以降の処理（例：GPT-4 による応答の生成）

    response = {
        "result": "success",
        "message": f"User input: {user_input}"
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
