#!/usr/bin/python3

import json 
from Model import Model 

class PredictGrades:
  trainingData = [] 
  finTrainingData = [] 
  model = Model()
  model.init(3, 1, 1, 4)

  # parse json training data
  for line in open("trainingData.json", "r"):
    trainingData.append(json.loads(line))

  for t in range(0, len(trainingData)):
    train = [
      [trainingData[t]["timeStudied"]],
      [trainingData[t]["timeSlept"]],
      [trainingData[t]["classLevel"]]
    ]
    
    finTrainingData.append(train)
  print(str(finTrainingData))
