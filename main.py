# HTML Integration with Flask
# GET AND POST

from flask import Flask, redirect, url_for, render_template, request
# WSGI application initialization
app = Flask(__name__)

# Home/Landing Page


@app.route('/')
def welcome():
    return render_template("index.html")

# About page


@app.route('/about')
def about():
    return "You have come to about page now"

# Dynamic URL building


@app.route('/results/<int:score>')
def results(score):
    exp = {"name": "Rishabh", "score": score}

    return render_template('results.html', total=score, exp=exp)

# Dynamic URL building


# @app.route('/fail/<int:score>')
# def fail(score):
#     return f"You have failed and your total marks is {score}"


# @app.route('/results/<int:marks>')
# def results(marks):
#     result = ''
#     if marks > 30:
#         result = "success"
#     else:
#         result = "fail"
#     return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4

    return redirect(url_for("results", score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
