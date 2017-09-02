#!/usr/bin/python3

import numpy as np
import math

class BackPropagation: 
  weights = []

  def sigmoidPrime(self, x):
    exp = math.e ** x
    return exp / (exp + 1)**2

  def computeNewWeights(self, loss, layerWeights, dependentWeights, inputs, result):
    gradients = []
    inputProd = 1
    for i in range(0, len(inputs)):
      inputProd *= inputs[i]

    for i in range(0, len(layerWeights)):
      parDer = 1
      if(len(dependentWeights) > 0):
        for j in range(0, len(dependentWeights)): 
          weightSum = 0
          if type(dependentWeights[j]) is float:
            weightSum += dependentWeights[j]
          else:
            for k in range(0, len(dependentWeights[j])):
              weightSum += dependentWeights[j][k]
         
          parDer = parDer * self.sigmoidPrime(weightSum * result)

      gradients.append(loss * parDer * inputProd)
   
    return gradients

  def trainModel(self, model, trainingData, testingData, trainResults, testResults):
    yhat = []
    loss = [] 
    testLoss = 1
    gamma = 1 
    self.weights = model.weights

    while abs(testLoss) > 0.001:
      totalLoss = []
      
      # initialize total loss array
      for i in range(0, len(self.weights)):
        weightLen = []
        for j in range(0, len(self.weights[i])):
          weightLen.append(0)
        totalLoss.append(weightLen)
          
      # get the sum of the loss with respect to each weight
      for i in range(0, len(trainingData)):
        yhat.append(model.getResult(trainingData[i]))
        loss.append(yhat[i] - trainResults[i])
    
        gradients = []
        weightNum = 0
        for j in range(0, model.layers):
          weightNum += 1
          for k in range(0, model.layerNodes):
            gradients.append(self.computeNewWeights(loss[i], self.weights[j], [], trainingData[i], trainResults[i]))
      
        for j in range(0, 4):
          gradients.append(self.computeNewWeights(loss[i], self.weights[weightNum + j], self.weights[j], trainingData[i], trainResults[i]))

        # add loss to total loss
        for i in range(0, len(totalLoss)):
          for j in range(0, len(totalLoss[i])):
            totalLoss[i][j] += gradients[i][j] 
      

      # update the weights 
      for i in range(0, len(totalLoss)):
        for j in range(0, len(totalLoss[i])):
          self.weights[i][j] -= gamma * totalLoss[i][j]

      testLoss = 0
      for i in range(0, len(testingData)):
        testEstimate = model.getResult(testingData[i])
        testLoss += testEstimate - testResults[i]
    return self.weights
