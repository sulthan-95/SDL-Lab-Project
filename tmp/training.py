import numpy
from keras.layers import Dense
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import InputLayer
numpy.random.seed(7)

#dataset=numpy.loadtxt("preprocessed_train.csv",delimiter=",",usecols=range)
dataset=numpy.genfromtxt('preprocessed_train.csv', delimiter=',')

X=dataset[1:295,1:-1]
Y=dataset[1:295,-1]

X_test=dataset[301:,1:-1]
Y_test=dataset[301:,-1]
#A sequential model is called
model=Sequential()

#An Input Layer that returns a tensor
model.add(Dense(12,input_dim=24,activation='relu'))

#A Dropout layer between each layer to avoid overfitting
model.add(Dropout(0.4))
model.add(Dense(6,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))

#Compile the model for the initial weights
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
print(model.summary())

#Fit the training data inside model
model.fit(X,Y,epochs=500,batch_size=50)

#Save the model in JSON format
json_model=model.to_json()
with open("model.json","w") as json_file:
	json_file.write(json_model)

#Save the weights of model in HDF5
model.save_weights("model.h5")

print("Model trained and saved to disk")

