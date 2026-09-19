from flask import Flask, render_template, request

app = Flask(__name__)


default_settings = {
    "navbar_items": [
        ["/", "Home"],
        ["/example-page", "Example"],
        # ["/ashley", "ASHLEY"],
        # ashley was here
    ]
}

@app.route("/")
def index():
    return render_template("index.html", **default_settings)

def main():
    app.run(host="127.0.0.1", port=8080, debug=True)
