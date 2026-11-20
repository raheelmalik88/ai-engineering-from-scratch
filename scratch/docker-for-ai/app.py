from flask import Flask
import torch

app = Flask(__name__)


@app.route("/")
def hello():
    return {"message": "Hello from inside the container", "torch": torch.__version__}


if __name__ == "__main__":
    # 0.0.0.0, not localhost: a server bound to localhost inside the
    # container cannot be reached from the Mac
    app.run(host="0.0.0.0", port=5000)
