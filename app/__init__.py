from flask import Flask
from .models import Library

app = Flask(__name__)
app.config.from_object('config.Config')  # This line imports the Config class from config.py

library = Library()

from app import routes
