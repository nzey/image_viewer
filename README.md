# image_viewer
[![Build Status][2]][3]

A mini python flask project ([deployed here][1]). Upload an image to view in browser.

# dependencies

- see [requirements.txt](requirements.txt)

# run locally

Complete the following tasks from the command line:

1) Install python version and package manager [virtualenv][5]:
```
[sudo] pip install virtualenv
```
2) Create a virtualenv named *venv*:**
```
virtualenv venv
```
** *if you choose a different environment name, be sure to add the name to the .gitignore file in the virtualenv section.*

3) Activate your new environment:
```
source activate venv
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) From project root:  
  ```
  export FLASK_APP=index.py && flask run
  ```
6) open browser to [http://localhost:5000][6]

7) After changes to source code, restart server:
  - ctrl-c
  - re-run step 5 command
  - refresh browser window

# test
In shell, from project root:
```
pytest
```


[1]:https://fathomless-brushlands-41511.herokuapp.com
[2]:https://travis-ci.org/nzey/image_viewer
[3]:https://travis-ci.org/nzey/image_viewer
[5]:https://virtualenv.pypa.io/en/stable/installation/
[6]:http://localhost:5000