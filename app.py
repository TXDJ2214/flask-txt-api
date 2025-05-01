from flask import Flask, request, Response
import os

app = Flask(__name__)
ALLOWED_DIR = "."  # Limit file access to current directory


def safe_filename(name):
    # For now, allow anything ending in .txt for testing
    print(f"🔎 Requested filename: {name}")
    if name.endswith(".txt"):
        return name
    print("❌ Rejected filename")
    return None


@app.route("/file/<filename>", methods=["GET"])
def get_file(filename):
    safe_name = safe_filename(filename)
    if not safe_name:
        return Response("Invalid filename", status=400)
    path = os.path.join(ALLOWED_DIR, safe_name)
    if not os.path.exists(path):
        return Response("File not found", status=404)
    with open(path, "r", encoding="utf-8") as f:
        return Response(f.read(), mimetype="text/plain")


@app.route("/file/<filename>", methods=["PUT"])
def put_file(filename):
    safe_name = safe_filename(filename)
    if not safe_name:
        return Response("Invalid filename", status=400)
    path = os.path.join(ALLOWED_DIR, safe_name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(request.data.decode("utf-8"))
    return f"{safe_name} updated."


@app.route("/", methods=["GET"])
def index():
    return "✅ Flask file server is running."


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
