#!/usr/bin/python3

import numpy as np
from random import random

class Model: 
  layers = 1
  inputNum = 1 
  outputNum = 1
  layerNodes = 1
  weights = []
  
  def init(self, inputs, out, lay, nodes):
    inputNum = inputs 
    outputNum = out 
    layers = lay 
    layerNodes = nodes 
    self.setInitialWeights()

  def getRanWeights(self, num):
    weight = []

    for i in range(0, num):
      weight.append(random())
    
    return weight

  def sigmoid(x):
    return 1 / (1 + np.exp(-x))

  def getError(data, train):
    loss = [] 
    for i in range(0, len(data)):
      error = (train[i]["grade"] - data[i]) ** 2
      loss.append(error / 2)
    
    return loss 

  def setInitialWeights(self):
    if self.layers >= 1:
      for i in range(0, self.layerNodes):
        self.weights.append(self.getRanWeights(self.inputNum))
      for i in range(1, self.layers):
        for j in range(0, self.layerNodes):
          self.weights.append(self.getRanWeights(self.layerNodes))
      for i in range(1, self.layerNodes):
        self.weights.append(self.getRanWeights(self.outputNum))

  def getResult(inputs):
    nodeResults = []

    for j in range(0, layerNodes):
      w = np.matrix([weights[j][0], weights[j][1], weights[j][2]])
      result = w * inputs 
      finValue = sigmoid(result)      
      nodeResults.append(finValue.item(0))

    if layers > 1:
      for i in range(0, layers):
        w = np.matrix([weight[j][0], weight[j][1], weight[j][2], weight[j][3]])
        f = np.matrix(
          [nodeResults[len(nodeResults) - layerNodes]],
          [nodeResults[len(nodeResults) - (layerNodes - 1)]],
          [nodeResults[len(nodeResults) - (layerNodes - 2)]],
          [nodeResults[len(nodeResults) - (layerNodes - 3)]]
        )
        result = w * f
        finValue = sigmoid(result)
        nodeResults.append(finValue.item(0))

    index = len(weight) - 1
    w = np.matrix([weight[index][0], weight[index][1], weight[index][2], weight[index][3]])
    f = np.matrix([
      [nodeResults[len(nodeResults) - layerNodes]],
      [nodeResults[len(nodeResults) - (layerNodes - 1)]],
      [nodeResults[len(nodeResults) - (layerNodes - 2)]],
      [nodeResults[len(nodeResults) - (layerNodes - 3)]]
      ]
    )
    result = w * f
    finValue = sigmoid(result)
    finalGrade = finValue.item(0)
   
    return finalGrade

  def trainModel(trainingData):
    yhat = []
    for i in range(0, len(trainingData)):
      yhat.append(getResult(trainingData[i]))
    loss = getError(yhat, trainingData)
