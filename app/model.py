# -*- coding: UTF-8 -*-
import pickle
import gzip
import xgboost

# 載入Model
with gzip.open('app/model/xgboost-iris.pgz', 'r') as f:
    xgboostModel = pickle.load(f)


def predict(input):
    pred=xgboostModel.predict(input)[0]
    print(pred)
    return pred