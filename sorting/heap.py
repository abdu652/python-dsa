class Heap:
    def __init__(self, array):
        self.array = array
        self.size = len(array)  
        
    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < self.size and self.array[l] > self.array[largest]: 
            largest = l
        if r < self.size and self.array[r] > self.array[largest]:  
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(largest)       # recursively heapify the affected sub-tree
            
    def heap(self):
        n = (self.size // 2) - 1
        for i in range(n, -1, -1):
            self.heapify(i)  
        return self.array
    def heapSort(self):
        for i in range(self.size-1,0,-1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.size -= 1      # exclude the sorted part
            self.heapify(0)
        return self.array    
arr = [4, 10, 3, 5, 1]
heap = Heap(arr)
print("Original array:",arr)  # Output: [4, 10, 3, 5, 1]
print("genarated heap:",heap.heap())  # Output: [10, 5, 3, 4, 1]        
print("Sorted heap:",heap.heapSort())  # Output: [1, 3, 4, 5, 10]        