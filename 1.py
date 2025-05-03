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
 
    def dfs(self, start): 
        visited=set()
        stack=[start]

        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                print(node," ")
                
                for neighbour in reversed(self.graph[node]):
                    if neighbour not in  visited:
                        stack.append(neighbour)

 
    def bfs(self, start): 
        visited = set() 
        queue = deque([start]) 
        visited.add(start) 
 
        while queue: 
            vertex = queue.popleft() 
            print(vertex, end=" ") 
            for i in self.graph[vertex]: 
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
 
start_node = input("\nEnter the star ng node for traversal: ") 
 
print("DFS:") 
gr.dfs(start_node) 
 
print("\nBFS:") 
gr.bfs(start_node) 