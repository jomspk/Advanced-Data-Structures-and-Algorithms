package main

import (
	"fmt"
)

func main(){
	var N,Y int
	fmt.Scan(&N, &Y)
	for i:=0;i<=N;i++ {
		for y:=0;y<=N-i;y++ {
			k := N-i-y
			if 10000*i+5000*y+1000*k == Y {
				fmt.Println("10000円が",i,"枚,","5000円が",y,"枚,","1000円が",k,"枚")
				return
			}
		}
	}
	fmt.Println("-1 -1 -1")
}