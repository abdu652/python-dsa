# create array
# initialize the first value of the array as the minimum value
#iterste though the array and compare the minimium value with current value
# if the current value is minimium update the minimum value
# change the following code to class based implementation


class MinFinder:
    def __init__(self, array):
        self.array = array
    
    def find_min(self):
        # Initialize the minimum value with the first element of the array
        min_val = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] < min_val:
                min_val = self.array[i]
        return min_val

# Example usage
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
finder = MinFinder(my_array)
