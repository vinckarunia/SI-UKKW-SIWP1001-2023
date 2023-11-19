import time 
from complexity.example import contoh

if __name__ == "__main__":

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    ex = contoh(arr)
    
    index_to_access = 2
    t1 = time.time()
    t_constant = ex.access_element(index_to_access)
    t2 = time.time()
    t_exec = t2 - t1

    print("Running time of t_constant: {}".format(t_exec))




