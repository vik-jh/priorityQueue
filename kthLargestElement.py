import heapq
def kthLargest(lst, k):
    heap=lst[:k]
    heapq.heapify(heap)
    for x in range(k,len(lst)):
        if lst[x]>heap[0]:
            heapq.heapreplace(heap,lst[x])
    return heap[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)