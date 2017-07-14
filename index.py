from flask import Flask, send_file
from flask import request

app = Flask(__name__)

import json

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