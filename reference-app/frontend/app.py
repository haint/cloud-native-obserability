from flask import Flask, render_template
import requests

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)


@app.route("/")
def homepage():
    return render_template("main.html")

@app.route("/backend")
def backend():
    response = requests.get("http://backend.default.svc.cluster.local:8081/")
    return response.text

@app.route("/trial")
def trail():
    response = requests.get("http://trial.default.svc.cluster.local:8082/")
    return response.text


if __name__ == "__main__":
    app.run()
