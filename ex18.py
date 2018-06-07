#This one is like ur sxripts argv

def print_two(*args):
    arg1,arg2 =args
    print(f"arg1: {arg1},arg2: {arg2}")


#ok
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


#take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


#no argument
def print_none():
    print("got nothing")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

