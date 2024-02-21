# year= int(input("Enter year"))
# if year % 4 !=0:
#     print("Not a leap year")
# else:
#     if year % 100 !=0:
#         print("Leap Year")
#     else:
#         if year % 400==0:
#             print("Leap Year")
#         else:
#             print("Not a leap year")




year =2000
print("leap year" if(year % 4 ==0 and  year % 100 !=0) or (year % 100==0 and year % 400==0 ) else "not a leap year")