# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

#!/bin/python3

import math
import os
import random
import re
import sys
import threading
# Complete the stepPerms function below.
valid_steps = 0
def stepPerms(n, current_stage=0):
    valid_steps = 0
    if current_stage == n:
       return 1 
    elif current_stage > n:
        return 0 
    else:
        step_1 = threading.Thread(
            target=stepPerms, args=(n, current_stage + 1,)
        ).start() 
        step_2 = threading.Thread(
            target=stepPerms, args=(n, current_stage + 2,)
        ).start()
        step_3 = threading.Thread(
            target=stepPerms, args=(n, current_stage + 3,)
        ).start()
        step_1.join()
        step_2.join()
        step_3.join()
        s1 = 0
        s2 = 0
        s3 = 0

        if step_1:
            s1 = step_1
        if step_2:
            s2 = step_2
        if step_3:
            s3 = step_3
        valid_steps  = (
            s1 + s2 + s3
        )
    return valid_steps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        print(res)
        # fptr.write(str(res) + '\n')

    # fptr.close()
