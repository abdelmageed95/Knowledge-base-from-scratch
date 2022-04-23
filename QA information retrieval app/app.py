import json
from flask import Flask, request, render_template
import sql
import qprocessing as qp
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    result = ""
    if request.method == "POST":
        question = request.form['question']
        query_parms = qp.question_processing(question)
        counter =0
        for i in query_parms:
            if i == 'null':
                counter +=1
        if counter < 2:
            result = sql.get_answer(query_parms)
        elif counter == 2:
            result = sql.get_answer(query_parms)
        else:
            result = "No Answer in our KB"

    return render_template('index.html', output = result)
    
if __name__ == '__main__':
    app.run(debug=True)	