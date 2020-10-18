from flask import Flask, render_template
from bugsnag.flask import handle_exceptions
import os
import bugsnag


app = Flask(__name__)

bugsnag.configure(
    api_key= os.environ.get("BUGSNAG_API_KEY"),
    project_root="./main.py",
)

@app.route("/")
handle_exceptions(app)

def index():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run()