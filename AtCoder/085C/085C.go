package main

import (
	"fmt"
)

func main(){
	var N,Y int
	count := 0
	fmt.Scan(&N, &Y)
	for i:=0;i<=N;i++ {
		for y:=0;y<=N-i;y++ {
			k := N-i-y
			if 10000*i+5000*y+1000*k == Y {
				count++
			}
		}
	}
	if count == 0 {
		fmt.Println("Answer is ", -1-1-1)
	}else {
		fmt.Println("Answer is ", count)
	}
}