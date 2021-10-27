from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("home.html", title="Home Page", heading="", isHome=True,)


@app.get("/showhome")
def home():
    return render_template(
        "home.html", title="Home Page", heading="Home Page", isHome=True,
    )


@app.get("/showPersonal")
def personal():
    return render_template(
        "personal.html", title="Personal Page", heading="Personal Page", isHome=False,
    )


@app.get("/showCV")
def cv():
    return render_template("cv.html", title="CV Page", heading="CV Page", isHome=False,)


@app.get("/showComputing")
def computing():
    return render_template(
        "computing.html",
        title="Computing Page",
        heading="Computing Page",
        isHome=False,
    )


@app.get("/showInterests")
def interests():
    return render_template(
        "interests.html",
        title="Interests Page",
        heading="Interests Page",
        isHome=False,
    )


@app.get("/showAr")
def ar():
    return render_template(
        "ar.html",
        title="Augmented Reality Page",
        heading="Augmented Reality Page",
        isHome=False,
    )


@app.get("/showCloudComputing")
def cloudComputing():
    return render_template(
        "cloud_computing.html",
        title="Cloud Computing Page",
        heading="Cloud Computing Page",
        isHome=False,
    )


@app.get("/showEmbeddedSoftware")
def embeddedSoftware():
    return render_template(
        "embedded_software.html",
        title="Embedded Software Page",
        heading="Embedded Software Page",
        isHome=False,
    )


@app.post("/processfeedback")
def save_data():
    the_email = request.form["email"]
    the_feedback = request.form["feedback"]
    with open("comments.txt", "a") as sf:
        print(f"{the_email}, {the_feedback}", file=sf)
        return render_template("home.html", title="Home Page", heading="",)


if __name__ == "__main__":
    app.run(debug=True)
