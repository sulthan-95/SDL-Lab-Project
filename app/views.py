from flask import render_template
from flask import request
from app import app
from .form import SymptomsForm
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import os
import gc


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	form=SymptomsForm()
	return render_template('index1.html',form=form);


@app.route('/results',methods=['POST'])
def results():
	result=SymptomsForm(request.form)
	array=[]
	array.append(result.age.data)
	array.append(result.bp.data)
	array.append(result.sg.data)
	array.append(result.al.data)
	array.append(result.sugar.data)
	if (result.rbc.data == True):
		array.append(1)
	else:
		array.append(0)
	if (result.pus_cell.data == True):
		array.append(1)
	else:
		array.append(0)
	if (result.pcc.data == True):
		array.append(1)
	else:
		array.append(0)
	if (result.bacteria.data == True):
		array.append(1)
	else:
		array.append(0)
	array.append(result.blood_glucose.data)
	array.append(result.blood_urea.data)
	array.append(result.serum.data)
	array.append(result.sodium.data)
	array.append(result.potassium.data)
	array.append(result.hemoglobin.data)
	array.append(result.pcv.data)
	array.append(result.wbc.data)
	array.append(result.rbc.data)
	if(result.ht.data==True):
		array.append(1)
	else:
		array.append(0)
	if(result.diabetes.data==True):
		array.append(1)
	else:
		array.append(0)
	if(result.cad.data==True):
		array.append(1)
	else:
		array.append(0)
	if(result.appetite.data==True):
		array.append(1)
	else:
		array.append(0)
	if(result.pedal.data==True):
		array.append(1)
	else:
		array.append(0)
	if(result.anemia.data==True):
		array.append(1)
	else:
		array.append(0)
	X=numpy.array([array])
	json_file=open('/home/mahmood/Documents/RNN_Project/tmp/model.json','r')
	json_loaded_model=json_file.read()
	json_file.close()
	  	#load the model from json file
	model = model_from_json(json_loaded_model)
       	#load the weights into new model
	model.load_weights("/home/mahmood/Documents/RNN_Project/tmp/model.h5")
	model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
	Y=model.predict(X)
	res=[round(x[0]) for x in Y]
	if(res[0]==1.0):
		fil="You have CKD.. Sorry"
	else:
		fil="Be happy... You have no disease.. Live Long"
	return render_template('results.html',res=fil);


