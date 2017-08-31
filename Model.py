#!/usr/bin/python3

import numpy as np
import math
from random import random

class Model: 
  layers = 1
  inputNum = 1 
  outputNum = 1
  layerNodes = 1
  weights = []
  resultsPerNode = []
  
  def init(self, inputs, out, lay, nodes):
    self.inputNum = inputs 
    self.outputNum = out 
    self.layers = lay 
    self.layerNodes = nodes 
    self.setInitialWeights()

  def getRanWeights(self, num):
    weight = []

    for i in range(0, num):
      weight.append(random())
    
    return weight

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def sigmoidPrime(self, x):
    exp = math.e ** x
    return exp / (exp + 1)**2

  def getLoss(self, data, answer):
    loss = [] 
    for i in range(0, len(data)):
      error = (answer[i] - data[i]) ** 2
      loss.append(error / 2)
    
    return loss 

  def getLossPrime(self, yhat, answer):
    loss = answer - yhat
    
    return loss 

  def setInitialWeights(self):
    initWeight = []
    if self.layers >= 1:
      for i in range(0, self.layerNodes):
        initWeight.append(self.getRanWeights(self.inputNum))
      for i in range(0, self.layers):
        for j in range(0, self.layerNodes):
          initWeight.append(self.getRanWeights(self.layerNodes))
      for i in range(1, self.layerNodes):
        initWeight.append(self.getRanWeights(self.outputNum))
    self.weights = initWeight
    print(self.weights)

  def getResult(self, inputs):
    nodeResults = []

    for j in range(0, self.layerNodes):
      w = np.matrix([[self.weights[j][0]], [self.weights[j][1]], [self.weights[j][2]]])
      result = w * inputs
      finValue = self.sigmoid(result)      
      nodeResults.append(finValue.item(0))

    if self.layers > 1:
      for i in range(0, self.layers):
        w = np.matrix([
          self.weights[j][0], 
          self.weights[j][1], 
          self.weights[j][2], 
          self.weights[j][3]
        ])
        f = np.matrix(
          [nodeResults[len(nodeResults) - self.layerNodes]],
          [nodeResults[len(nodeResults) - (self.layerNodes - 1)]],
          [nodeResults[len(nodeResults) - (self.layerNodes - 2)]],
          [nodeResults[len(nodeResults) - (self.layerNodes - 3)]]
        )
        result = w * f
        finValue = self.sigmoid(result)
        nodeResults.append(finValue.item(0))

    index = len(self.weights) - 1
    w = np.matrix([
      self.weights[index - 3][0],
      self.weights[index - 2][0], 
      self.weights[index - 1][0], 
      self.weights[index][0]
    ])
    f = np.matrix([
      [nodeResults[len(nodeResults) - self.layerNodes]],
      [nodeResults[len(nodeResults) - (self.layerNodes - 1)]],
      [nodeResults[len(nodeResults) - (self.layerNodes - 2)]],
      [nodeResults[len(nodeResults) - (self.layerNodes - 3)]]
      ]
    )
    result = w * f
    finValue = self.sigmoid(result)
    finalGrade = finValue.item(0)
    self.resultsPerNode.append(nodeResults)
   
    return finalGrade

  def computeNewWeights(loss, layerWeights, dependentWeights, inputs, results):
    for i in range(0, len(layerWeights)):
     parDer = 1
     gamma = 0.001
     if(len(dependentWeights) > 0):
       for j in range(0, len(dependentWeights)): 
         weightSum = 0
         for k in range(0, len(dependentWeights[j])):
           weightSum += dependentWeights[j][k]
         
         parDer = parDer * self.sigmoidPrime(weightSum * results[j])

     grad = loss * parDer * inputs
     gradients.append(layerWeights[i] - (gamma *grad))
    

  def trainModel(self, trainingData, testingData, results):
    yhat = []
    loss = 0
    testLoss = 1
    while testLoss > 0.00001:
      for i in range(0, len(trainingData)):
        yhat.append(self.getResult(trainingData[i]))
        loss.append(yhat[i] - results[i])
    
        gradients = []
        for j in range(0, layers):
          for k in range(0, layerNodes):
            gradients.append(self.computeNewWeights(weights[j]), [], trainingData[j], resultsPerNode[j])
      
        for j in range(0, 4):
          gradients.append(self.computeNewWeights(weights[j]), [], trainingData[j], resultsPerNode[j])

      testLoss = 0
      for i in range(0, len(testingData)):
        testEstimate = self.getResult(testingData[i]))
        loss += testEstimate - results[len(trainingData) + i - 1])

      self.resultsPerNode = []
      print(gradients)
