from flask import Flask, request, Response
import os

app = Flask(__name__)
DATA_FILE = "data.txt"

@app.route("/data.txt", methods=["GET"])
def get_file():
    if not os.path.exists(DATA_FILE):
        return Response("File not found.", status=404)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return Response(f.read(), mimetype="text/plain")

@app.route("/data.txt", methods=["PUT"])
def update_file():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(request.data.decode("utf-8"))
    return "File updated."

@app.route("/", methods=["GET"])
def index():
    return "✅ Flask file server is running."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

