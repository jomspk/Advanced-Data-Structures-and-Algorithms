package main

import (
	"container/heap"
	"fmt"
)

const N int = 4
const N2 int = 16

var dx = [4]int{0, -1, 0, 1}
var dy = [4]int{1, 0, -1, 0}
var dir = [4]string{"r", "u", "l", "d"}
var MDT [N2][N2]int

type Puzzle struct {
	f     [N2]int
	space int
	MD    int
	cost  int
}

type State struct {
	puzzle    Puzzle
	estimated int
}

type StateHeap []State

func (h StateHeap) Len() int           { return len(h) }
func (h StateHeap) Less(i, j int) bool { return h[i].estimated < h[j].estimated }
func (h StateHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *StateHeap) Push(x interface{}) {
	*h = append(*h, x.(State))
}

func (h *StateHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func getAllMD(pz Puzzle) int {
	sum := 0
	for i := 0; i < N2; i++ {
		if pz.f[i] == N2 {
			continue
		}
		sum += MDT[i][pz.f[i]-1]
	}
	return sum
}

func astar(s Puzzle) int {
	PQ := &StateHeap{}
	heap.Init(PQ)
	s.MD = getAllMD(s)
	s.cost = 0
	V := make(map[Puzzle]bool)
	initial := State{
		puzzle:    s,
		estimated: getAllMD(s),
	}
	heap.Push(PQ, initial)

	for PQ.Len() > 0 {
		st := heap.Pop(PQ).(State)
		u := st.puzzle

		if u.MD == 0 {
			return u.cost
		}
		V[u] = true

		sx := u.space / N
		sy := u.space % N

		for r := 0; r < 4; r++ {
			tx := sx + dx[r]
			ty := sy + dy[r]
			if tx < 0 || ty < 0 || tx >= N || ty >= N {
				continue
			}
			v := u

			v.MD -= MDT[tx*N+ty][v.f[tx*N+ty]-1]
			v.MD += MDT[sx*N+sy][v.f[tx*N+ty]-1]

			swap(&v.f[sx*N+sy], &v.f[tx*N+ty])
			v.space = tx * N + ty
			if !V[v] {
				v.cost++
				newState := State{
					puzzle:    v,
					estimated: v.cost + v.MD,
				}
				heap.Push(PQ, newState)
			}
		}
	}
	return -1
}

func swap(a, b *int) {
	*a, *b = *b, *a
}

func abs(value int) int {
	if value >= 0 {
		return value
	}
	return -value
}

func main() {
	for i := 0; i < N2; i++ {
		for j := 0; j < N2; j++ {
			MDT[i][j] = abs(i/N-j/N) + abs(i%N-j%N)
		}
	}
	var in Puzzle
	for i := 0; i < N2; i++ {
		fmt.Scan(&in.f[i])
		if in.f[i] == 0 {
			in.f[i] = N2
			in.space = i
		}
	}
	fmt.Println(astar(in))
}