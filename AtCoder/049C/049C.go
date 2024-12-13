// package main

// import (
// 	"fmt"
// )

// func main(){
// 	var S string
// 	words := map[string]string{
// 		"eam": "dream",
// 		"ase": "erase",
// 		"mer": "dreamer",
// 		"ser": "eraser",
// 	}
// 	fmt.Scan(&S)
// 	for len(S)>3 {
// 		lastThreeWords := S[len(S)-3:]
// 		value, exists := words[lastThreeWords]
// 		if !exists {
// 			return
// 		}
// 		specificWord := S[len(S)-len(value):]
// 		if specificWord == value {
// 			S = S[:len(S)-len(value)]
// 		}else {
// 			return
// 		}
// 	}
// 	if len(S)==0 {
// 		fmt.Println("Success")
// 	}
// }
package main

import (
	"fmt"
	"strings"
)

func main(){
	var S string
	fmt.Scan(&S)
	S = strings.Replace(S, "dream", "A", -1)
	S = strings.Replace(S, "erase", "B", -1)
	S = strings.Replace(S, "Aer", "", -1)
	S = strings.Replace(S, "Br", "", -1)
	S = strings.Replace(S, "A", "", -1)
	S = strings.Replace(S, "B", "", -1)
	if S == "" {
		fmt.Println("Success")
	}
}