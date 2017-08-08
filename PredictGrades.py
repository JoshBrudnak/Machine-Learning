#!/usr/bin/python3

import numpy as np
import json 
from random import random

class PredictGrades:
  def getWeights(num):
    weights = []

    for i in range(0, num):
      weights.append(random())
    
    return weights

  def sigmoid(x):
    return 1 / (1 + np.exp(-x))

  trainingData = [] 
  weight = [] 
  layers = 1
  features = 3
  layerNodes = 4
  
  # parse json training data
  for line in open("trainingData.json", "r"):
    trainingData.append(json.loads(line))

  for t in range(0, len(trainingData)):
    # get initial weights
    for i in range(0, layerNodes):
      weight.append(getWeights(features))

    if layers > 1:
      for i in range(0, layers):
        for j in range(0, layerNodes):
          weight.append(getWeights(4))
    for i in range(0, layerNodes):
      weight.append(getWeights(4))

    nodeResults = []
    for j in range(0, layerNodes):
      w = np.matrix([weight[j][0], weight[j][1], weight[j][2]])
      f = np.matrix([
        [trainingData[t]["timeStudied"]],
        [trainingData[t]["timeSlept"]], 
        [trainingData[t]["classLevel"]]
        ]
      )
      result = w * f
      finValue = sigmoid(result)      
      nodeResults.append(finValue.item(0))

    if layers > 1:
      for i in range(0, layers):
        w = np.matrix([weight[j][0], weight[j][1], weight[j][2], weight[j][3]])
        f = np.matrix(
          [nodeResults[len(nodeResults) - 4]],
          [nodeResults[len(nodeResults) - 3]],
          [nodeResults[len(nodeResults) - 2]],
          [nodeResults[len(nodeResults) - 1]]
        )
        result = w * f
        finValue = sigmoid(result)
        nodeResults.append(finValue.item(0))

    index = len(weight) - 1
    w = np.matrix([weight[index][0], weight[index][1], weight[index][2], weight[index][3]])
    f = np.matrix([
      [nodeResults[len(nodeResults) - 4]],
      [nodeResults[len(nodeResults) - 3]],
      [nodeResults[len(nodeResults) - 2]],
      [nodeResults[len(nodeResults) - 1]]
      ]
    )
    result = w * f
    finValue = sigmoid(result)
    finalGrade = finValue.item(0)

    print("Time Studied " + str(trainingData[t]["timeStudied"]))
    print("Time Slept " + str(trainingData[t]["timeSlept"]))
    print("Class Level " + str(trainingData[t]["classLevel"]))
    print("Grade " + str(finalGrade))
