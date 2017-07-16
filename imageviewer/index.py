from flask import Flask, request, send_file, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/img', methods=['POST'])
def imgSubmitted():
  f = request.files['image']
  f.save('imageviewer/uploaded_file')
  return send_file('uploaded_file', mimetype=f.mimetype)