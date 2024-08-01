for n in range(1,200):
    list=[]
    sum=0

    for i in str(n):
        list.append(int(i))
    lenth = len(list)
    for i in list:
        # i=i**lenth
        # sum=sum+i
        sum += i ** lenth
    if n==sum:
        print(f"{sum} is an armstrong number")
    else:
        continue



