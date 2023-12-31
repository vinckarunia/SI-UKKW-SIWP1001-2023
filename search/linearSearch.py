"""
Buat sebuag algorithm LinearSeach

"""
from typing import List
from util.decorators import time_decorator

class LinearSearch():
    @time_decorator
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1 
