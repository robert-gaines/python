import os

class Config(object):
    #
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MyB70Vb3kJbfKWX4ltE5'