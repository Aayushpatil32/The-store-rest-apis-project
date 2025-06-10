import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MacBook2024@127.0.0.1:3306/Unbetable_store'
    SQLALCHEMY_TRACK_MODIFICATIONS = False