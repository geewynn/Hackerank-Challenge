import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sort_numbers = sorted(arr)
    max_sum = sum(sort_numbers[1:])
    min_sum = sum(sort_numbers[:4])
    print(str(min_sum)+ ' '+ str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
