// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"strconv"
// )

// func main(){
// 	var list []int
// 	scanner := bufio.NewScanner(os.Stdin)
// 	for i:=0;i<200;i++ {
// 		if !scanner.Scan() {
// 			break // 入力が終了した場合
// 		}
// 		text := scanner.Text()
// 		if text == "" {
// 			break
// 		}
// 		num, _ := strconv.Atoi(text)
// 		list = append(list, num)
// 	}
// 	fmt.Println(recursion(list))
// }

// func recursion(list []int) int {
// 	if len(list) == 0 {
// 		return 0
// 	}
// 	count := 0
// 	for i:=0;i<len(list);i++ {
// 		if(list[i]%2 == 1 || list[i] == 0) {
// 			list = append(list[:i], list[i+1:]...)
// 			continue
// 		}
// 		list[i] = list[i]/2
// 		count++
// 	}
// 	return count + recursion(list)
// }

package main

import (
	"fmt"
	"math"
)
func countCalcurate(value int) int {
	if value%2 == 1 {
		return 0
	}
	return 1 + countCalcurate(value/2)
}
func main(){
	var n, value, count int
	min := math.MaxInt64
	fmt.Scan(&n)
	for i:=0;i<n;i++ {
		fmt.Scan(&value)
		count = countCalcurate(value)
		if count < min {
			min = count
		}
	}
	fmt.Println("全体を2で割り切れる最高の回数は、",min)
}