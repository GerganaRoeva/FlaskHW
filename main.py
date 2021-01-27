from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    return render_template("login.html")
    # else:
    #     return "hihi"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if request.method == 'POST':
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)