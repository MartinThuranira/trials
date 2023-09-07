from sqlalchemy import false


a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false] 

print(a,"is greater") if (a>b) else print(b,"is Greater")

def power(n):
    return lambda a: a ** n
 
 
# base = lambda a : a**2 get
# returned to base
base = power(2)
 
print("Now power is set to 2")
 
# when calling base it gets
# executed with already set with 2
print("8 powerof 2 = ", base(8))

age = 20

adult = True if age >= 10 else False

print ("You are an adult!" if adult else "You are not an adult!")