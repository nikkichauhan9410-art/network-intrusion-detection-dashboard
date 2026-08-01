from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Network Intrusion Detection Dashboard"

if __name__ == "__main__":
    app.run(debug=True)
