package main

import (
	"fmt"
	// "math"
	// "sort"
)

// func main(){
// 	var N int
// 	count := 0
// 	prev := math.MaxInt64
// 	fmt.Scan(&N)
// 	D := make([]int, N)
// 	for i:=0;i<N;i++ {
// 		fmt.Scan(&D[i])
// 	}
// 	sort.Ints(D)
// 	for i:=N-1;i>=0;i-- {
// 		if D[i] < prev {
// 			count++
// 			prev = D[i]
// 		}
// 	}
// 	fmt.Println("Answer is ", count)
// }
func main(){
	var N,value int
	fmt.Scan(&N)
	D := make(map[int]int, N)
	for i:=0;i<N;i++ {
		fmt.Scan(&value)
		D[value] = 1
	}
	fmt.Println("Answer is ", len(D))
}