package main

import (
	"fmt"
)

func checkSum(value int) int {
	total := 0
	for i:=1;i<5;i++ {
		total += value%10
		value -= value%10
		if value == 0 {
			return total
		}
		value = value/10
	}
	return 0
}
// func checkSum(value int) int {
// 	if value == 0 {
// 		return 0
// 	}
// 	return value%10 + checkSum((value - value%10)/10)
// }
func main(){
	var a,b,n int
	answer := 0
	fmt.Scan(&a,&b,&n)
	for i:=1;i<=n;i++ {
		checkSumValue := checkSum(i)
		if a<=checkSumValue && checkSumValue<=b {
			answer+=i
		}
	}
	fmt.Println("answer is ", answer)
}

