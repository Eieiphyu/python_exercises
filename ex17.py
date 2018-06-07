from sys import argv
from os.path import exists


script, from_file, to_file = argv


print(f"Copy from {from_file} to {to_file}")

#2 on i line how

in_file = open(from_file)
indata = in_file.read()

print(f"Input file is {len(indata)} bytes long")

print(f"Doesoutput file exist? {exists(to_file)}")

print(f"Ready, hit RETURN to continute CTRL-C to abort.")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright all sone")
out_file.close()
in_file.close()

