# config.py
import os
import datetime
import cloudinary

BASE_DIR = os.getcwd()

class Config:
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    UPLOAD_FOLDER = 'static/img'
    SECRET_KEY = 'curso_flask'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=900000)
    cloudinary.config(
    cloud_name = 'dcdfpnnyp',
    api_key='531989171832749',
    api_secret='-kHcTqhbMJ5VTpToGQxxDTNkE0A'
)

