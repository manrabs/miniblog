import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-aint-gon-believe-this'