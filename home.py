import os
from fastai import *
from fastai.imports import *
from fastai.vision import *
from fastai.metrics import error_rate
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from werkzeug import secure_filename
app = Flask(__name__)
CORS(app)

def test():
  defaults.device = torch.device('cpu')
  img = open_image(path/'static/lotus_root.png')
# img

  learn = load_learner(path/'data/export.pkl')  

  pred_class, pred_idx, outputs = learn.predict(img)
  pred_class

@app.route("/")
def home():
  import json
  a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
  defaults.device = torch.device('cpu')
  img = open_image(path/'static/home-mid.jpg')
# img


  pred_class, pred_idx, outputs = learn.predict(img)
  pred_class

  learn = load_learner(path)  
  # a python dictionary
  return jsonify(a)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    #     response = flask.jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join('static', secure_filename(f.filename)))
      import json
      a = {'name':f.filename }
      data = jsonify(a)
      data.headers.add('Access-Control-Allow-Origin', '*')
      return data



if __name__ == '__main__':
    test()
    # app.run(host='0.0.0.0')
