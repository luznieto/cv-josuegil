from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
