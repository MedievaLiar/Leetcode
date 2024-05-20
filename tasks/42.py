from typing import List
from typing import Optional
from heapq import heappush, heappop

# Beats 99%, O(NKlogK)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def addTo_heap_And_HashTable(self, value, index): # updates hashMap and heap
            heappush(self.heap, value)
            try:
                self.hashTable[value].append(index)
            except KeyError:
                self.hashTable[value] = [index]
        
        # heap to find minimums quickly(O(1)) and adding each element O(log(k)) time
        self.heap = []
        
        # Hashtable to contain the lists of index containing this value
        self.hashTable = {}
        
        # Adding it instead of making it in-place using nodes would give us the same complexity (O(n*k) time and memory)
        returnedArray = []
        
        # Adding a data to hashTable and sortedKArray
        for index in range(len(lists)):
            node = lists[index]
            if node: #In case one array is empty
                addTo_heap_And_HashTable(self, node.val, index)
        
        # Go through all nodes:
        while self.heap:
            minValue = heappop(self.heap)
            
            # Now for each node where value = min:
            for index in self.hashTable[minValue]:
                returnedArray.append(minValue) # add to a result, it causes O(NK) 
                
                nextNode = lists[index].next
                
                # Update heap and hashMap:
                if nextNode != None: # In case we got the latest element in some linkedlist
                    addTo_heap_And_HashTable(self, nextNode.val, index)
                
                
                lists[index] = nextNode # go for a next node
                
            # Because we got all the elements used:
            self.hashTable[minValue] = []
        
        # Now let's make an linkedList :)
        returnedArray = returnedArray[::-1]
        node = None
        for value in returnedArray:
            node = ListNode(value, node)
        
        return node
            
