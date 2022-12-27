from flask import Response, Flask
from werkzeug.routing import Rule

app = Flask(__name__)
app.url_map.add(Rule("/<path:path>", endpoint="catch_all"))


@app.route("/", defaults={"path": ""})
@app.endpoint("catch_all")
def catch_all(path):
    return Response("Error", status=500)
