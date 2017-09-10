package main

import "fmt"

func main() {
  trainingData := ReadCsv("mnist_train.csv")
  testingData := ReadCsv("mnist_test.csv")

  fmt.Println(trainingData[0].label)
  fmt.Println(trainingData[0].image)
  fmt.Println(testingData[0].label)
  fmt.Println(testingData[0].image)
  fmt.Println(len(trainingData))
}
