#!/usr/bin/python3

import numpy as np
import math
from random import random

class GeneticAlgorithym:
  def getLoss(self, estimate, answer):
    error = (answer - estimate) ** 2
    error = error / 2
    
    return error 
  
  def getGenome(self, weights):
    finWeight = []
    for i in range(0, len(weights)):
      for j in range(0, len(weights[i])):
        finWeight.append(weights[i][j] + (random()))

    return finWeight

  def mutateGenomes(self, population):
    mutPopulation = []
    gamma = 0.01 
    for i in range(0, len(population)): 
      mut = int(random() * 100)
      if mut == 75:
        mutGenome = []
        for j in range(0, len(population[i])): 
          mutGenome.append(population[i][j] - (random() * 0.1))
          gamma *= -1.0
      
        mutPopulation.append(mutGenome)
      else:
        mutPopulation.append(population[i])

    return mutPopulation

  def trainModel(self, model, trainingData, trainResults):
    populationSize = 50
    continueSize = 10
    minError = 1
    minGenome = []
    population = []

    for i in range(0, populationSize):
      population.append(self.getGenome(model.weights))

    while minError > 0.01:
      population = self.mutateGenomes(population) 

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
      for i in range(0, continueSize):
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
      minGenome = nextGen[0]
      print(minError)
      population = nextGen 
      for k in range(0, 4):
        for i in range(0, continueSize):
          nextGenome = []
          bits = []
          for j in range(0, continueSize):
            ran = random()
            if ran >= 0.5:
              nextGenome.append(nextGen[i][j])
            else:
              nextGenome.append(nextGen[len(nextGen) - 1 - i][j])
          population.append(nextGenome)
    return model.convertNewWeights(minGenome)
