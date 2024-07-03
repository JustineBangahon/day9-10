from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['name']
        birthday = request.form['birthday']
        birthday_year = datetime.strptime(birthday, "%Y-%m-%d").year
        curr_year = datetime.now().year
        age = curr_year - birthday_year

        return jsonify({"name": name, "age": age})
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
