package main

import (
	"fmt"
	"sort"
	"strconv"
)

func findBridge(V int, graph *[][]int) {
	var prenum []int
	var low []int
	var parent []int
	var bridges [][2]int
	var time int = 0
	var prev int
	var now int
	var tmp [][2]int
	var results [][2]int
	for i:=0;i<V;i++ {
		prenum = append(prenum, -1)
		low = append(low, -1)
		parent = append(parent, -1)
	}
	for i:=0;i<V;i++ {
		if prenum[i] == -1 {
			dfs(i, graph, &prenum, &low, &time, &parent, &bridges)
		}
	}
	bridges = unique(bridges)

	sort.SliceStable(bridges, func(i, j int) bool {return bridges[i][0] < bridges[j][0]})
	prev = 0
	now = 0
	for _, point := range(bridges) {
		now = point[0]
		if prev != now {
			sort.SliceStable(tmp, func (i, j int) bool  {return tmp[i][1] < tmp[j][1]})
			results = append(results, tmp...)
			tmp = tmp[:0]	
			tmp = append(tmp, point)
		}else {
			tmp = append(tmp, point)
		}
		prev = now
	}
	sort.SliceStable(tmp, func (i, j int) bool  {return tmp[i][1] < tmp[j][1]})
	results = append(results, tmp...)

	for _, point := range(results) {
		fmt.Printf("%d %d\n", point[0], point[1])
	}
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
func unique(intSlice [][2]int) [][2]int {
	seen := make(map[string]bool)
	result := [][2]int{}

	for _, row := range(intSlice) {
		key1 := strconv.Itoa(row[0])
		key2 := strconv.Itoa(row[1])
		if !seen[key1+key2] && !seen[key2+key1] {
			seen[key1+key2] = true
			seen[key2+key1] = true
			result = append(result, row)
		}
	}
	return result
}
func dfs(vertex int, graph *[][]int, prenum *[]int, low *[]int,time *int, parent *[]int, bridges *[][2]int) {
	(*low)[vertex] = *time
	(*prenum)[vertex] = (*low)[vertex]
	(*time)++
	for _,node := range (*graph)[vertex] {
		if (*prenum)[node] == -1 {
			(*parent)[node] = vertex
			dfs(node, graph, prenum, low, time, parent, bridges)
			(*low)[vertex] = originalMin((*low)[vertex], (*low)[node])
			if (*low)[node] > (*prenum)[vertex] {
				(*bridges) = append((*bridges), [2]int{originalMin(vertex, node), originalMax(vertex, node)})
			}
		}else if node != (*parent)[vertex] {
			(*low)[vertex] = originalMin((*low)[vertex],(*prenum)[node])
		}
	}

}
func main() {
	var V, E int

	fmt.Scan(&V,&E)

	graph := make([][]int, V)
	for i:=0;i<E;i++ {
		var u, v int
		fmt.Scan(&u, &v)
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	findBridge(V, &graph)
}