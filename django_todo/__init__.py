import os

if os.path.isfile('env.py'):
    import env
SECRET_KEY = os.environ.get('SECRET_KEY')