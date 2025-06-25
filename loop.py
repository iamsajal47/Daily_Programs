# n = int(input("enter the value: "))
# sum = 0

# for i in range(1,n+1):
#     sum = sum + i

# print(f"sum is{sum}")

# even odd sum 

# n = int(input("Enter the number: "))

# oddsum = 0
# evensum = 0

# for i in range(1,n+1):
#     if i % 2 ==0:
#         evensum = evensum + i
#     else:
#         oddsum = oddsum + i


# print(f"Even sum is {evensum} and Odd sum is {oddsum}")

# n = int(input("tell your range: "))

# for i in range(1,n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)


# n = int(input("tell your number: "))

# for i in range(7,n+1):
#     if i % 7 == 0 or i % 10 == 0:
#         print(i)

# s = int(input("tell your start number: "))
# e = int(input("tell your end point: "))

# for i in range(s,e+1):
#     if i % 7 == 0 or i % 10 == 0:
#         print(i)

# 12 ke factor is - 1,2,3,4,6,12

# 13 ke - 1, 13 jiske 2 factor ho usko prime number 


num = int(input("which number factor you want: "))

for i in range(1,num+1):
    if num % i == 0:
        print(i)


