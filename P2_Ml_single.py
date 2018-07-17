import requests
import os
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
class ml_single(object) :
    cls = None
    __instance = None
    def __init__(self):
        self.get()
    @staticmethod
    def singleton():
        if ml_single.__instance:
            return ml_single.__instance
        else:
            ml_single.__instance = ml_single()
            return ml_single.__instance  
    def get(self):
        #获取数据的保存路径
        PATH = "d:\\vscodeproject\\test\\program2\\"
        #通过request获取数据
        r = requests.get("http://www.ml.com//program2//iris.data")
        with open(PATH+'iris.data','w') as f:
            f.write(r.text)
        #读取iris.data中的数据  
        df = pd.read_csv(PATH+'iris.data',names=['speal length','speal width','petal length','petal width','class'])
        df['class'] = df['class'].map({'Iris-setosa':'SET','Iris-versicolor':'VIR','Iris-virginica':'VER'})#对类名进行修改
        df['width petal'] = df['petal width'].apply(lambda v:1 if v>1.3 else 0)
        #建模 对前50条数据进行学习
        clf = RandomForestClassifier(max_depth=5, n_estimators=10)
        X = df.ix[:,:4] 
        y = df.ix[:,4]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
        self.cls = clf.fit(X_train,y_train)
    def getpredict(self,test):
        return  self.cls.predict(test)[0]

 


		