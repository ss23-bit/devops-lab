import os
from flask import Flask

app = Flask(__name__)

container_id = os.uname()[1]


@app.route("/")
def hello():
    return f"Production API: Ready | Serve by: {container_id}\n"


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
