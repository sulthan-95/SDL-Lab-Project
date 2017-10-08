from flask import render_template
from app import app
#from .forms import SymptomsForm
@app.route('/')
@app.route('/index')
def index():
	return render_template('index1.html');

