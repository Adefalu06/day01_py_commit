def add_num(a,b):
    return a + b
sum =add_num(2,5)
print(sum)


# def is_even(num):
#     while num :
#         if num %2 == 0:
#             print("Even Number!")
#         else:
#             print("Odd number!")
            
#         return num
# number =int(input("Enter a number ",))
# is_even(number)


# def large_num(number):
#     large= max(number)
#     return large

# numbers = [21,1,3,30]
# print(large_num(numbers))

def large_num(number):
    large = number[0]

    for num in number:
        if num > large:
            large = num
    return large

numbers = [21, 1, 3, 30]
print("This is the largest number from the list: ",large_num(numbers))

def small_num(number):
    small = number[0]

    for num in number:
        if num < small:
            small = num

    return small


numbers = [21, 1, 3, 30]
print(f"smallest number ",small_num(numbers))