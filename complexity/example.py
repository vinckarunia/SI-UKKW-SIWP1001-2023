"""
example of time-complexity 
"""
from util.decorators import time_decorator

class contoh():
    def __init__(self, arr):
        self.arr = arr

    # contoh O(1) atau Constant Time Complexity
    @time_decorator
    def access_element(self, index):
        return self.arr[index]
        # contohnya 
        # arr = [1, 2, 3, 4, 5]
        # print(access_element(arr, 2))  # mengakses element pada index ke-2

    # contoh O(n) atau Linear Time Complexity
    @time_decorator
    def find_max(self):
        max_val = self.arr[0]
        for num in self.arr:
            if num > max_val:
                max_val = num
        return max_val

    # contoh O(log n) atau Logarithmic Time Complexity
    @time_decorator
    def binary_search(self, target):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    # contoh O(n^2) atau Quadratic Time Complexity
    @time_decorator
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]         

    # contoh O(n^3) atau Cubic Time Complexity
    @time_decorator
    def sum_triplets(self):
        n = len(self.arr)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total += self.arr[i] + self.arr[j] + self.arr[k]
        return total