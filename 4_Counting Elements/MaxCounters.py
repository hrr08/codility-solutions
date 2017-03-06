# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7
    result = [0] * N
    res = {}
    minval = 0
    maxCount = 0
    maxIndex = 0
    
    for i in xrange(len(A)):
        if A[i] <= N:
            if (A[i]-1) not in res:
                res[A[i]-1] = 1
            else:
                res[A[i]-1] = res[A[i]-1] + 1
                
            if maxCount < minval + res[A[i]-1]:
                maxCount = minval + res[A[i]-1]
                minval = 0

        else:
            res = {}
            minval = maxCount
            initMax = maxCount
            

    for i in xrange(len(result)):
        result[i] = initMax
        if (i in res) and res[i] !=0:
            result[i] += res[i]
        
        
    return result




























# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7
    result = [0] * N

    maxCount = 0
    maxCurrent = 0
    
    for i in xrange(len(A)):
        if A[i] <= N:
            if maxCount > result[A[i]-1]:
                result[A[i]-1] = maxCount
            
            result[A[i]-1] += 1
            
            if maxCurrent < result[A[i]-1]:
                maxCurrent = result[A[i]-1]

        else:
            maxCount = maxCurrent

    for i in xrange(len(result)):
        if result[i] < maxCount:        
            result[i] = maxCount
        
        
    return result