def solution(N):
    # write your code in Python 3.6
    old = bin(N)
    new = str(old)
    new = new[3:]
    #list_len = len(new)
    counter = 0
    new_counter = 0
    ones = 0

    for i in new:
        if i == "1":
            ones = ones + 1
        if i == "0":
            counter = counter + 1
            if new.index(i)+1 == "1":
                new_counter = counter
            if ones > 1:
                counter = 0
                ones = 1
                #break
                
        if counter > new_counter:
            new_counter = counter
    
    
    if ones < 1:
        new_counter = 0        
    return new_counter  

tester = 328
#solution(tester)
print (solution(tester))
print (bin(tester))