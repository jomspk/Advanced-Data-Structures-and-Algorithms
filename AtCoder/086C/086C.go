package main

import (
	"fmt"
	"math"
)

func main(){
	var N int
	fmt.Scan(&N)
	coordinate := make([][2]int,N)
	t := make([]int, N)
	isSuccess := true
	for i:=0;i<N;i++ {
		fmt.Scan(&coordinate[i][0], &coordinate[i][1], &t[i])
		if i == 0 {
			continue
		}
		absX := math.Abs(float64(coordinate[i][0] - coordinate[i-1][0]))
		absY := math.Abs(float64(coordinate[i][1] - coordinate[i-1][1]))
		time := t[i] - t[i-1]
		if int(absX + absY) > time {
			isSuccess = false
		}
		if int(absX + absY) <= time {
			if (time - int(absX+absY)) % 2 != 0 {
				isSuccess = false
			}
		}
	}
	if isSuccess {
		fmt.Println("Make it!")
	}

}