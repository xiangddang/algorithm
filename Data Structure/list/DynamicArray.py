class DynamicArray:
    # initialize the array with capacity, length and array
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity
    # get the element at index i
    def get(self, i: int) -> int:
        return self.array[i]
    # set the element at index i to n
    def set(self, i: int, n: int) -> None:
        self.array[i] = n
    # push back the element n to the array
    def pushback(self, n: int) -> None:
        # if the array is full, resize the array
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1
    # pop back the last element in the array
    def popback(self) -> int:
        # if the array is empty, return -1
        if self.length == 0:
            return -1
        # if the array is not empty, return the last element
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]
    # resize the array
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        # create a new array with the new capacity
        new_arr = [0] * self.capacity
        # copy the old array to the new array
        for i in range(self.length):
            new_arr[i] = self.array[i]
        self.array = new_arr
    # get the size of the array
    def getSize(self) -> int:
        return self.length
    # get the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity