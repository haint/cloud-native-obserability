from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("main.html")

@app.route("/backend")
def backend():
    response = requests.get("http://backend.default.svc.cluster.local:8081/")
    return response

@app.route("/trial")
def trail():
    response = requests.get("http://trial.default.svc.cluster.local:8082/")
    return response


if __name__ == "__main__":
    app.run()
