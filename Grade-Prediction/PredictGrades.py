#!/usr/bin/python3

import json 
from Model import Model 
from BackPropagation import BackPropagation
from GeneticAlgorithym import GeneticAlgorithym 

class PredictGrades:
  data = [] 
  trainResults = []
  testResults = []
  trainingData = [] 
  testingData = [] 

  model = Model()
  model.init(3, 1, 1, 4)
  bpTraining = BackPropagation()
  genAlTraining = GeneticAlgorithym()

  # parse json training data
  for line in open("trainingData.json", "r"):
    data.append(json.loads(line))

  for i in range(0, len(data) - 4):
    train = [
      data[i]["timeStudied"],
      data[i]["timeSlept"],
      data[i]["classLevel"]
    ]

    trainResults.append(data[i]["grade"])
    trainingData.append(train)
    
  for i in range(len(data) - 4, len(data)):
    train = [
      data[i]["timeStudied"],
      data[i]["timeSlept"],
      data[i]["classLevel"]
    ]

    testResults.append(data[i]["grade"])
    testingData.append(train)

  #model.weights = bpTraining.trainModel(model, trainingData, testingData, trainResults, testResults)
  genAlTraining.trainModel(model, trainingData, testingData, trainResults, testResults)
  
  while True:
    print("How long did you study: ")
    studied = int(input()) * 0.01
    print("How long did you sleep: ")
    slept = int(input()) * 0.1
    print("Class level: ")
    classLevel = int(input()) * 0.001
     
    inputs = [studied, slept, classLevel]
    grade = model.getResult(inputs)
    grade = grade * 100
    print("Your grade will be: %.2f" % (grade))
