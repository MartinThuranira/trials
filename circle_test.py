
def solution(A, B, X, Y):
    # write your code in Python 3.6
    c = 20**2
    count = 0
    print(type(B))
    for (a,b) in zip(A,B):
        x = abs(X - a) ** 2
        y = abs(Y - b) ** 2
        count = count + 1
        print(a,b)
        
        if  x + y > c :
            return -1
        else:
            return A.index(count)

res = solution([200,100,300],[300,100,400],100,100)
print(res)