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
  if graph[x][y] == 0:
      #해당노드 방문처리
      graph[x][y] = 1
      #상, 하, 좌, 우 의 위치들도 모두 재귀적으로 호출
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True
   return False

#n, m 을 공백을 기준으로 구분하여 입력 받기 
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
   graph.append(list(map(int, input())))

#모든 노드에 대하여 음료수 채우기
result = 0  
for i in range(n):
   for j in range(m):
       #현재 위치에서 dfs 수행
       if dfs(i,j) == True:
           result += 1

print(result)     



