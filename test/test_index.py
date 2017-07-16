import sys
sys.path.append('/Users/nzey/devprojects/challenges/photo_loader')
from index import app

def test_img_post():
  "HTTP response data is the file sent with HTTP request"
  response = app.test_client().post('/img',
                          content_type='multipart/form-data',
                          data={'image': open('test/test_image', 'rb')},
                          follow_redirects=True)
  assert open('test/test_image', 'rb').read() == response.data