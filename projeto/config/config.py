# config.py
import os
import datetime
import cloudinary
import secrets

BASE_DIR = os.getcwd()

class Config:
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    #SQLALCHEMY_DATABASE_URI =  'sqlite:///database.db'
    #UPLOAD_FOLDER = 'static/img'
    SECRET_KEY = secrets.token_hex(32)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=900000)
    cloudinary.config(
    cloud_name = 'dsqxpduuv',
    api_key='456834939959468',
    api_secret='FEwY5iPu4RS_sG0h_vlNYPVIfDE'
)

