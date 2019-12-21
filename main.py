from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Header to be committed to master -> prod"



if __name__ == "__main__":
    app.run()