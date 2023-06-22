# first function says only hello world
def hello():
    print("Hello world")
    return

hello()

#second function takes three arguments and converts to list
def pack(arg1,arg2,arg3):
    mylist = [arg1,arg2,arg3]
    return mylist

list = pack("apples", "sandwich", "snack")
print(list)

#Third function prints out items in array | list
def eat_lunch(packed):
    for food in packed:
        if food == packed[0]:
            print("first I eat " + food)
        else:
            print("Next I eat " + food)
        
    print("My luchbox is empty!")
    return

eat_lunch(list)
