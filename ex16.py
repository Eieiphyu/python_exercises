from sys import argv
script, filename = argv


print("WE r going to erase {filename}.")
print("If u don't want that, hit CTRL-C(^C).")
print("If u do want that, hit RETURN.")


input("?")


print("Opening file....")
target = open(filename, 'w')
print("Transcating the file.Goodbye!")
target.truncate()

print("I am going to ask you for three times.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("finally close")
target.close()


