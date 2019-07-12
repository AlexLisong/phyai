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

def get_category(filename):
  defaults.device = torch.device('cpu')
  img = open_image('static/' + filename)
# img

  learn = load_learner('data')  

  pred_class, pred_idx, outputs = learn.predict(img)
  return pred_class

@app.route("/")
def home():
  import json
  a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
  return jsonify(a)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    #     response = flask.jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

   if request.method == 'POST':
      f = request.files['file']
      name = secure_filename(f.filename)
      f.save(os.path.join('static', name))
      import json
      category = get_category(name)
      a = {'category': str(category)}
      print (a)
      data = jsonify(a)
      data.headers.add('Access-Control-Allow-Origin', '*')
      return data



if __name__ == '__main__':
    # print(get_category('lotus_root.png'))
    app.run(host='0.0.0.0',port=5001)
