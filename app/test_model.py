#Import the model for testing output
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
import gc

dataset=numpy.genfromtxt('../tmp/preprocessed_train.csv', delimiter=',')
X_test=dataset[301:,1:-1]
Y_test=dataset[301:,-1]

json_file=open('../tmp/model.json','r')
json_loaded_model=json_file.read()
json_file.close()

try:
	

	#load the model from json file
	model = model_from_json(json_loaded_model)

	#load the weights into new model
	model.load_weights("../tmp/model.h5")
	print("Model loaded from disk")

	model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
	score=model.evaluate(X_test,Y_test)

	print("\n%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

except Exception as e:
	print(e)
gc.collect()
