from flask import Flask, render_template, url_for, request,jsonify
import os
import json

app = Flask(__name__)

path = 'data/'

if not os.path.exists(path):
    os.mkdir(path)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/result',methods=["POST","GET"])
def result():
    fname = request.form['fname']
    lname = request.form['lname']
    cnumber = request.form['cnumber']
    email = request.form['email']
    jdata = request.form.to_dict()

    with open(f"{path}/log.json", "a+") as outfile:
        json.dump(jdata, outfile)

    try:
        return render_template('result.html', data=jdata)
    except:
        return render_template('result.html', data="Error Data")
        
if __name__ == "__main__":
    app.run(debug=True, port=8000)