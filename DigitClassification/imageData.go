package main

import (
  "bufio"
  "fmt"
  "os"
  "strings"
  "math"
  "strconv"
)

type ImageData struct {
  label int
  image [][]int
}

func getData(data []string, parsedData chan []ImageData) {
  var result []ImageData

  for _,row := range data {
    var intRow []int
    rowParts := strings.Split(row, ",")

    for i := range rowParts {
      intPart,_ := strconv.Atoi(rowParts[i])
      intRow = append(intRow, intPart)
    }

    var image [][]int
    label := intRow[0]

    imageSize := int(math.Sqrt(float64(len(intRow) - 1)))
    for j := 1; j < imageSize; j++ {
      image = append(image, intRow[((j * imageSize) - imageSize) + 1 : j * imageSize])
    }

    dataMember := ImageData{label, image}
    result = append(result, dataMember)
  }

  parsedData <- result
}

func ReadCsv(fileName string) []ImageData {
    var rawData []string
    var data []ImageData
    threads := 200
    finData := make([]chan []ImageData, threads + 1)
    for i := range finData {
      finData[i] = make(chan []ImageData)
    }

    file,_ := os.Open(fileName)
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
      rawData = append(rawData, string(scanner.Bytes()))
    }

    dataPerThread := (int)(len(rawData) / threads)
    //remainder := len(rawData) % threads

    for i := 0; i <= threads; i++ {
      start := int((dataPerThread * (i + 1)) - dataPerThread)
      end := int((dataPerThread * (i + 1)) - 1)
      threadData := rawData[start : end]

      go getData(threadData, finData[i])
    }

    for i := range finData {
      threadData := <-finData[i]
      for j := range threadData {
        data = append(data, threadData[j])
      }
    }
    fmt.Println("done")
    return data
}
