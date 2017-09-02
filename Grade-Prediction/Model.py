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

  def setInitialWeights(self):
    initWeight = []
    if self.layers >= 1:
      for i in range(0, self.layerNodes):
        initWeight.append(self.getRanWeights(self.inputNum))
      for i in range(1, self.layers):
        for j in range(0, self.layerNodes):
          initWeight.append(self.getRanWeights(self.layerNodes))
      for i in range(0, self.layerNodes):
        initWeight.append(self.getRanWeights(self.outputNum))
    self.weights = initWeight

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
