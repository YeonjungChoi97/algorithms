#백준 1966

import sys
from collections import deque

n = int(sys.stdin.readline())


for _ in range(n):
    n,m= map(int, str(sys.stdin.readline()).split())
    lst = deque(map(int,str(sys.stdin.readline()).split()))
    index_queue = deque(range(n))
    count=0
    while index_queue:
        if lst[index_queue[0]] ==max(lst):
            if index_queue[0] == m:
                print(count+1)
                break
            lst[index_queue[0]]=0
            index_queue.popleft()
            count+=1
        else:
            index_queue.append(index_queue.popleft())
