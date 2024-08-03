#factorial = 5!  = 5*4*3*2*1 =120

#using - for

n=4
empty= 1
if n <0:
   print ("invalid input")
if n == 0:
    print("fact = 1")

if n > 0:

    for i in range (1,n+1):
        empty=empty*i
print("fact of 5 is : " , empty)

#using recursion:
#function khud k andar khud k parent function ko call karata hai
