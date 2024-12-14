package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputFile, err := os.Open("./input.txt")
	result := 0

	if err != nil {
		log.Fatal(err)
	}
	defer inputFile.Close()

	scanner := bufio.NewScanner(inputFile)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
		line := scanner.Text()
		if safeLine(line) == true {
			result++
		}
	}

	println(result)

}

func safeLine(line string) bool {
	vals := strings.Split(line, " ")
	safe := true

	num1, err1 := strconv.Atoi(vals[0])
	num2, err2 := strconv.Atoi(vals[1])

	if err1 != nil || err2 != nil {
		log.Fatal("Error atoi")
	}

	ascending := num1 < num2

	for i := 0; i < len(vals)-1 && safe == true; i++ {
		num1, err1 := strconv.Atoi(vals[i])
		num2, err2 := strconv.Atoi(vals[i+1])

		if err1 != nil || err2 != nil {
			log.Fatal("Error atoi")
		}

		if (num1 > num2 && ascending == true) || (num1 < num2 && ascending == false) || (num1-num2 > 3 || num1-num2 < -3) || num1 == num2 {
			safe = false
		}

	}

	return safe
}
