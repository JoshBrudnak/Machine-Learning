#!/usr/bin/python3

import numpy as np
import math

class GeneticAlgorithym:
  weights = []

  def sigmoidPrime(self, x):
    exp = math.e ** x
    return exp / (exp + 1)**2

  def computeNewWeights(self, loss, layerWeights, dependentWeights, inputs, result):

  def trainModel(self, model, trainingData, testingData, trainResults, testResults):
