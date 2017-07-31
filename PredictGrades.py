#!/usr/bin/python3

#import numpy as np
import json 
from random import random

class PredictGrades:
  def getWeights(num):
    weights = []

    for i in range(0, num):
      weights.append(random())
    
    return weights

  trainingData = [] 
  weight = [] 
  layers = 1
  features = 3
  layerNodes = 4
  
  for line in open("trainingData", "r"):
    trainingData.append(json.loads(line))
  for i in range(0, layerNodes):
    weight.append(getWeights(features))
  if layers > 1:
    for i in range(0, layers):
      for j in range(0, layerNodes):
        weight.append(getWeights(4))
  for i in range(0, layerNodes):
    weight.append(getWeights(1))


  print(weight)
