# BFS Approach

class Queue:
    def __init__(self) -> None:
        self.arr = []
    
    def enQueue(self, val):
        self.arr.append(val)
    
    def deQueue(self):
        pop = self.arr[0]
        self.arr.remove(self.arr[0])
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
                "D" : ["A", "E", "F"],
                "E" : ["D", "F", "G"],
                "F" : ["D", "H", "E"],
                "G" : ["E", "H"],
                "H" : ["F", "G"]
           }

visited = {}
level = {}
parent = {} 
bfs_traversal_output = []
queue = Queue()

for Node in adj_list.keys():
    visited[Node] = False
    level[Node] = -1
    parent[Node] = None

src = "A"
visited[src] = True
level[src] = 0
queue.enQueue(src)

while not queue.isEmpty():
    u = queue.deQueue()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u] + 1
            parent[v] = u
            queue.enQueue(v)
print(parent)