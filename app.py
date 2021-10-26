from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")  # HTTP request:   GET  /
def index():
    return render_template("home.html",
                           title="Home Page",
                           heading="",)


@app.get("/showhome")
def home():
    return render_template("home.html",
                            title="Home Page",
                            heading="",)

@app.get("/showPersonal")
def personal():
    return render_template("personal.html",
                            title="Personal Page",
                            heading="",)

@app.get("/showCV")
def cv():
    return render_template("cv.html",
                            title="CV Page",
                            heading="",)

@app.get("/showComputing")
def computing():
    return render_template("computing.html",
                            title="Computing Page",
                            heading="",)

@app.get("/showInterests")
def interests():
    return render_template("interests.html",
                            title="Interests Page",
                            heading="",)
                            


"""
@app.post("/processfeedback")
def save_data():
    
        Receive the data from the HTML form, then save it to a disk file, then respond
        with a nice friendly message to the awaiting browser.

        The following inputs are expected: first, last, and dob.
    
    # python-name = html-name:
    the_feedback = request.form["feedback"]
    # So... now, use the python-names in your code:
    with open("comments.txt", "a") as sf:
        print(f"{the_feedback}", file=sf) 
        return "Thanks for your feedback"
"""

if __name__ == "__main__":
    app.run(debug=True)
