from flask import Flask
from flask import request, jsonify,render_template

app = Flask(__name__)
app.debug = True



@app.route('/', methods=['GET'])
def hello():
    return 'New Hello World !!'

@app.route('/api', methods=['GET', 'POST'])
def api():
    """
    /api entpoint
    GET - returns json= {'status': 'test'}
    POST -  {
            name - str not null
            age - int optional
            }
    :return:
    """

@app.route("/hello",)
def page():
    return render_template("hello.html")

def main():
    app.run(port=8000)

if __name__ == '__main__':
    main()
