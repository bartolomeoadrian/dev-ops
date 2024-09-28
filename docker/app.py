import os
import flask
import sentry_sdk
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Manejar la falta de variables de entorno
try:
    SENTRY_DSN = os.environ["SENTRY_DSN"]
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
    DEBUG = os.environ["DEBUG"]
except KeyError as e:
    raise RuntimeError(f"Falta la variable de entorno: {e}")


sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(GITHUB_TOKEN),
)

app = flask.Flask(__name__)

app.config["DEBUG"] = DEBUG == "True"


@app.route("/", methods=["GET"])
def index():
    return """<h1>Online</h1>
                <p>The Flask API is running</p>"""


@app.route("/chat", methods=["GET"])
def chat():
    response = client.complete(
        messages=[
            SystemMessage(content="Sos un asistente feliz, podes responder con emojis"),
            UserMessage(content=flask.request.args.get("message")),
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model="meta-llama-3.1-405b-instruct",
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
