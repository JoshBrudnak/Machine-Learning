#!/usr/bin/python3

import numpy as np
import math
from random import random

class GeneticAlgorithym:
  def getLoss(self, estimate, answer):
    error = (answer - estimate) ** 2
    error = error / 2
    
    return error 
  
  def sigmoidPrime(self, x):
    exp = math.e ** x
    return exp / (exp + 1)**2
  
  def getGenome(self, weights):
    finWeight = []
    for i in range(0, len(weights)):
      for j in range(0, len(weights[i])):
        finWeight.append(weights[i][j])

    return finWeight

  #def computeNewWeights(self, loss, layerWeights, dependentWeights, inputs, result):

  def trainModel(self, model, trainingData, testingData, trainResults, testResults):
    populationSize = 50
    genome = self.getGenome(model.weights)
    minError = 1
    population = []
    for i in range(0, populationSize): 
      population.append(genome)
   
    while minError > 0.001:
      sign = 1.0
      newPopulation = []
      for i in range(0, len(population)): 
        mutGenome = []
        for j in range(0, len(population[i])): 
          mutGenome.append(population[i][j] + ((sign * random()) - 0.1))
          sign *= 1.0
        newPopulation.append(mutGenome)
      population = newPopulation

      populationLoss = []
      for i in range(0, len(population)): 
        totalLoss = 0
        model.convertNewWeights(population[i])
        for j in range(0, len(trainingData)):
          yhat = model.getResult(trainingData[j])
          totalLoss += self.getLoss(yhat, trainResults[j])  
        populationLoss.append(totalLoss)
 
      nextGen = []
      nextGenIndex = []
      for i in range(0, 10):
        index = 0
        lowest = 1.0
        for j in range(0, len(populationLoss)): 
          found = False
          if populationLoss[j] < lowest:
            for k in range(0, len(nextGen)): 
              if(nextGen[k] == populationLoss[j]):
                found = True 
            if found == False:
              lowest = populationLoss[j]
              index = j

        nextGen.append(population[index])
        nextGenIndex.append(index)
        lowest = 1
        index = 0

      minError = populationLoss[nextGenIndex[0]] 
      print(minError)
      population = []
      for i in range(0, 5):
        nextAverage = []
        for j in range(0, len(nextGen[i])):
          nextAverage.append((nextGen[i][j] + nextGen[9 - i][j]) / 2)
        population.append(nextAverage)
     
      for i in range(0, 10):
        alt = []
        for j in range(0, len(nextGen[i])):
          if(i % 2 == 0):
            alt.append(nextGen[i][j])
          else:
            alt.append(nextGen[9 - i][j])

      for i in range(0, populationSize - 20):
        ran = []
        for j in range(0, len(nextGen[0])):
          ran.append(random())
        population.append(ran)

      #print(nextGen)
