import numpy as np
import pandas as pd
from sklearn import preprocessing as pre
train=pd.read_csv('kidney_disease.csv');
#train.dropna(inplace=True);
#print(train.info());
'''Mapper functions that maps the train attributes 
from categorical to classfication'''

train['classification']=train['classification'].map({'notckd':0,'ckd':1})
train['classification']=train['classification']
no_yes_mapper={'no':0,'yes':1}
present_mapper={'notpresent':0,'present':1}
normal_mapper={'normal':1,'abnormal':0}
appet_mapper={'poor':0,'good':1}

'''Mapper implemetation on attributes'''

train['htn']=train['htn'].map(no_yes_mapper)
train['dm']=train['dm'].map(no_yes_mapper)
train['cad']=train['cad'].map(no_yes_mapper)
train['pe']=train['pe'].map(no_yes_mapper)
train['ane']=train['ane'].map(no_yes_mapper)
train['rbc']=train['rbc'].map(normal_mapper)
train['pc']=train['pc'].map(normal_mapper)
train['pcc']=train['pcc'].map(present_mapper)
train['ba']=train['ba'].map(present_mapper)
train['appet']=train['appet'].map(appet_mapper)

'''Individual attributes operations'''
#AGE
train['age']=train['age'].fillna(train['age'].median())
train['age']=pre.scale(train['age'])


#BP
train['bp']=train['bp'].fillna(train['bp'].median())
#Ok with this data

#SG
#print (train[['sg', 'classification']].groupby(['sg'], as_index=False).mean())
train['sg']=train['sg'].fillna('1.020')

#al
train['al']=train['al'].fillna(train['al'].median())

#su
train['su']=train['su'].fillna(train['su'].median())

#rbc
train['rbc']=train['rbc'].fillna(1.0)
#print (train[['rbc', 'classification']].groupby(['rbc'], as_index=False).mean())


#pc
train['pc']=train['pc'].fillna(1)

#pcc
train['pcc']=train['pcc'].fillna(0.0)
#print (train[['pcc', 'classification']].groupby(['pcc'], as_index=False).mean())

#ba
train['ba']=train['ba'].fillna(0)

#bgr
train['bgr']=train['bgr'].fillna(train['bgr'].median())
train['bgr']=pre.scale(train['bgr'])

#bu
train['bu']=train['bu'].fillna(train['bu'].mean())
train['bu']=pre.scale(train['bu'])

#sc
train['sc']=train['sc'].fillna(train['sc'].mean())
train['sc']=pre.scale(train['sc'])

#sod
train['sod']=train['sod'].fillna(train['sod'].mean())
train['sod']=pre.scale(train['sod'])

#pot
train['pot']=train['pot'].fillna(train['pot'].mean())
train['pot']=pre.scale(train['pot'])

#hemo
train['hemo']=train['hemo'].fillna(train['hemo'].mean())
train['hemo']=pre.scale(train['hemo'])

#pcv
train['pcv']=train['pcv'].fillna(train['pcv'].mean())
train['pcv']=pre.scale(train['pcv'])

#wc
train['wc']=train['wc'].fillna(train['wc'].median())
train['wc']=pre.scale(train['wc'])

#rc
train['rc']=train['rc'].fillna(train['rc'].mean())
train['rc']=pre.scale(train['rc'])

#Fill remaining

train['htn']=train['htn'].fillna(1)
train['dm']=train['dm'].fillna(1)
train['cad']=train['cad'].fillna(1)
train['appet']=train['appet'].fillna(1)
train['ane']=train['ane'].fillna(1)

pre_train=train.loc[:,'age':'classification']

pre_train.to_csv('preprocessed_train.csv');

'''Helper print functions'''

#print(train[['age','classification']].groupby(['age'],as_index=False).mean())
print(train.info())
