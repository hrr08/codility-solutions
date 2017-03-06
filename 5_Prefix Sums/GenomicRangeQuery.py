# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):
    N = len(S)
    sumA = [0]*(N+1)
    sumC = [0]*(N+1)
    sumG = [0]*(N+1)
    sumT = [0]*(N+1)
 
    for i, char in enumerate(S):
        sumA[i+1] = sumA[i]
        sumC[i+1] = sumC[i]
        sumT[i+1] = sumT[i]
        sumG[i+1] = sumG[i]
        if char == 'A':
            sumA[i+1] += 1
        elif char == 'C':
            sumC[i+1] += 1
        elif char == 'G':
            sumG[i+1] += 1
        elif char == 'T':
            sumT[i+1] += 1

    #print sumA, sumC, sumG, sumT 
 
    res = [0]*len(P)
    for i in xrange(len(P)):
        A = sumA[Q[i] + 1]- sumA[P[i]]
        C = sumC[Q[i] + 1]- sumC[P[i]]
        G = sumG[Q[i] + 1]- sumG[P[i]]
        T = sumT[Q[i] + 1]- sumT[P[i]]
        if A > 0:
            res[i] = 1
        elif C > 0:
            res[i] = 2
        elif G > 0:
            res[i] = 3
        elif T > 0:
            res[i] = 4
    return res