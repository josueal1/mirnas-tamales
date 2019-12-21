from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Header to be committed to master -> prod </h1>"



if __name__ == "__main__":
    app.run(debug=True)