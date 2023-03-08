import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#

def bfs(n, m, edges):
    # Write your code here
    print('bfs')

if __name__ == '__main__':
     first_multiple_input = input().rstrip().split()

     n = int(first_multiple_input[0])

     m = int(first_multiple_input[1])

     edges = []

     for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))


     bfs(n, m, edges)
