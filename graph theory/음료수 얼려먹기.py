"""
 link : youtube.com/watch?v=7C9RgOcvkvo
 from 00:42:43.
 연결요소 찾기, connected component
 dfs or bfs, 연결요소의 갯수가 몇개인지.
 using dfs...  
 1. check up, down, left right unvisited nodes for a value of 0. 
    If exists, visit the node
 2. repeat 1 for connected nodes with such conditions
 3. repeat 1-2 steps and count unvisited nodes
"""

#dfs 로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x,y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if (x <= -1 or x >= n) or (y <= -1) or (y >= m):
    return False
  #현재 노드를 방문하지 않았다면
  if:



