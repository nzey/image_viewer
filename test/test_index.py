import sys
import os
ROOT = os.path.abspath(__file__)[0:-len('test/test_index.py')]
sys.path.append(ROOT)
from index import app

def test_img_post():
  "HTTP response data is the file sent with HTTP request"
  test_img_filename = 'test/test_image'
  response = app.test_client().post('/img',
                          content_type='multipart/form-data',
                          data={'image': open(test_img_filename, 'rb')},
                          follow_redirects=True)
  assert open(test_img_filename, 'rb').read() == response.data