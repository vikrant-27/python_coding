n=10
list=[] #empty list
result=''

for i in range (1,10+1):
    print(i)
    list.append(str(i)) #appending into empty list (string)
    i+=1
    result=','.join(list) #converting list to string

print(list) #printing stringed list
print(result) #final result

