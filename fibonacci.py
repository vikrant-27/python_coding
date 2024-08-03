
# 1,2,3,4,5 = 3+3,4,5

# n=5
# sum=1
# summ=0
# for i in range(1,n+1):
#     sum=sum*i
#     summ=summ+sum
# print(summ)

#generating a series
# in any series 0,1 will be constant i.e at the 1st and 2nd position
# i.e a=0 & b=1 & c=0+1=1
# in next loop a=b , b=c , c=a+c

a=0
b=1
inp =int (input("enter a nuber for fibonacci series : "))
if inp ==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1, inp + 1):
        c = a + b
        a = b
        b = c
        print(c)


