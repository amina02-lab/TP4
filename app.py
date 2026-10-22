from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Cloud Computing Lab - PaaSRdeeeep</h1>
<p>This application is deployed using a Platform as a Service.</p>
"""

@app.route("/about")
def about():
    return """
    <h1>About This Application</h1>
    <p>This application was developed for a Cloud Computing lab.</p>
    <p>It is deployed using Render, a PaaS platform.</p>
    """
