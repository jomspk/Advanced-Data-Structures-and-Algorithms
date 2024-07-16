package main

import (
	"fmt"
	"sort"
)

func findArticulationPoint(V int, graph *[][]int) {
	var prenum []int
	var low []int
	var parent []int
	var articulation_points []int
	var time int = 0
	for i:=0;i<V;i++ {
		prenum = append(prenum, -1)
		low = append(low, -1)
		parent = append(parent, -1)
	}
	for i:=0;i<V;i++ {
		if prenum[i] == -1 {
			dfs(i, graph, &prenum, &low, &time, &parent, &articulation_points)
		}
	}
	sort.SliceStable(articulation_points, func(i, j int) bool {return articulation_points[i] < articulation_points[j]})
	articulation_points = unique(articulation_points)
	for _, point := range(articulation_points) {
		fmt.Println(point)
	}
}
func originalMin(value1 int, value2 int) int {
	if value1 < value2 {
		return value1
	}else{
		return value2
	}
}
func unique(intSlice []int) []int {
	keys := make(map[int]bool)
	list := []int{}

	for _, entry := range(intSlice) {
		_, value := keys[entry]
		if !value {
			keys[entry] = true
			list = append(list, entry)
		}
	}
	return list
}
func dfs(vertex int, graph *[][]int, prenum *[]int, low *[]int,time *int, parent *[]int, articulation_points *[]int) {
	var children int = 0
	(*low)[vertex] = *time
	(*prenum)[vertex] = (*low)[vertex]
	(*time)++
	for _,node := range (*graph)[vertex] {
		if (*prenum)[node] == -1 {
			(*parent)[node] = vertex
			children++
			dfs(node, graph, prenum, low, time, parent, articulation_points)
			(*low)[vertex] = originalMin((*low)[vertex], (*low)[node])
			if (*parent)[vertex] == -1 && children > 1 {
				(*articulation_points) = append((*articulation_points), vertex)
			}else if (*parent)[vertex] != -1 && (*low)[node] >= (*prenum)[vertex] {
				(*articulation_points) = append((*articulation_points), vertex)
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
	findArticulationPoint(V, &graph)
}