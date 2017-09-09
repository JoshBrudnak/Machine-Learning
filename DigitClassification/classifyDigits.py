import numpy as np
import csv
import math 
from threading import Thread

class classifyDigits():

  def readCsv(fileName):
    data = []
    with open(fileName) as f:
      reader = csv.reader(f)

      for row in reader:
        intRow = []
        for i in range(0, len(row)):
          intRow.append(int(row[i]))

        label = intRow[0]
        image = []
        imageSize = int(math.sqrt(len(row) - 1))
        for i in range(1, imageSize):
          image.append(intRow[(i * imageSize) - imageSize : i * imageSize])
         
        dataMember = {"label": label, "image": image}
        data.append(dict(dataMember))

    return data
        
  trainingData = readCsv("mnist_train.csv")  
  testingData = readCsv("mnist_test.csv")  
