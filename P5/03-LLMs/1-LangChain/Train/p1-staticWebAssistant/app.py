from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import run_agent
import traceback

app = Flask(__name__)
CORS(app)

user_sessions = {}

API_KEY = "K1ovn39nsfs49mlsg"

def get_user_id():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'unknown')
    return f"{user_ip}_{hash(user_agent)}"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    if not data or "api_key" not in data or "query" not in data:
        return jsonify({"error": "Invalid request. 'api_key' and 'query' are required."}), 400

    if data["api_key"] != API_KEY:
        return jsonify({"error": "Unauthorized. Invalid API key."}), 403

    query = data["query"]
    user_id = get_user_id()

    try:
        print("[INFO] Processing query:", query)
        response = run_agent(user_id=user_id, query=query)
        print("[INFO] Response generated successfully.")
        return jsonify({"answer": response}), 200

    except Exception as e:
        print("ERROR IN /generate:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)