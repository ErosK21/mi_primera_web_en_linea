from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def prueba_servidor_web():
    return render_template("index.html")

if __name__ == "__main__": app.run(debug=True)
