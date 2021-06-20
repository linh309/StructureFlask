import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Statement for enabling the development environment
DEBUG = True

SECRET_KEY = 'dev'

DATABASE = os.path.join(BASE_DIR, 'db','flaskr.sqllite')