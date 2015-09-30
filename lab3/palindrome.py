
# Input function lets you input a string into the variable
string = input("Please enter a string: ")
count = 0

#print prints to the console
print(string)

stringlen = len(string )

print(stringlen)

for i  in range(0, stringlen):
  count = count + 1

print(count)