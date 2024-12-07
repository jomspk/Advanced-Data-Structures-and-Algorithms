package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	// count := 0
	// for _, char := range s {
	// 	if char == '1' {
	// 		count++
	// 	}
	// 	fmt.Printf("%c\n", char)
	// }
	// fmt.Println("1の合計",count)
	fmt.Println("1の合計:",strings.Count(s, "1"),"個")
}