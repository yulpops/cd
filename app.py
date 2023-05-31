from flask import Flask
from flask import request, jsonify,render_template

app = Flask(__name__)
app.debug = True



@app.route('/', methods=['GET'])
def hello():
    return 'Test Hello World !!'


@app.route("/hello",)
def page():
    return render_template("hello.html")

def main():
    app.run(port=8000)

if __name__ == '__main__':
    main()
