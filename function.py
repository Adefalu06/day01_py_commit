# def hello():
#     print("Hello World")
# hello()

def sum(num1, num2):
    if (type (num1) is not int or type (num2) is not int):
        return
    return num1 + num2
total=sum(1,2)
print(total)

def multiple_data(*arg):
    print(arg)
    print(type(arg))
multiple_data("Adefalu", "Malik", "Monday", "Sunday") 

def multi_items(**doc):
    print(doc)
    print(type(doc))
multi_items(day="Friday", week= "week 2")