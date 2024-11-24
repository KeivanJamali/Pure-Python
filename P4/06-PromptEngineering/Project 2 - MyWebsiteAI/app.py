from flask import Flask, request, jsonify, session
from KPG import KPG
from flask_cors import CORS
from uuid import uuid4


app = Flask(__name__)
CORS(app)

user_sessions = {}

# Load the API key from environment variables or set it directly

def get_user_id():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'unknown')
    return f"{user_ip}_{hash(user_agent)}"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    # Validate request structure
    if not data or "api_key" not in data or "query" not in data:
        return jsonify({"error": "Invalid request. 'api_key' and 'query' are required."}), 400

    # Validate API key
    if data["api_key"] != API_KEY:
        return jsonify({"error": "Unauthorized. Invalid API key."}), 403

    # Get the query
    query = data["query"]
    user_id = get_user_id()

    try:
        docs_path = r"D:\All Python\Pure-Python\P4\06-PromptEngineering\Project 2 - MyWebsiteAI\docs"
        log_path = r"D:\All Python\Pure-Python\P4\06-PromptEngineering\Project 2 - MyWebsiteAI\RR"
        user = KPG(
                   model_name=KPG.models["Meta"][0],
                   temp=0.2)
        user.fit(documents_folder_path=docs_path,
                 log_folder_path=log_path,
                 user_id=user_id)
        response = user.generate(query=query)

        return jsonify({"answer": response}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)