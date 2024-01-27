from flask import Blueprint

# Create a Blueprint object
receiptsroutesobject = Blueprint("receiptsroutes", __name__)

# Import the routes from receiptsroutes.py
from . import receiptsroutes
