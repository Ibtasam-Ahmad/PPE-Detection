from urllib import response
from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/<int:id>')
def hello_world(id):
    multipy=id*2
    response={
        "multiply":90
    }
    return jasonify(response)

    if __name__== '__main__':
        app.run