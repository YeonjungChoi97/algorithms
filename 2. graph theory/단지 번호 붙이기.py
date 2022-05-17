#baekjoon 2667


#dfs 로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
#baekjoon 2667


#dfs 로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x,y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
    if (x <= -1 or x >= n) or (y <= -1) or (y >= n):
        return False
      #현재 노드를 방문하지 않았다면
    if graph[x][y] == 1:
          #해당노드 방문처리
        global count
        count += 1
        graph[x][y] = 0
          #상, 하, 좌, 우 의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#n, m 을 공백을 기준으로 구분하여 입력 받기
n = int(input())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#모든 노드에 대하여 음료수 채우기
result = 0
count = 0
house_no = []
for i in range(n):
    for j in range(n):
       #현재 위치에서 dfs 수행
        if dfs(i,j) == True:
            house_no.append(count)
            result += 1
            count = 0

print(result)
house_no.sort()
for i in house_no:
    print(i)
