from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def ai():
    input_user = ""
    if request.method == "POST":
        input_user = request.form['input']
    print(input_user)
    return render_template("index.html")

app.run(debug=True)