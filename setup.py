from setuptools import setup
# from pip.req import parse_requirements

setup(name='image viewer',
      version='1.0',
      author='Lindsay Anchors',
      url='https://fathomless-brushlands-41511.herokuapp.com/',
      py_modules=['imageviewer.index'],
      entry_points={
        'console_scripts' : [
            'start=imageviewer.index:server',
        ]
      },
      nclude_package_data=True,
      install_requires= [
        "click==6.7",
        "Flask==0.12.2",
        "gunicorn==19.1.0",
        "itsdangerous==0.24",
        "Jinja2==2.9.6",
        "MarkupSafe==0.23",
        "PasteDeploy==1.5.2",
        "py==1.4.34",
        "pytest==3.1.2",
        "Werkzeug==0.12.2",
      ]
     )