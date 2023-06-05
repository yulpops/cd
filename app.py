from flask import Flask
from flask import request, jsonify,render_template

app = Flask(__name__)
app.debug = True

asfasfa

@app.route('/', methods=['GET'])
def hello():
    return 'Last Hello World !!'


@app.route("/hello",)
def page():
    return render_template("hello.html")

@app.route("/main",)
def page2():
    return render_template("index.html")

def main():
    app.run(port=8000)

if __name__ == '__main__':
    main()
