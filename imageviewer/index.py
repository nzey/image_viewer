from flask import Flask, request, send_file, render_template
from tempfile import NamedTemporaryFile
import os 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/img', methods=['POST'])
def imgSubmitted():
  with NamedTemporaryFile() as temp:
    f = request.files['image']
    mimetype = f.mimetype
    f.save(temp)
    f.close
    temp.seek(0)
    return send_file(temp.name, mimetype=mimetype)

def server():
  print('SERVER START SCRIPT RUN -------------------------')
  os.environ["FLASK_APP"]='imageviewer/index.py'
  os.system('flask run')