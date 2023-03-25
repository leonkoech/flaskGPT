import flask 
from flask import request, jsonify
from Chatbot_for_VR import chatGPT


app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    query_params = request.args
    text = query_params.get('text')
    # function to send to chat gpt
    chats = 'return of function(text)'
    return jsonify(chats)

# handle Errors
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()