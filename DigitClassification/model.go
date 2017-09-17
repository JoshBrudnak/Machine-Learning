package main

import {
  "fmt"
  "math"
}

var convolutionLayers int
var fullyConLayers int
var layerNodes []int
var filterSize int
var outputs int
var imageFilters [][][][]int

func initializeModel(cLayerNum int, flayerNum int, layerDepth []int, filtSize int, outputNum int) {
  convolutionLayers = clayerNum
  fullyConLayers = flayerNum
  layerNodes = layerDepth
  filterSize = filtSize
  outputs = outputNum
  setInitialFilters()
}

func getRanFilters(number int, size int) [][][]int {
  var filters [][][]int
  random := math.Rand

  for i := 0; i < number; i++ {
    for j := 0; j < size; j++ {
      for k := 0; k < size; k++ {
        filters[i][j][k] = append(filt, random.Float64)
      }
    }
  }

  return filters
}

func setInitialFilters() {
  var filt [][][][]int
  for i := 0; i < layers; i++ {
    filt = append(filt, getRanFilters(layerNodes[i], filterSize))
  }

  imageFilters = filt
}

func sigmoid(x int) float64 {
  return 1 / (1 + math.E ^ float64(-x))
}

func dotProduct(fMatrix [][]int, sMatrix [][]int) int {
  dotProd := 0
  if len(fMatrix) != len(sMatrix) {
    return 0
  }

  for i := range fMatrix {
    for j := range fMatrix[i] {
      dotProd += fMatrix[i][j] * sMatrix[i][j]
    }
  }

  return dotProd
}

func classifyImage(image [][]int) []float64 {

}

func trainModel(trainingData []ImageData, testData []ImageData) {
  var yhat [][]float64

  for _,data := range trainingData {
    yhat = append(yhat, classifyImage(data.image))
  }

}
