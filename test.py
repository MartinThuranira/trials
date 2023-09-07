def solution(A):
    # write your code in Python 3.6
    A.sort()
    current = A[0]
    for i in A:
        if i - current > 1:
            return current+1
            break
        else:
            current = i
        if A[-1] - A[-2] <= 1:
            return A[-1] + 1
            break
        if A[-1] <= 0:
            return 1
            break
        
print(solution([1, 3, 6, 4, 1, 2,2,7,7,100,-5,-4]))