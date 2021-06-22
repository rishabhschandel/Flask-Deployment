from flask import Flask, redirect, url_for
# WSGI application initialization
app = Flask(__name__)

# Home/Landing Page


@app.route('/')
def welcome():
    return "<h1>Welcome to this page!</h1>"

# About page


@app.route('/about')
def about():
    return "You have come to about page now"

# Dynamic URL building


@app.route('/success/<int:score>')
def success(score):
    return f"You have passed and your total marks is {score}"

# Dynamic URL building


@app.route('/fail/<int:score>')
def fail(score):
    return f"You have failed and your total marks is {score}"


@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks > 30:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))


if __name__ == "__main__":
    app.run(debug=True)
