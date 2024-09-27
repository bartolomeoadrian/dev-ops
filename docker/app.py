import os
import flask
import sentry_sdk
from dotenv import load_dotenv

load_dotenv(override=True)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = flask.Flask(__name__)

app.config["DEBUG"] = os.getenv("DEBUG") == "True"


@app.route("/", methods=["GET"])
def index():
    return """<h1>Online</h1>
                <p>The Flask API is running</p>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
