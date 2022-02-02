import urllib3
from flask import Flask, request, redirect


app = Flask(__name__)


@app.route("/")
def index():
    if request.args.get("r"):

        return redirect(request.args.get("r"))

    return "Hello {name}".format(name=request.args.get("name", "stranger"))


if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)

