import os
from flask import Flask, request, jsonify, json, Response, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from instance import app_config
from dotenv import load_dotenv
load_dotenv()


config_name = os.getenv('APP_ENV')
app = Flask(__name__)
app.config.from_object(app_config[config_name])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

from app import routes, models
