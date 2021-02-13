sum1 = lambda x,y:x+y
print(sum1(12,13))
a,b=map(int,input().split())
print((lambda a,b:a-b) (a,b))


print("Sum of 10 natural numbers")
print((lambda : sum(range(1,11)))())

