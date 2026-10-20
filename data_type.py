#casting a number 
# year = str(1999)
# print(type(year))
# print(year)

# statement = "I like Quran from" + " " + year + "s."
# print(statement)

# band = {
#     "position":"Top",
#     "Age":"22"
# }

# band2 = dict(position='Top', Age= '22')
# print(band)
# print(band2)
# print(type(band))
# print(len(band))

# #Access Items in dict
# print(band["position"])
# print(band.get("Age"))

# #list all values
# print(band.values())

# #List all keys 
# print(band.keys())

# #List keys/values as tuple
# print(band.items())

# #change values in dic
# band["position"] ="Leader"
# band.update({"Day":"Morning"}) 
# print(band)

# value =1
# while value <15:
#     value+=1
#     if value ==7:
#        continue
#     print(value)
# else: 
#    print("this is the value of :" + str(value))

counter = 1
# TIME_LIMIT = 60

# while counter <= TIME_LIMIT:
#     print(counter)
#     counter = counter + 1

# print("Time's up!")

# names = ["fadilu", "sharafa", "ikire"]
# actions = ["code," "eat", "sleep"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

# timeLimit = 60

# for i in range (0, timeLimit, +1):
#     print(i)

# evenNum = 21

# for i in range(0, evenNum, +2):
#     print(i)

password = "secret1234"
userPin = input("Enter password: ")

while userPin != password: 
    print("Enter correct password")
    input("Try again: ")
print("Access Granted!")
