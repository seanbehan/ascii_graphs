from flask import Flask, request
from lib import barchart

app = Flask(__name__)

@app.route("/")
def home():
    return "ASCII Charts!"

@app.route("/bar")
def bar_graph():
    lst = map(lambda s: int(s), request.values.get('values').encode('utf-8').split(','))
    return barchart(lst), 200, {'Content-Type': 'text/plain'}

if __name__=='__main__':
    app.run(debug=True)
