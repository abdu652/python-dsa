class Merge:
    def __init__(self):
        self.array = []
        self.size = 0
    def merge(self,left,right,array):
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                k += 1
                i += 1
            else:
                array[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
        return array
    def mergeSort(self,array):
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.mergeSort(array[:mid])
        right = self.mergeSort(array[mid:])
        return self.merge(left,right,array)
array = [2,33,4,1,5,38,9,20,0]
merge_sort = Merge()
print("original array:",array)  # Output: [2, 33, 4, 1, 5, 38, 9, 20, 0]    
print("sorted array",merge_sort.mergeSort(array))  # Output: [0, 1, 2, 4, 5, 9, 20, 33, 38]            
