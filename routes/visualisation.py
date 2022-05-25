from flask import Blueprint
from controllers.viz import dataViz, visualisation


visualisations = Blueprint('visualisation', __name__) 


visualisations.route('/viz')(visualisation)

visualisations.route('/dataViz/')(dataViz)
