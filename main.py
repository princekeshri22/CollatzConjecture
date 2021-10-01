#Collatz Conjecture

# The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows:

# If the previous term is even, the next term is half of the previous term.
# If the previous term is odd, the next term is 3 times the previous term plus 1.
# The conjecture is that no matter what value of n, the sequence will always reach 1.

# if x is odd then next term 3*x + 1
# if x is even then next term x//2

# def even(n):
#     return n%2==0

def nextVal(n):
    if(n%2 == 0):
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
