package main

import "fmt"

func main() {
  trainingData := ReadCsv("mnist_train.csv")
  testingData := ReadCsv("mnist_test.csv")

  initializeModel(2, 1, 2, 10, 2, 10)
  trainModel(trainingData, testingData)
}
