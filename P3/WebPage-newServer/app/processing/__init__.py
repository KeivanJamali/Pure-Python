from flask import Blueprint

bp = Blueprint('processing', __name__)

from app.processing import routes
