from collections import deque 
 
class Graph: 
     
    graph = {} 
 
    def add_edge(self, u, v): 
        if u not in self.graph: 
            self.graph[u] = [] 
        if v not in self.graph: 
            self.graph[v] = [] 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
 
    def dfs(self, start,target,visited=None): 
        if visited is None:
            visited = set() 
        visited.add(start) 
        if start==target: 
            return True 
        print(start, end=" ") 
        for i in self.graph[start]:
            if i not in visited: 
                if self.dfs(i,target, visited): 
                    return True 
        return False 
 
    def bfs(self, start,target): 
        visited = set() 
        queue = deque([start]) 
        visited.add(start) 
 
        while queue: 
            vertex = queue.popleft() 
            print(vertex, end=" ") 
            if(vertex==target): 
                break 
            for i in self.graph[vertex]: 
                print("vk",i)
                if i not in visited: 
                    visited.add(i) 
                    queue.append(i) 
 
gr = Graph() 
 
root = input("Enter the root node: ") 
gr.graph[root] = []   
 
num_nodes = int(input("Enter the total number of nodes (including the root): ")) 
 
print("Now, enter each node and its child nodes:") 
 
for _ in range(num_nodes - 1):   
    node = input("Enter a node: ") 
    ans = 'y' 
    while ans == 'y': 
        print("child node present or not(y or n):") 
        ans = input() 
        if ans=='n': 
            break 
        child = input(f"Enter child node for {node}: ") 
        gr.add_edge(node, child) 
         
 
print("\nGraph (Adjacency List):") 
print(gr.graph) 
 
target=input("\nEnter a Node where to travese:") 
 
start_node = input("\nEnter the star ng node for traversal: ") 
 
print("DFS:") 
gr.dfs(start_node,target) 
 
print("\nBFS:") 
gr.bfs(start_node,target) 