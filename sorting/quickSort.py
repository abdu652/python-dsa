class QuickSort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)
        
    def partition(self, start, end):
        pivot = self.array[end]
        pIndex = start
        for i in range(start, end):
            if self.array[i] <= pivot:
                self.array[pIndex], self.array[i] = self.array[i], self.array[pIndex]
                pIndex += 1
        # Swap the pivot element with the element at pIndex
        self.array[pIndex], self.array[end] = self.array[end], self.array[pIndex]
        return pIndex
       
    def quickSort(self, start, end):
        if start < end:
            pIndex = self.partition(start, end)
            self.quickSort(start, pIndex - 1)
            self.quickSort(pIndex + 1, end)  # Use end, not self.size-1

a = [3, 5, 8, 1, 7, 9, 2, 4]
end = len(a) - 1
q1 = QuickSort(a)
q1.quickSort(0, end)
print(q1.array)  # Output: [1, 2, 3, 4, 5, 7, 8, 9]