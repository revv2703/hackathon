from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def ai():
    input_user = request.args.get("input")
    return render_template("index.html")

app.run(debug=True)