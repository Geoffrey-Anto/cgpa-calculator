from flask import Flask, request
from gpa import read_csv_server

import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gpa", methods = ["POST"])
def gpa():
    # get body
    try:
        f = request.files["gpa.csv"]
    except:
        return {
            "error": "Invalid file name, must be gpa.csv"
        }
    fileData = None
    try:
        fileData = f.stream.read().decode("utf-8")
    except:
        return {
            "error": "Invalid file"
        }
    if fileData == None:
        return {
            "error": "Invalid file"
        }
    try:
        return {
            "gpa": read_csv_server(fileData)
        }
    except:
        return {
            "error": "Invalid file Or Server Error"
        }
     
#get from env        
PORT= os.environ.get("PORT", 5000)
        
app.run(port=int(PORT))
