def checkMaxHeap(lst):
    n = len(lst)
    
    for i in range(0, (n//2)):
        left = (2*i) + 1
        right = left + 1
        #if lst[i]>lst[2*i+1] or lst[i]>lst[2*i+2]:
        if left<n and lst[left]>lst[i]:
            return False
        if right<n and lst[right]>lst[i]:
            return False
        #else:
            #return False
        
    return True
   

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')