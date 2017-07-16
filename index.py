from flask import Flask, request, send_file
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Image Viewer</title>
    </head>
    <body>
      <h1>Image Viewer</h1>
      <form action="/img" method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <input type="submit">
      </form>
    </body>
    </html>
  '''

@app.route('/img', methods=['POST'])
def imgSubmitted():
  f = request.files['image']
  f.save('uploaded_file')
  return send_file('uploaded_file', mimetype=f.mimetype)