package main

import(
	"fmt"
	"sort"
)

func main(){
	var n int
	drawer := true
	result := 0
	fmt.Scan(&n)
	cards := make([]int,n)
	for i:=0;i<n;i++ {
		fmt.Scan(&cards[i])
	}
	sort.Ints(cards)
	for i:=n-1;i>=0;i-- {
		fmt.Println("result:", result)
		if drawer {
			result += cards[i]
		}else {
			result -= cards[i]
		}
		drawer = !drawer
	}
	fmt.Println("Answer is ",result)
}