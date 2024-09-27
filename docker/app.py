import os
import flask
import sentry_sdk
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

app = flask.Flask(__name__)

app.config["DEBUG"] = os.environ["DEBUG"] == "True"


@app.route("/", methods=["GET"])
def index():
    return """<h1>Online</h1>
                <p>The Flask API is running</p>"""


@app.route("/chat", methods=["GET"])
def chat():
    response = client.complete(
        messages=[
            SystemMessage(content="You are a helpful assistant."),
            UserMessage(content=flask.request.args.get("message")),
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
