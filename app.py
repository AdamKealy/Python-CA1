from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("home.html",
                           title="Home Page",
                           heading="",)


@app.get("/showhome")
def home():
    return render_template("home.html",
                            title="Home Page",
                            heading="Home Page",)

@app.get("/showPersonal")
def personal():
    return render_template("personal.html",
                            title="Personal Page",
                            heading="Personal Page",)

@app.get("/showCV")
def cv():
    return render_template("cv.html",
                            title="CV Page",
                            heading="CV Page",)

@app.get("/showComputing")
def computing():
    return render_template("computing.html",
                            title="Computing Page",
                            heading="Computing Page",)

@app.get("/showInterests")
def interests():
    return render_template("interests.html",
                            title="Interests Page",
                            heading="Interests Page",)

                            
@app.post("/processfeedback")
def save_data():
    the_email = request.form["email"]
    the_feedback = request.form["feedback"]
    with open("comments.txt", "a") as sf:
        print(f"{the_email}, {the_feedback}", file=sf) 
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
