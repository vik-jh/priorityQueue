"""Implement the function RemoveMin for the min priority queue class.
For a minimum priority queue, write the function for removing the minimum element present. Remove and return the minimum element."""

class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        i=0
        lc=2*i+1
        rc=2*i+2
        l=self.getSize()
        while(i<l):
            if rc<=(l-1):
                if self.pq[lc].priority<self.pq[rc].priority and self.pq[lc].priority<self.pq[i].priority:
                    self.pq[lc],self.pq[i]=self.pq[i],self.pq[lc]
                    i=2*i+1
                    lc = 2 * i + 1
                    rc = 2 * i + 2

                elif self.pq[rc].priority<self.pq[lc].priority and self.pq[rc].priority<self.pq[i].priority:
                    self.pq[rc],self.pq[i]=self.pq[i],self.pq[rc]
                    i=2*i+2
                    lc = 2 * i + 1
                    rc = 2 * i + 2
                else:
                    break
            elif  rc>(l-1) and lc<(l-1) and self.pq[lc].priority<self.pq[i].priority:
                self.pq[lc],self.pq[i]=self.pq[i],self.pq[lc]
                i=i+1
                lc = 2 * i + 1
                rc = 2 * i + 2
            else:
                break








    def removeMin(self):
        self.pq[self.getSize()-1],self.pq[0]=self.pq[0],self.pq[self.getSize()-1]
        c=self.pq.pop().ele
        self.__percolateDown()
        return c


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1

