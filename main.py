import time 
import argparse
import ast
from complexity.example import contoh
from search.linearSearch import LinearSearch
#tambahkan disini misalnya from sort.nama_algorithma import nama_fungsinya

def parse_input(input_str):
    try:
        #validasi inputnya
        input_list = ast.literal_eval(input_str)
        if not isinstance(input_list, list):
            raise ValueError
        return input_list
    except (ValueError, SyntaxError):
        raise argparse.ArgumentTypeError(f"Invalid list input: {input_str}")

def main ():
    parser = argparse.ArgumentParser(description="mengukur algorithm runtime.")
    parser.add_argument('algorithm', help='nama algorithm', choices=['linear_search', 'examples']) ### tambahkan disini algoritma yang kalian buat
    parser.add_argument('--in_data', type=parse_input, help='Input list in Python list format, e.g., "[1, 2, 3]"')
    parser.add_argument('--target', type=int, help='Target number for search algorithms')
    args = parser.parse_args()

    if args.algorithm == 'linear_search':
        if args.in_data is not None and args.target is not None:
            searcher = LinearSearch()
            searcher.search(args.in_data, args.target)
    elif args.algorithm == 'examples':
        if args.in_data is not None:
            ex = contoh(args.in_data)
            # call a method from Examples class here
            # ex.some_method()

if __name__ == "__main__":

    main()

    # arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    # ex = contoh(arr)
    
    # index_to_access = 2
    # t1 = time.time()
    # t_constant = ex.access_element(index_to_access)
    # t2 = time.time()
    # t_exec = t2 - t1

    # print("Running time of t_constant: {}".format(t_exec))




