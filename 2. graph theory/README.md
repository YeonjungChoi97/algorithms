# Introduction to graph theory: 
### Depth First Search and Breadth First Search

---- 

#### from: https://www.youtube.com/watch?v=7C9RgOcvkvo

#### We must know... 
#### Stack

- First-In-Last-Out (FILO)
- if in a -> b -> c, then out c -> b -> a

```python
stack = []
stack.append("a") #O(1)
stack.append("b")
stack.append("c")
stack.append("d")

stack.pop() #O(1)

print(stack) #[a, b, c]

stack.append("e")
stack.append("f")
print(stack[::-1] #[f, e, c, b, a]
stack.pop()


print(stack) #[a, b, c, e]
```
#### Queue

- First-In-First-Out (FIFO)
- if in a -> b -> c, then out a -> b -> c

```python
from collections import deque 

#for less time complexity! 
#please please use deque library

queue = deque()

queue.append("a") #O(1)
queue.append("b")
queue.append("c")
queue.append("d")

print(queue) #[a, b, c, d]

queue.popleft() #O(1)

print(queue) #[b, c, d]
```

#### Recursive Function

- need to define a condition to stop the recursion
- else, the function wwill be infinitely called

```python
#factorial example

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
    
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n*(n-1)! to code
    return n* factorial_recurrsive (n-1)

```

- Euclidean algorithm
a method for computing the greatest common divisor of two integers
lets suppose...
A%B = R
GCD of A&B is GCD of B&R
we can write this into recursive function...

```python

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(a,b))
 
```
----
#### DFS (Depth-First Search)
DFS is a search algorithm for finding shortest path that searches for the deepest node first.
DFS uses Stack data structure and psuedocode looks as follows:

1. add the starting node to stack, mark it as visiteed 
2. visit one of the unvisited neighbouring nodes, push to stack, mark it visited. 
    If all of the neighbouring nodes is visited, pop the latest node from stack 
4. repeat #2 untill stack becomes empty

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#example graph
graph = [
    [],
    [2,3,8],
    [1,7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# 1, 2, 7, 6, 8, 3, 4, 5

```

#### BFS (Breadth-First Search)

BFS is a search algorithm for finding shortest path that searches for the shallowest node first.
DFS uses Queue data structure and psuedocode looks as follows:

1. add the starting node to queue, mark it as visited 
2. pop the node from queue, visit all of the unvisited neighbouring nodes, push to queue, mark it visited. 
4. repeat #2 untill stack becomes empty

```python
from collections import deque 

def bfs(graph, start, visited):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#example graph
graph = [
    [],
    [2,3,8],
    [1,7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

# 1, 2, 3, 8, 7, 4, 5, 6

```



