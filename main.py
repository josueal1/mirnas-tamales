from flask import Flask, render_template, request
from bugsnag.flask import handle_exceptions
import os
import bugsnag

bugsnag.configure(
    api_key= os.getenv("BUGSNAG_API_KEY"),
    project_root="./main.py",
)

app = Flask(__name__)
handle_exceptions(app)


@app.route("/")
def index():
    return render_template("gallery.html")


@app.route("/test", methods=["GET", "POST"])
def test():
	if request.method == "GET":
		try:
			raise bugsnag.notify(Exception('getting /test'))
		except Exception as e:
			print("the following exception was raise in program: ", e)

		finally:
			return render_template("gallery.html")

	elif request.method == "POST":
		raise Exception("no code for POST method in /test")
		return "No method here"


if __name__ == "__main__":
    app.run()