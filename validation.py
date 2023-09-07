def validate(n):
    check = 0
    a = any(char.isnumeric() for char in n)
    b = any(char.isupper() for char in n)
    c = any(char.islower() for char in n)
    
    d = a and b and c
    return d

def main():
    number = int(input())
    for n in range(number):
        test = input()
        print(validate(test))


if __name__ == "__main__":
    main()
        
