# go though the array one value at a time
# compare the current value with the next value
# if the current value is greater than the next value, swap the values
# repeat the process until the array is sorted
class Bubble:
   def __init__(self,array):
      self.array = array;
   def sort(self):
      for i in range(len(self.array)):
         for j in range(len(self.array)-1-i):
            if self.array[j] > self.array[j+1]:
               self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
      return self.array
array = [2,33,4,1,5,38,9,20,0]
bubble_sort = Bubble(array)
print(bubble_sort.sort())