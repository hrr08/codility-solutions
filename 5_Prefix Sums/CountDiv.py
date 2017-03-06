# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    # write your code in Python 2.7
    count = 0
    if K != 0:
        if A%K == 0:
            count += (B/K) - (A/K) + 1
        else:
            count += (B/K) - (A/K)
            
    return count