def solution(A):
    # write your code in Python 3.6
    new_maximum = 0
    maximum = 0
    for i in A:
        if i%3 == 0:
            maximum = i
        if maximum > new_maximum:
            new_maximum = maximum
    return new_maximum

print(solution([-1,-2,0,6]))