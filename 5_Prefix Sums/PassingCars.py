# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    #N = len(A)
    #P = [0] * (N+1)
    sum = 0
    factor = 0
    for i in xrange(len(A)):
        if A[i] == 0:
            factor += 1
        if A[i] == 1:
            if sum+factor > 1000000000:
                return -1
            else:
                sum += factor
            
    return sum