package main

import (
	"fmt"
)

const N int = 4
const N2 int = 16
const LIMIT int = 100
var dx [4]int = [4]int {0, -1, 0, 1}
var dy [4]int = [4]int {1, 0, -1, 0}
var dir [4]string = [4]string {"r", "u", "l", "d"}
var MDT [N2][N2]int

type Puzzle struct {
	f [N2]int
	space int
	MD int
}
var state Puzzle
var limit int
var path [LIMIT]int

func getAllMD(pz Puzzle) int {
	var sum int = 0
	for i:=0; i < N2; i++ {
		if pz.f[i] == N2 {
			continue
		}
		sum += MDT[i][pz.f[i] - 1]
	}
	return sum
}

func isSolved() bool {
	for i:=0; i < N2; i++ {
		if state.f[i] != i + 1 {
			return false
		}
	}
	return true
}

func dfs(depth int, prev int) bool {
	if state.MD == 0 {
		return true
	}
	if depth + state.MD > limit {
		return false
	}
	var sx int = state.space / N
	var sy int = state.space % N
	var tmp Puzzle
	for r:=0; r < 4; r++ {
		var tx int = sx + dx[r]
		var ty int = sy + dy[r]
		if tx < 0 || ty < 0 || tx >= N || ty >= N {
			continue
		}
		// if originalMax(prev, r) - originalMin(prev, r) == 2 {
		// 	continue
		// }
		if abs(prev-r) == 2 {
			continue
		}
		tmp = state
		state.MD -= MDT[tx * N + ty][state.f[tx * N + ty] - 1]
		state.MD += MDT[sx * N + sy][state.f[tx * N + ty] - 1]
		swap(&state.f[tx * N + ty], &state.f[sx * N + sy])
		state.space = tx * N + ty
		if dfs(depth + 1, r) {
			path[depth] = r
			return true
		}
		state = tmp
	}
	return false
}

func swap(right *int, left *int) {
	var tmp int = *right
	*right = *left
	*left = tmp
}

func originalMin(value1 int, value2 int) int {
	if value1 < value2 {
		return value1
	}else{
		return value2
	}
}

func originalMax(value1 int, value2 int) int {
	if value1 > value2 {
		return value1
	}else {
		return value2
	}
}

func abs(value int) int {
	if value >= 0 {
		return value
	}else {
		return -value
	}
}

func iterative_deepening(in Puzzle) string {
	in.MD = getAllMD(in)

	for limit = in.MD; limit <= LIMIT; limit++ {
		state = in
		if dfs(0, -100) {
			var ans string = ""
			for i := 0; i < limit; i++ {
				ans += dir[path[i]]
			}
			return ans
		}
	}
	return "unsolvable"
}
func main() {
	for i:=0; i < N2; i++ {
		for j:=0; j < N2; j++ {
			MDT[i][j] = abs(i / N - j / N) + abs(i % N - j % N)
		}
	}
	var in Puzzle
	for i:=0; i < N2; i++ {
		fmt.Scan(&in.f[i])
		if in.f[i] == 0 {
			in.f[i] = N2
			in.space = i
		}
	}
	var ans string = iterative_deepening(in)
	fmt.Println(len(ans))
}