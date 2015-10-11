from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def thanks_page():
    """Accepts form data and returns a thank-you page."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    position = request.form.get("position")
    salary = request.form.get("salary")

    return "Thank you, {} {}, for applying to be a {}. Your minimum salary requirement is {} dollars.".format(first_name, last_name, position, salary)


if __name__ == "__main__":
    app.run(debug=True)
