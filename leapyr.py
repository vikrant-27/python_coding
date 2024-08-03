# to check if given number is leap yr or not
#normal - 365 , leap - 366
# condition
# for century years like 2000, 1000 etc:
#     if num %400==0 & num%100==0
# for non ceentury years:
#     if num%4==0 & num%100!=0

year=2000

if year%400==0 and year%100==0:
    print (year,"leap")
elif year%4==0 and year%100 !=0:
    print(year,"leap")
else:
    print(year,"not leap")