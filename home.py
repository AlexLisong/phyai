import os
from fastai import *
from fastai.imports import *
from fastai.vision import *
from fastai.metrics import error_rate
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64
import json

from werkzeug import secure_filename
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

CORS(app)

def get_category(filename):
  defaults.device = torch.device('cpu')
  img = open_image('static/' + filename)

  learn = load_learner('data')

  pred_class, pred_idx, outputs = learn.predict(img)
  return pred_class

def get_dog_category(filename):
  defaults.device = torch.device('cpu')
  img = open_image('static/' + filename)

  learn = load_learner('dog_data')

  pred_class, pred_idx, outputs = learn.predict(img)
  return pred_class

@app.route("/")
def home():
    return render_template('file.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():

   if request.method == 'POST':
      f = request.files['file']
      name = secure_filename(f.filename)
      f.save(os.path.join('static', name))
      category = get_category(name)
      a = {'category': str(category), 'desc': '123'}
      print (a)
      data = jsonify(a)
      data.headers.add('Access-Control-Allow-Origin', '*')
      return data

@app.route('/upload_dog_b64', methods=['POST'])
def upload_base64_file():

    data = request.get_json()

    if data is None:
       print("No valid request body, json missing!")
       return jsonify({'error': 'No valid request body, json missing!'})
    else:
       img_data = data['img']

       name = convert_and_save(img_data)
       category = get_dog_category(name)

       a = {'category': str(category), 'desc': '123'}
       print (a)
       data = jsonify(a)
       data.headers.add('Access-Control-Allow-Origin', '*')
       return data

@app.route('/upload_b64', methods=['POST'])
def upload_base64_file():

    data = request.get_json()

    if data is None:
       print("No valid request body, json missing!")
       return jsonify({'error': 'No valid request body, json missing!'})
    else:
       img_data = data['img']

       name = convert_and_save(img_data)
       category = get_category(name)

       a = {'category': str(category), 'desc': '123'}
       print (a)
       data = jsonify(a)
       data.headers.add('Access-Control-Allow-Origin', '*')
       return data

def convert_and_save(b64_string):
    imgdata = base64.b64decode(b64_string)
    name = secure_filename("imageToSave.jpg")
    with open(os.path.join('static',name), 'wb') as f:
        f.write(imgdata)
    return name


if __name__ == '__main__':
    # print(get_category('lotus_root.png'))
    app.run(host='0.0.0.0',port=5001)
