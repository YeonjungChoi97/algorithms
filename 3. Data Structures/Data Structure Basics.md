### Data Structure Basics
Codes and lectures provided by CS Dojo: https://www.youtube.com/watch?v=bum_19loj9A&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H

#### Trees
```python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_values(root):
    if (root == None):
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(sum_values(node2))

```


#### Binary Search

```python
def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
	        return mid
        elif target < arr[mid]:
	        right = mid - 1
        else:
            left = mid + 1
    return -1

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
assert search(arr1, 11) == 6
assert search(arr1, 13) == 7
assert search(arr1, -2) == 0
assert search(arr1, 8) == 4
assert search(arr1, 6) == -1
assert search(arr1, 14) == -1
assert search(arr1, -4) == -1

arr2 = [3]
assert search(arr2, 6) == -1
assert search(arr2, 2) == -1
assert search(arr2, 3) == 0

print("If you didn't get an assertion error, this program has run successfully.")
```


#### Quick Sort
divide and conquer + partition

best case - O(nlogn)  
worst case - O(nlogn)  
average case - O(n^2) 

```python
def quicksort(arr):
    qs(arr, 0, len(arr) - 1)

def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = []
a4 = [3, 1, -1, 0, 2, 5]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]

quicksort(a1)
quicksort(a2)
quicksort(a3)
quicksort(a4)
quicksort(a5)
quicksort(a6)
quicksort(a7)
quicksort(a8)
quicksort(a9)

assert a1 == [1, 2, 3]
assert a2 == [1, 2, 3]
assert a3 == []
assert a4 == [-1, 0, 1, 2, 3, 5]
assert a5 == [0, 0, 1, 1, 2, 2, 2, 2, 2, 4, 4]
assert a6 == [0]
assert a7 == [-2, -1, 0, 1, 2, 3, 4]
assert a8 == [1, 2, 3, 4, 5, 6, 7]
assert a9 == [2, 2, 2, 2, 2, 2, 2]

print("If you didn't get an assertion error, this program has run successfully.")
```

#### Stacks and Queues 

Stack - first in last out
Queue - first in first out

#### Hash Table and Dictionaries
Dictionary: data structure of key, value pair
- search, insert, delete: time complexity of O(1)  


How to choose hash function (e.g. djb2 -> string hash function)
1. fast to compute
2. avoid collisions 

How to deal with collisions
1. Chaining  
store key-value pair in a linked list, all the key-value pairs assigned in the slot  
- insertion - O(1)  
- search - O(1+a)
2. Linear Probing
if collision happens, put in next empty left slot. pretty inefficienct, clusters happen
3. Double Hashing
if collision happens, check next empty nth element.
everytime collision happens, we produce silghtly different sequence each time.
