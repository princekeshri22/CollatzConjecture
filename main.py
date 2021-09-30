#Collatz Conjecture

# if x is odd then next term 3*x + 1
# if x is even then next term x//2

def even(n):
    return n%2==0

def nextVal(n):
    if(even(n)):
        return n//2
    else:
        return 3*n+1

num = int(input("Enter start parameter :- "))
i = 0

while(num != 1):
    num = nextVal(num)
    print(num)
    i += 1
print("\n\n")
print(i)

#---------------------------------