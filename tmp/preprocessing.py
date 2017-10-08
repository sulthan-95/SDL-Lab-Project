import numpy as np
import pandas as pd
from sklearn import preprocessing as pre
train=pd.read_csv('kidney_disease.csv');
#train.dropna(inplace=True);
#print(train.info());
'''Mapper functions that maps the train attributes 
from categorical to classfication'''

train['classification']=train['classification'].map({'notckd':0,'ckd':1})
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


train['bp']=train['bp'].fillna(train['bp'].median())

'''Helper print functions'''

print(train[['age','classification']].groupby(['age'],as_index=False).mean())
print(train.info())
