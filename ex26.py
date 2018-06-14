print("How old r u?",end= ' ')
age=input()
print("How tall r u?",end=' ')
height=input()
print("How much do u weight",end =' ')
weight=input()

print(f"So ur {age} old,{height} tall and{weight} heavy.")

from sys import argv
script,filename = argv

txt = open(filename)

print("here's ur file {filename}:")
print(txt.read())

print("Type file agai:")
file_again = input(">")
txt_again=open(file_again)

print(txt_again.read())

print('Let\'s prctice everything')
print('You\'d need to knoe \'bout escapes with that do:')
print('\n newlines and \t tabs:')

poem="""
\tThe lovely world
with logics so firmly planted
cannot discern \n the needs of love
nor comprenhed passion from intution
and requires an explanatio
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6
print(f"THis sould be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))

# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cats = 20
dogs = 15

if people < cats :
    print("2 many cats! The word is doomed!")

if people > cats :
    print("not many cats! the world is saved!")

if people < dogs :
    print("The world id drooled on!")

if people > dogs :
    print("The world is dry!")

dogs += 4
if people >= dogs :
    print("People are greater tha or equal to dogs.")

if people <= dogs :
    print("People are less tha or equal to dogs.")

if people == dogs :
    print("People are dogs.")

