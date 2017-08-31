#!/usr/bin/python3

import json 
from Model import Model 

class PredictGrades:
  data = [] 
  trainResults = []
  testResults = []
  trainingData = [] 
  testingData = [] 

  model = Model()
  model.init(3, 1, 1, 4)

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
    trainingData.append(train)

  model.trainModel(trainingData, testingData, trainResults, testResults)
