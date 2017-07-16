# image_viewer
 [![Build Status][2]][3] 

A mini-Python/Flask project with continuous integration testing and deployment. Try it out [here][1] - upload an image to view in browser.

# dependencies

- See [requirements.txt](requirements.txt)

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
6) Open browser to [http://localhost:5000][6]

7) After changes to source code, restart server:
  - ctrl-c
  - re-run step 5 command
  - refresh browser window

# test
In shell, from project root:
```
pytest
```
# contribution instructions
(assumes knowledge of git commands)
1) Fork repo from [github.com/nzey/image_viewer][4]
2) `git clone [your_fork_url]`
3) `git remote add upstream https://github.com/nzey/image_viewer`
4) Make your changes locally
5) Pull from upstream (in case changes have been made since you cloned) and merge with your local changes
6) Test locally (`pytest`)
7) Git add, commit, and push to your own fork (`git push origin master`)
8) Submit pull request (will trigger Travis CI build and deploy to Heroku if build succeeds)

# connect Travis CI to a Github repo
(already done for this repo)
1) Go to [travis-ci.org][7] ([travis-ci.com][8] for private repos)
2) Click on 'Sign in with GitHub' in the top right
3) When account is done syncing, go to https://travis-ci.org/profile/YOUR_GITHUB_HANDLE (if not taken there automatically)
4) To activate Travis for a repository, click on the X next to the repo you want to connect
5) Add .travis.yml file to your repository
- see this project's [yml][9] for a simple example
- see Travis [python specific documentation][10] for more complex examples and additional information
6) Git add, commit, and push with new yml file to your Github repo. Check back on your Travis profile page to see build status.

[1]:https://fathomless-brushlands-41511.herokuapp.com
[2]:https://travis-ci.org/nzey/image_viewer.svg?branch=master
[3]:https://travis-ci.org/nzey/image_viewer
[4]:https://github.com/nzey/image_viewer
[5]:https://virtualenv.pypa.io/en/stable/installation/
[6]:http://localhost:5000
[7]:https://travis-ci.org/
[8]:https://travis-ci.com/
[9]:.travis.yml
[10]:https://docs.travis-ci.com/user/languages/python/