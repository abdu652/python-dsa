class Insertion:
    def __init__(self):
        pass
    def insert(self,data):
        l = len(data)
        for i in range(1,l):
            key = data[i]
            j = i-1
            while j >=0 and key < data[j]:
                data[j+1] = data[j]
                j = j-1                
            data[j+1] = key
        return data
i = Insertion()
a = [6,1,7,3,10,8]
print("original array:",a)
print("sorted array:",i.insert(a))    
