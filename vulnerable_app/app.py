from flask import Flask, request, jsonify
import subprocess
import pickle
import base64

app = Flask(__name__)

# Intentionally vulnerable:
# Hardcoded secret
app.config["SECRET_KEY"] = "super-secret-development-key"


@app.get("/")
def index():
    return "Intentionally vulnerable demo application"


@app.get("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    # Intentionally vulnerable:
    # shell=True with user-controlled input
    result = subprocess.check_output(
        f"ping -n 1 {host}",
        shell=True,
        text=True
    )

    return result


@app.get("/calculate")
def calculate():
    expression = request.args.get("expression", "1 + 1")

    # Intentionally vulnerable:
    # eval() on user input
    result = eval(expression)

    return str(result)


@app.post("/profile")
def profile():
    data = request.get_data()

    decoded = base64.b64decode(data)

    # Intentionally vulnerable:
    # unsafe deserialization
    profile_data = pickle.loads(decoded)

    return jsonify(profile_data)


if __name__ == "__main__":
    app.run()