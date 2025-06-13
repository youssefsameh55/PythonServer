from flask import Flask, request, jsonify

app = Flask(__name__)
latest_ip = None

@app.route("/register", methods=["POST"])
def register():
    global latest_ip
    data = request.get_json()

    # Get IP from JSON payload if present, else fallback to remote_addr
    latest_ip = data.get("ip") if data and "ip" in data else request.remote_addr

    return jsonify({"status": "ok", "ip": latest_ip})

@app.route("/get_ip", methods=["GET"])
def get_ip():
    if latest_ip:
        return jsonify({"ip": latest_ip})
    return jsonify({"error": "No IP registered"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
