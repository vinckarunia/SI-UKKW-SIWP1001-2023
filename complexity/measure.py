import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_time(arr):
    start_time = time.time()
    bubble_sort(arr)
    return time.time() - start_time

# Test with different input sizes
input_sizes = [10, 50, 100, 200, 300, 400, 500]
times = []

for size in input_sizes:
    arr = list(range(size, 0, -1))  # Worst case scenario for bubble sort
    times.append(measure_time(arr))

# Plotting the results
plt.plot(input_sizes, times, marker='o')
plt.title('Time Complexity of Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
plt.savefig("time-complexity.png")
