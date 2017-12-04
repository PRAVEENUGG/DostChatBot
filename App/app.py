from flask import Flask
from flask import render_template,jsonify,request
import requests
from models import *
#from response import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

def format_entities(entities):
    """
    formats entities to key value pairs
    """
    e = {}
    for entity in entities:
        e[entity["entity"]] = entity["value"]
    return e

def get_query_results(intent, entities):
    resp = results.get_results(intent,entities)
    return resp
    
@app.route('/chat',methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        res = results()
        response = requests.get("http://localhost:5000/parse",params={"q":request.form["text"]})
        response = response.json()
        intent = response["intent"]["name"]
        entities = format_entities(response["entities"])
        print(entities)
        # at this point we have the intent & entities, now use this to query the db
        print(response)
        response_msg = get_query_results(intent, entities)
        return jsonify({"status":"success","response":response_msg})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True

if __name__ == "__main__":
    app.run(port=8000)
