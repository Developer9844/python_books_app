from flask import Flask, render_template, request, redirect, url_for
from .models import Library

app = Flask(__name__)
app.config.from_object('config.Config')  # This line imports the Config class from config.py

library = Library()

from app import routes
# Creating SQLAlchemy instance
