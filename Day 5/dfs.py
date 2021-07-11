# DFS Approach

class Stack:
    def __init__(self) -> None:
        self.arr = []
    
    def push(self, val):
        self.arr.append(val)
    
    def pop(self):
        pop = self.arr.pop()
        return pop

    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False

adj_list = {
                "A" : ["B", "D"],
                "B" : ["A", "C"],
                "C" : ["B"],
                "D" : ["A", "F", "E"],
                "E" : ["D", "F", "G"],
                "F" : ["D", "H", "E"],
                "G" : ["E", "H"],
                "H" : ["F", "G"]
           }

stack = Stack()
visited = {}
dfs_traversal_output = []
parent = {}
level = {}

for Node in adj_list.keys():
    visited[Node] = False
    parent[Node] = None
    level[Node] = -1

src = "A"
visited[src] = True
level[src] = 0
stack.push(src)

while not stack.isEmpty():
    u = stack.pop()
    dfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u] + 1
            parent[v] = u
            stack.push(v)

print(dfs_traversal_output)