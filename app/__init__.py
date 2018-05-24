from flask import Flask,jsonify
import os

app = Flask(__name__,template_folder='movie-genre-prediction')
from app import genre_classification