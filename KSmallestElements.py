import heapq

def kSmallest(lst, k):
    heap = lst[:k]
    heapq._heapify_max(heap)
    n =len(lst)
    for i in range(k, n):
        if heap[0]>lst[i]:
            heapq._heapreplace_max(heap,lst[i])
    return heap

# main
size = int(input())
array = [int(x) for x in input().split()]
k = int(input())
if k < 0 or k > len(array):
  exit()
elements = kSmallest(array,k)
elements.sort()
for ele in elements:
  print(ele,end=" ")



