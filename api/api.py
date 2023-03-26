import flask 
from flask import request, jsonify
from Chatbot_for_VR import chatGPT

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "welcome"

@app.route('/api/<text>', methods=['GET'])
def chat(text):
     chats = chatGPT(text)
     return jsonify(chats)

# handle Errors
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()