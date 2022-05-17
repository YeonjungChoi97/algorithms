#백준 1260
#DFS: Depth First Search, uses stack to find the shortest path, better when target is far from source, faster
#BFS: Breadth First Search, uses Queue to find the shortest path, better when target is closer to source, slower

from collections import deque

#첫째줄에 n,m,v 들어옴
n, m, v = map(int, input().split())

#graph 를 initialise 함, graph[0]의 포지션은 비워두기위해 N+1 의 길이를 갖는 리스트 생성 
graph = [[] for _ in range(n + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  graph[m1].append(m2)
  graph[m2].append(m1)
  
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[1]:
            ds(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[1]:
                queue.append(i)
                visited[i] = True
                
visited = [False] * n

dfs(graph, v, visited)

visited = [False] * n

bfs(graph, v, visited)
