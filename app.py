
import json
from flask import Flask, request
import sql
import qprocessing as qp
app = Flask(__name__)
	
@app.route("/predict",methods=['GET'])
def predict():

    question = request.args.get('question')
    query_parms = qp.question_processing(question)
    result = sql.get_answer(query_parms)
    return str(result)
    
if __name__ == '__main__':
    from waitress import serve
    serve(app, port=5000)	