# -*- coding: UTF-8 -*-
# import app.model as model
import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    input_array = np.array([[5.5, 2.4, 2.7, 1.]])
    result = np.sum(input_array)
    response = app.response_class(
        response=jsonify({'result': str(result)}),
        status=200,
        mimetype='application/json'
    )
    return [response]  # 返回可迭代對象

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1 = insertValues['sepalLengthCm']
    x2 = insertValues['sepalWidthCm']
    x3 = insertValues['petalLengthCm']
    x4 = insertValues['petalWidthCm']
    input_array = np.array([[x1, x2, x3, x4]])
    # 進行預測
    result = np.sum(input_array)
    response = app.response_class(
        response=jsonify({'result': str(result)}),
        status=200,
        mimetype='application/json'
    )
    return [response]  # 返回可迭代對象
