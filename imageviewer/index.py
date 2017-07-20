from flask import Flask, request, send_file, render_template
from tempfile import TemporaryFile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/img', methods=['POST'])
def imgSubmitted():
  temp = TemporaryFile(suffix='.jpg')
  f = request.files['image']
  f.save(temp)
  temp.seek(0)
  response = send_file(temp, mimetype=f.mimetype)
  f.close
  temp.close
  return response
