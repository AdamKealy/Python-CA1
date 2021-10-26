from flask import Flask, request, render_template
import datetime

app = Flask(__name__)


@app.get("/")  # HTTP request:   GET  /
def index():
    return render_template("index.html",
                           title="Welcome!",
                           heading="Tell us about yourself",)


@app.get("/showform")
def display_form():
    """
        Retrieve the form.html file from the hard disk, and send it to the
        browser.
    """
    return render_template("form.html",
                           title="Welcome Form",
                           heading="Please fill in this form",)


@app.post("/processfeedback")
def save_data():
    """
        Receive the data from the HTML form, then save it to a disk file, then respond
        with a nice friendly message to the awaiting browser.

        The following inputs are expected: first, last, and dob.
    """
    # python-name = html-name:
    the_feedback = request.form["feedback"]
    # So... now, use the python-names in your code:
    with open("comments.txt", "a") as sf:
        print(f"{the_feedback}", file=sf) 


if __name__ == "__main__":
    app.run(debug=True)
